# Generated by Django 3.0.4 on 2020-03-28 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_code', models.CharField(max_length=200)),
                ('item_description', models.CharField(max_length=200)),
                ('item_price', models.CharField(max_length=200)),
            ],
        ),
    ]
