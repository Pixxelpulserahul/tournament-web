# Generated by Django 5.1 on 2024-09-05 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginpage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlogin',
            name='password',
            field=models.CharField(max_length=100),
        ),
    ]
