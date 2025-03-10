from django.db import models

# Create your models here.

class Type(models.Model):
    type_name = models.CharField(max_length=200, default='None')

    def __str__(self):
        return self.type_name

class Cat(models.Model):
    cat_name = models.CharField(max_length=200, default='No Catitos')
    type = models.ForeignKey(Type, on_delete=models.CASCADE)

    def __str__(self):
        return self.cat_name

    def get_absolute_url(self):
        return "/cats/%i/" % self.id
