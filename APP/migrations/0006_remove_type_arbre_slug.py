# Generated by Django 2.2.6 on 2019-11-15 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0005_type_arbre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='type_arbre',
            name='slug',
        ),
    ]
