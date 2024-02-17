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


class CarDealer:
    def __init__(self, address, city, full_name, id, lat, long, short_name, st, zip):
        # Atributos del concesionario
        self.address = address
        self.city = city
        self.full_name = full_name
        self.id = id
        self.lat = lat
        self.long = long
        self.short_name = short_name
        self.st = st
        self.zip = zip

    def __str__(self):
        return "Dealer name: " + self.full_name

class DealerReview:
    def __init__(self, dealership, name, purchase, review, purchase_date, car_make, car_model, car_year, sentiment, id):
        self.dealership = dealership
        self.name = name
        self.purchase = purchase
        self.review = review
        self.purchase_date = purchase_date
        self.car_make = car_make
        self.car_model = car_model
        self.car_year = car_year
        self.sentiment = sentiment
        self.id = id

    def __str__(self):
        return f"Review by {self.name} for {self.dealership}: {self.review}"