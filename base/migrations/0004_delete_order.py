# Generated by Django 4.2.2 on 2023-07-03 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_order_email_order_phonenumber'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
    ]