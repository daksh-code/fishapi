# Generated by Django 3.1.7 on 2022-02-01 19:52

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FishDetails',
            new_name='FishDetail',
        ),
    ]
