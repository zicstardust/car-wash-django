from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()
    cpf = models.CharField(max_length=12)

    def __str__(self) -> str:
        return self.name

class Car(models.Model):
    car = models.CharField(max_length=50)
    plate = models.CharField(max_length=50)
    year = models.IntegerField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    washes = models.IntegerField(default=0)
    repairs = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.car