# Generated by Django 4.1.7 on 2023-04-05 08:02

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Crowdfunding', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Campaign',
            new_name='Fundraiser',
        ),
        migrations.RenameField(
            model_name='pledge',
            old_name='campaign',
            new_name='fundraiser',
        ),
    ]