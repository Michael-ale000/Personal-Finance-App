# Generated by Django 4.2.5 on 2023-10-04 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Personal_Finance_Assistant', '0003_alter_incomerecord_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incomerecord',
            name='category',
            field=models.CharField(max_length=250),
        ),
    ]
