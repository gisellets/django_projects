# Generated by Django 5.1.3 on 2025-03-04 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cat',
            old_name='cat_text',
            new_name='cat_name',
        ),
    ]
