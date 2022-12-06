from django.db import models

# Create your models here.
class Customer(models.Model):
    nama = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    alamat = models.TextField()

def _str_(self):
    return self.nama

