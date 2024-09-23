from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    range = models.CharField(max_length=100)
    top_speed = models.CharField(max_length=100)
    battery = models.CharField(max_length=100)
    motor = models.CharField(max_length=100)
    charging_time = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
