# Generated by Django 3.0.5 on 2020-10-05 21:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0017_auto_20200930_0030'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ('-date_created',), 'permissions': [('can_moderate_article', 'Може одобрювати статті'), ('can_draft_article', 'Може створювати чернетку статті')]},
        ),
        migrations.RemoveIndex(
            model_name='article',
            name='articles_ar_slug_452037_idx',
        ),
    ]