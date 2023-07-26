from django.db import models

class Order(models.Model):
    phone_number = models.CharField(max_length=15)
    menu = models.CharField(max_length=100)

    def __str__(self):
        return f'Order by {self.phone_number} for {self.menu}'