# Generated by Django 5.1.3 on 2025-03-17 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0004_rename_specie_type_rename_specie_cat_type_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Treat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cats', models.ManyToManyField(to='cats.cat')),
            ],
        ),
    ]
