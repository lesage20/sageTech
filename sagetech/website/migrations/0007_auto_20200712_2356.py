# Generated by Django 3.0.8 on 2020-07-12 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auto_20200712_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialaccount',
            name='icon',
            field=models.CharField(choices=[('dribble', 'fa-dribbble'), ('facebook', 'fa-facebook'), ('instagram', 'fa-instagram'), ('google-plus', 'fa-google-plus-g'), ('pinterest', 'fa-pinterest'), ('linkedin', 'fa-linkedin-in'), ('rss', 'fa-rss'), ('flickr', 'fa-flickr')], max_length=20, null=True),
        ),
    ]
