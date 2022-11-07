from django.db import models

# Create your models here.
firstname = models.Charfield(max_length=100)
email = models.EmailField(null=True, blank=True, max_length=100)
height = models.DecimalField(max_digits=10,decimal_places=5,null=True)
latitude = models.DecimalField(max_digits=22, decimal_places=16, mull=True, blank=True)
isActive = models.BooleanField(default=False, verbose_name="Zoning Fee")
birthdate = models.DateField(default=timezone.now, blank=True)
coach = models.ForeignKey(Person, on_delete=models.CASCADE)