# Generated by Django 4.1.3 on 2022-11-13 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_subscribers_date_subscribers_email_subscribers_sex_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribers',
            name='date',
            field=models.DateField(default='2000-01-01'),
        ),
    ]
