# Generated by Django 3.1 on 2020-08-12 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0003_auto_20200812_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transacao',
            name='data',
            field=models.DateTimeField(),
        ),
    ]
