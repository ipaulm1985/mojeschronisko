from django.db import models

# Create your models here.

class Pies(models.Model):
    nazwa = models.CharField(max_length=100)
    rasa = models.CharField(max_length=100)
    plec = models.CharField(max_length=100)
    wiek = models.DateField()
    # wiek = models.IntegerField()  pomyslec

class Badania(models.Model):
    nazwa = models.CharField(max_length=100)


class Pies_badania(models.Model):
    pies = models.ForeignKey(Pies, on_delete=models.CASCADE)
    badania = models.ForeignKey(Badania, on_delete=models.CASCADE)
    data_badania = models.DateField(auto_now=True)


class Leczenie(models.Model):
    nazwa = models.CharField(max_length=100)


class Pies_leczenie(models.Model):
    pies = models.ForeignKey(Pies, on_delete=models.CASCADE)
    leczenie = models.ForeignKey(Leczenie, on_delete=models.CASCADE)
    data_leczenia = models.DateField(auto_now=True)


class Dieta(models.Model):
    nazwa = models.CharField(max_length=100)


class Pies_dieta(models.Model):
    pies = models.ForeignKey(Pies, on_delete=models.CASCADE)
    dieta = models.ForeignKey(Dieta, on_delete=models.CASCADE)
    data_diety = models.DateField(auto_now=True)


class Lokalizacja(models.Model):
    boks = models.SmallIntegerField()