# Generated by Django 4.2.5 on 2023-10-04 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0017_alter_stockportfolio_stockname'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockportfolio',
            name='buy_price',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
    ]
