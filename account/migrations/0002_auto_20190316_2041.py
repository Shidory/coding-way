# Generated by Django 2.1.7 on 2019-03-16 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createaccount',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]
