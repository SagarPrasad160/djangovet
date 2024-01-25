from django.db import models

# Create your models here.
class Owner(models.Model):
  first_name = models.CharField(max_length=200)
  last_name = models.CharField(max_length=200)
  phone = models.CharField(max_length=20)

  def get_absolute_url(self):
    return '/owner/list'


class Patient(models.Model):
  DOG = "DO"
  CAT = "CA"
  BIRD = "BI"
  REPTILE = "RE"
  OTHER = "OT"
  ANIMAL_TYPE_CHOICES = [
    (DOG, "Dog"),
    (CAT, "Cat"),
    (BIRD, "Bird"),
    (REPTILE, "Reptile"),
    (OTHER, "Other"),
  ]
  animal_type = models.CharField(max_length=2,choices=ANIMAL_TYPE_CHOICES,default=OTHER)
  breed = models.CharField(max_length=200)
  pet_name = models.CharField(max_length=20)
  age = models.IntegerField(default=0)
  owner = models.ForeignKey(Owner,on_delete=models.CASCADE)

  def get_absolute_url(self):
    return '/patient/list'



