from django.db import models

# Create your models here.


class Trialuser(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField("Full Name" , max_length=1024)