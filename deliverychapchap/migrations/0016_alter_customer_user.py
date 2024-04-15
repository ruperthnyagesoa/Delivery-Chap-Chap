# Generated by Django 3.2.1 on 2021-06-17 06:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodkart', '0015_alter_orders_restaurant_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='user', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
