# Generated by Django 3.0.8 on 2020-07-17 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default='/static/images/usericon.png', null=True, upload_to='images'),
        ),
    ]
