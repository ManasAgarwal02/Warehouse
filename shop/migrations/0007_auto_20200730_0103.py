# Generated by Django 3.0.8 on 2020-07-29 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_orderupdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderupdate',
            name='timeStamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]