# Generated by Django 4.0.2 on 2022-03-02 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enderecos', '0001_initial'),
        ('core', '0005_pontoturistico_avaliacoes'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='enderecos',
            field=models.ManyToManyField(to='enderecos.Endereco'),
        ),
    ]
