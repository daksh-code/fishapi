# Generated by Django 3.1.7 on 2022-02-06 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20220201_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fishdetail',
            name='fish_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
