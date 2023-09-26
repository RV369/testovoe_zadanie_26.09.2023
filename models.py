from django.db import models


class Owner(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField()
    surname = models.CharField()
    patronymic = models.CharField()
    phone_number = models.CharField(max_length=12)


class Fleet(models.Model):
    id = models.AutoField(primary_key=True)
    id_owner = models.ManyToManyField(Owner)
    name = models.CharField()
    number_of_cars = models.PositiveIntegerField()


class Cars(models.Model):
    id = models.AutoField(primary_key=True)


class Driver(models.Model):
    id = models.AutoField(primary_key=True)
    cars = models.ManyToManyField(Cars)


class Route(models.Model):
    id = models.AutoField(primary_key=True)
    driver = models.ManyToManyField(Driver)
    cars = models.ManyToManyField(Cars)
