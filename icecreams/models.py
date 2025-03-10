from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator 

class IceCream(models.Model):
    name = models.CharField(max_length=64, unique=True)
    static_image_path = models.URLField(blank=True, null=True)

    @property
    def image_path(self):
        return f'{settings.STATIC_URL}{self.static_image_path}'
    
    def __str__(self):
        return f"{self.name} ice cream"

class IceCreamBall(models.Model):
    ice_cream = models.ForeignKey(IceCream, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)], default=1)

    def __str__(self):
        return f"Ball of {self.ice_cream}"

# Create your models here.
class IceCreamBucket(models.Model):
    initial_quantity = models.IntegerField(validators=[MinValueValidator(1)], default=40)
    quantity = models.IntegerField(default=40)
    ice_cream = models.ForeignKey(IceCream, on_delete=models.CASCADE)

    @property
    def rounded_percent_ratio(self):
        return round(self.quantity * 100 / self.initial_quantity)

    def __str__(self):
        return f"Bucket contains {self.quantity} / {self.initial_quantity} balls of {self.ice_cream}"
    
class Recipe(models.Model):
    name = models.CharField(max_length=64, unique=True)
    ice_cream_balls = models.ManyToManyField(IceCreamBall)