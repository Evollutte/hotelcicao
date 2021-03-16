from django.db import models


class Categories(models.TextChoices):
    de = 'de', 'Deluxe'
    hi = 'hi', 'Higher'
    st = 'st', 'Standard'


class Sizes(models.TextChoices):
    s1 = 's1', '30 M²'
    s2 = 's2', '60 M²'
    s3 = 's3', '90 M²'

class Values(models.TextChoices):
    v1 = 'v1', 'R$ 100'
    v2 = 'v2', 'R$ 200'
    v3 = 'v3', 'R$ 500'


class Capabilities(models.TextChoices):
    c1 = 'c1', '1 Pessoa'
    c2 = 'c2', '2 Pessoas'
    c3 = 'c3', '5 Pessoas'


class Services(models.TextChoices):
    s1 = 's1', 'Wi-Fi'
    s2 = 's2', 'Wi-Fi, Café'
    s3 = 's3', 'Wi-Fi, Café, Frigobar'


class Bedrooms(models.Model):
    category = models.CharField(
        max_length=2,
        choices=Categories.choices,
        default=Categories.st,
        verbose_name='Categoria'
    )
    size = models.CharField(
        max_length=2,
        choices=Sizes.choices,
        default=Sizes.s1,
        verbose_name='Tamanho'
    )
    value = models.CharField(
        max_length=2,
        choices=Values.choices,
        default=Values.v1,
        verbose_name='Valores'
    )
    capacity = models.CharField(
        max_length=2,
        choices=Capabilities.choices,
        default=Capabilities.c1,
        verbose_name='Capacidade'
    )
    service = models.CharField(
        max_length=2,
        choices=Services.choices,
        default=Services.s1,
        verbose_name='Serviços'
    )
