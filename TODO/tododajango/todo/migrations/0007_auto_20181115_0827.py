# Generated by Django 2.1 on 2018-11-15 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0006_auto_20181115_0820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='name',
            field=models.TextField(default='None'),
        ),
        migrations.AlterField(
            model_name='products',
            name='phoneNumber',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='pinCode',
            field=models.IntegerField(null=True),
        ),
    ]