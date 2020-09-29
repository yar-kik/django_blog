# Generated by Django 3.0.5 on 2020-09-29 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0012_auto_20200923_0041'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('D', 'Чернетка'), ('M', 'На модерації'), ('P', 'Опублікований')], default='', max_length=1, verbose_name='статус'),
        ),
    ]
