# Generated by Django 3.0.2 on 2020-02-02 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20200202_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bosyu',
            name='main_text',
            field=models.TextField(max_length=1000),
        ),
    ]
