from django.db import models


class Device(models.Model):
    """Устройства"""
    name = models.CharField('Наименование', help_text='Модель устройства', max_length=150, default='')
    type = models.CharField('Тип устройства', max_length=50, default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Устройство'
        verbose_name_plural = 'Устройства'


class Article(models.Model):
    """Артикул"""
    article = models.CharField('Артикул', max_length=50, unique=True, blank=True, null=True)
    serial_number = models.CharField('Серийный номер', max_length=100, blank=True, null=True)
    image = models.ImageField('Изображение', upload_to='article/', blank=True, null=True)
    devices = models.ForeignKey(Device, verbose_name='устройство', blank=True, null=True, on_delete=models.CASCADE)
    date = models.DateTimeField(blank=True, null=True, auto_now_add=True)

    def __str__(self):
        return self.article

    class Meta:
        verbose_name = 'Артикул'
        verbose_name_plural = 'Артикулы'


class Product(models.Model):
    name = models.CharField('Наименование', max_length=100, blank=True, null=True)
    partcode = models.CharField('Парт код', max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class TypeWork(models.Model):
    name = models.CharField('Наименование', max_length=255, unique=True, blank=True, null=True)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вид работы'
        verbose_name_plural = 'Виды работ'


class StatusList(models.Model):
    name = models.CharField('Статус', max_length=50, unique=True, blank=True, null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статус устройства'
        verbose_name_plural = 'Статус устройств'


class Client(models.Model):
    name = models.CharField('ФИО', max_length=100, blank=True, null=True)
    phone = models.CharField('Телефон', max_length=100, blank=True, null=True)
    address = models.CharField('Адрес', max_length=255, blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    description = models.TextField('Комментарии')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Company(models.Model):
    name = models.CharField('Компания', max_length=100, blank=True, null=True)
    status = models.CharField('Статус', max_length=50, blank=True, null=True)
    phone = models.CharField('Телефон', max_length=50, blank=True, null=True)
    address = models.CharField('Адрес', max_length=255, blank=True, null=True)
    date = models.DateField(blank=True, null=True, auto_now_add=True)
    description = models.TextField('Комментарии')
    client = models.ForeignKey(Client, verbose_name='клиент', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'


class DeviceHistory(models.Model):
    articles = models.ForeignKey(Article, verbose_name='артикул', blank=True, null=True, on_delete=models.CASCADE)
    companies = models.ForeignKey(Company, verbose_name='компания', blank=True, null=True, on_delete=models.CASCADE)
    clients = models.ForeignKey(Client, verbose_name='клиент', blank=True, null=True, on_delete=models.CASCADE)
    type_works = models.ManyToManyField(TypeWork, verbose_name='вид работы', blank=True, null=True)
    products = models.ManyToManyField(Product, verbose_name='товар', blank=True, null=True)
    date = models.DateTimeField('Дата')
    work_time = models.TimeField('Норма/час', blank=True, null=True)
    status = models.ForeignKey(StatusList, verbose_name='статус', blank=True, null=True, on_delete=models.CASCADE)
    guarantee = models.DateField('Гарантия')
    description = models.TextField('Комментарии')

    def __str__(self):
        return self.articles.article

    # def get_context(self, request):
    #     context = super().get_context(request)
    #     devicehistory = DeviceHistory.objects.all()
    #     context['devicehistory'] = devicehistory
    #     return context

    class Meta:
        verbose_name = 'История устройства'
        verbose_name_plural = 'История устройств'


class ProductHistory(models.Model):
    products = models.ForeignKey(Product, verbose_name='товар', blank=True, null=True, on_delete=models.CASCADE)
    companies = models.ForeignKey(Company, verbose_name='компания', blank=True, null=True, related_name='company', on_delete=models.CASCADE)
    unit = models.CharField('Единица измерения', max_length=20, blank=True, null=True)
    count = models.IntegerField('Количество', blank=True, null=True)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    date_receipt = models.DateTimeField('Дата поступления')
    date_offs = models.DateTimeField('Дата списания')
    description = models.TextField('Комментарии')

    def __str__(self):
        return self.products.name

    class Meta:
        verbose_name = 'История товара'
        verbose_name_plural = 'История товаров'


class Warehouse(models.Model):
    products = models.ForeignKey(Product, verbose_name='товар', blank=True, null=True, on_delete=models.CASCADE)
    unit = models.CharField('Единица измерения', max_length=20, blank=True, null=True)
    companies = models.ForeignKey(Company, verbose_name='компания', blank=True, null=True, on_delete=models.CASCADE)
    count = models.IntegerField('Количество')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    date = models.DateTimeField('Дата', blank=True, null=True)

    def __str__(self):
        return self.products.name

    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склады'
