# Generated by Django 4.2.5 on 2023-10-04 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Personal_Finance_Assistant', '0019_alter_incomerecord_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incomerecord',
            name='category',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='incomerecord',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
