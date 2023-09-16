from django.db import models
from Product.models import Product
from User.models import User

class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date_of_comment = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f"Comment by {self.user.username} on {self.product.name}"