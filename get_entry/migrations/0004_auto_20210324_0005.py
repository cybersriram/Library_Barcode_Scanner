# Generated by Django 3.1.7 on 2021-03-24 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_entry', '0003_auto_20210324_0915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='in_out_rp',
            name='date',
            field=models.DateField(),
        ),
    ]
