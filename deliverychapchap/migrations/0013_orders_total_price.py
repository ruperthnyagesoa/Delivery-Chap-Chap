# Generated by Django 3.2.1 on 2021-06-10 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodkart', '0012_auto_20210610_1345'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
