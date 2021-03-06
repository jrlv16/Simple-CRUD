# Generated by Django 2.2.6 on 2019-10-03 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bonzai',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('age', models.PositiveSmallIntegerField()),
                ('taille', models.DecimalField(decimal_places=2, max_digits=3)),
                ('pays_origine', models.CharField(max_length=15)),
                ('type_arbre', models.CharField(choices=[('FEUIL-CADU', 'FEUILLU_CADUQUE'), ('FEUIL-PERS', 'FEUILLU_PERSISTANT'), ('CONIF-PERS', 'CONIFERE_PERSISTANT')], default='FEUIL-CADU', max_length=10, verbose_name="Type d'arbre")),
                ('provenance', models.CharField(max_length=20)),
                ('img_arbre', models.ImageField(blank=True, null=True, upload_to='logo/')),
            ],
        ),
    ]
