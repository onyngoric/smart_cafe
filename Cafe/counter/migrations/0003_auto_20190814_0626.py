# Generated by Django 2.2.2 on 2019-08-14 03:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('counter', '0002_cashier'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cashier',
            old_name='name',
            new_name='username',
        ),
    ]
