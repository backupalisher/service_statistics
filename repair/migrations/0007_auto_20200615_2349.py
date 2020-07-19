# Generated by Django 3.0.6 on 2020-06-15 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('repair', '0006_auto_20200615_2235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='devicehistory',
            name='articles',
        ),
        migrations.AddField(
            model_name='devicehistory',
            name='articles',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='repair.Article', verbose_name='артикул'),
        ),
        migrations.RemoveField(
            model_name='devicehistory',
            name='clients',
        ),
        migrations.AddField(
            model_name='devicehistory',
            name='clients',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='repair.Client', verbose_name='клиент'),
        ),
        migrations.RemoveField(
            model_name='devicehistory',
            name='companies',
        ),
        migrations.AddField(
            model_name='devicehistory',
            name='companies',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='repair.Company', verbose_name='компания'),
        ),
        migrations.RemoveField(
            model_name='producthistory',
            name='companies',
        ),
        migrations.AddField(
            model_name='producthistory',
            name='companies',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='company', to='repair.Company', verbose_name='компания'),
        ),
        migrations.RemoveField(
            model_name='warehouse',
            name='companies',
        ),
        migrations.AddField(
            model_name='warehouse',
            name='companies',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='repair.Company', verbose_name='компания'),
        ),
    ]
