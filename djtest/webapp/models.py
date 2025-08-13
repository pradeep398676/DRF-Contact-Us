from django.db import models

# Create your models here.


class ContactUsModel(models.Model):
    name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    address = models.TextField(blank=True, null=True)
    contactno = models.CharField(max_length=20, blank=True)
    dob = models.DateField(blank=True)
    gender = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"