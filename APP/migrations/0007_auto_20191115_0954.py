# Generated by Django 2.2.6 on 2019-11-15 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0006_remove_type_arbre_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeFeuille',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Indefini', max_length=15)),
            ],
        ),
        migrations.DeleteModel(
            name='Type_Arbre',
        ),
    ]
