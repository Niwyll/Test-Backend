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
    quantity = models.IntegerField(default=40)
    ice_cream = models.ForeignKey(IceCream, on_delete=models.CASCADE)

    def __str__(self):
        return f"Bucket contains {self.quantity} balls of {self.ice_cream}"