# Generated by Django 4.2 on 2023-05-02 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0008_alter_openinghour_options_and_more'),
        ('orders', '0002_alter_order_country_alter_order_phone_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_data',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='vendors',
            field=models.ManyToManyField(blank=True, to='vendor.vendor'),
        ),
    ]
