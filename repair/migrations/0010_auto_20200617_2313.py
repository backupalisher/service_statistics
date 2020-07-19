# Generated by Django 3.0.6 on 2020-06-17 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repair', '0009_auto_20200616_0030'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='devicehistory',
            name='type_works',
        ),
        migrations.AddField(
            model_name='devicehistory',
            name='type_works',
            field=models.ManyToManyField(blank=True, null=True, to='repair.TypeWork', verbose_name='вид работы'),
        ),
    ]
