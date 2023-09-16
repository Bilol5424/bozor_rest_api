from django.db import models
from User.models import User
from Category.models import Category
from location.models import Location

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    date_of_placement = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.name