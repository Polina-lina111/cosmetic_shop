from django.db import models


class Product(models.Model):

    title = models.CharField(
        max_length=100
    )

    brand = models.CharField(
        max_length=100
    )

    description = models.TextField()

    price = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.title