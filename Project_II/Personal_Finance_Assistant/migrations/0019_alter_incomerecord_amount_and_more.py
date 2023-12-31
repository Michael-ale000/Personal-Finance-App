# Generated by Django 4.2.5 on 2023-10-04 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Personal_Finance_Assistant', '0018_alter_incomerecord_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incomerecord',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='incomerecord',
            name='category',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='incomerecord',
            name='title',
            field=models.CharField(max_length=250),
        ),
    ]
