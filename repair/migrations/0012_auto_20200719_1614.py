# Generated by Django 3.0.6 on 2020-07-19 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('repair', '0011_auto_20200617_2314'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='devicehistory',
            name='products',
        ),
        migrations.AddField(
            model_name='devicehistory',
            name='products',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='repair.Product', verbose_name='товар'),
        ),
        migrations.RemoveField(
            model_name='devicehistory',
            name='type_works',
        ),
        migrations.AddField(
            model_name='devicehistory',
            name='type_works',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='repair.TypeWork', verbose_name='вид работы'),
        ),
    ]