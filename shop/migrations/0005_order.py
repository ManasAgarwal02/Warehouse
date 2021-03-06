# Generated by Django 3.0.8 on 2020-07-29 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20200727_1503'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=50)),
                ('email', models.CharField(default='', max_length=60)),
                ('address', models.CharField(default='', max_length=112)),
                ('phone', models.CharField(default='', max_length=14)),
                ('city', models.CharField(default='', max_length=500)),
                ('state', models.CharField(default='', max_length=500)),
                ('zip_code', models.CharField(default='', max_length=500)),
                ('items_json', models.CharField(default='', max_length=1000)),
            ],
        ),
    ]
