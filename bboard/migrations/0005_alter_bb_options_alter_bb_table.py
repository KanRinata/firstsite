# Generated by Django 4.2 on 2023-05-17 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0004_alter_icecream_quantity'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bb',
            options={'ordering': ['-published', 'title'], 'verbose_name': 'Объявление', 'verbose_name_plural': 'Объявления'},
        ),
        migrations.AlterModelTable(
            name='bb',
            table=None,
        ),
    ]