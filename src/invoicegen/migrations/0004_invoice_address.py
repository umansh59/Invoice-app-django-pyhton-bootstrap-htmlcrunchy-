# Generated by Django 4.2.3 on 2023-07-28 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoicegen', '0003_invoice_line_eight_invoice_line_eight_quantity_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='address',
            field=models.CharField(blank=True, default='', max_length=200, null=True, verbose_name='Customer Name'),
        ),
    ]