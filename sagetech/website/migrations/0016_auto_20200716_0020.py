# Generated by Django 3.0.8 on 2020-07-16 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0015_auto_20200716_0018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialaccount',
            name='icon',
            field=models.CharField(choices=[('linkedin', 'fa-linkedin-in'), ('facebook', 'fa-facebook'), ('dribble', 'fa-dribbble'), ('flickr', 'fa-flickr'), ('google-plus', 'fa-google-plus-g'), ('rss', 'fa-rss'), ('pinterest', 'fa-pinterest'), ('instagram', 'fa-instagram')], max_length=20, null=True),
        ),
    ]
