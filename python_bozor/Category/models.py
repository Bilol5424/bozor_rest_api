from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    description = models.TextField()

    def str(self):
        return self.name