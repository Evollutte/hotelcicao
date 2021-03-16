# Generated by Django 3.1.7 on 2021-03-16 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bedrooms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bedrooms',
            name='capacity',
            field=models.CharField(choices=[('c1', '1 Pessoa'), ('c2', '2 Pessoas'), ('c3', '5 Pessoas')], default='c1', max_length=2, verbose_name='Capacidade'),
        ),
        migrations.AlterField(
            model_name='bedrooms',
            name='category',
            field=models.CharField(choices=[('de', 'Deluxe'), ('hi', 'Higher'), ('st', 'Standard')], default='st', max_length=2, verbose_name='Categoria'),
        ),
        migrations.AlterField(
            model_name='bedrooms',
            name='service',
            field=models.CharField(choices=[('s1', 'Wi-Fi'), ('s2', 'Wi-Fi, Café'), ('s3', 'Wi-Fi, Café, Frigobar')], default='s1', max_length=2, verbose_name='Serviços'),
        ),
        migrations.AlterField(
            model_name='bedrooms',
            name='size',
            field=models.CharField(choices=[('s1', '30 M²'), ('s2', '60 M²'), ('s3', '90 M²')], default='s1', max_length=2, verbose_name='Tamanho'),
        ),
        migrations.AlterField(
            model_name='bedrooms',
            name='value',
            field=models.CharField(choices=[('v1', 'R$ 100'), ('v2', 'R$ 200'), ('v3', 'R$ 500')], default='v1', max_length=2, verbose_name='Valores'),
        ),
    ]
