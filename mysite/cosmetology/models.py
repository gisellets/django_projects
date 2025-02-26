from django.db import models

# Create your models here.

class Services(models.Model):
    text = models.CharField(max_length=200)


    def __str__(self):
        return self.text

class Timeslot(models.Model):
    name = models.CharField(max_length=200)
    services = models.ForeignKey(Services, on_delete=models.CASCADE)


    def __str__(self):
        return self.name
    
