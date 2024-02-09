from django.db import models
from django.utils import timezone


class CarMake(models.Model):
    # Campos del modelo CarMake
    name = models.CharField(max_length=100)
    description = models.TextField()

    # Otros campos que desees agregar

    def __str__(self):
        return self.name


class CarModel(models.Model):
    # Relación Many-To-One con CarMake
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)

    # Otros campos del modelo CarModel
    dealer_id = models.IntegerField()  # Ajusta esto según tu lógica de negocio
    name = models.CharField(max_length=100)
    CAR_TYPES = [
        ('Sedan', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'WAGON'),
        # Agrega más opciones según sea necesario
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES)
    year = models.DateField(default=timezone.now)

    # Otros campos que desees agregar

    def __str__(self):
        return f"{self.name} ({self.car_make.name})"
