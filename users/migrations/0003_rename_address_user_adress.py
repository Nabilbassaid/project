# Generated by Django 5.0.4 on 2024-04-29 21:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_address_user_phone_alter_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='address',
            new_name='adress',
        ),
    ]
