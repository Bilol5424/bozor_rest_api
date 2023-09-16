from django.db import models

class Location(models.Model):
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def str(self):
        return f"{self.address}, {self.city}, {self.country}"