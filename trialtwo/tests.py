from django.test import TestCase

# Create your tests here.

class Trialuser(models.Model):
    name = models.CharField("Full Name", max_length=1024)