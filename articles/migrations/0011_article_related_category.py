# Generated by Django 3.0.5 on 2020-09-23 00:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('archives', '0001_initial'),
        ('articles', '0010_auto_20200921_1829'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='related_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='archives.InfoBase'),
        ),
    ]
