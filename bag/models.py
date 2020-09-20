from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Bonus(models.Model):
    class Meta:
        verbose_name_plural = 'Bonuses'

    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=False)
    expires_on = models.DateField()
    description = models.CharField(help_text="Describes what the amount is for on a discount by discount basis.", max_length=256)
    amount = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
