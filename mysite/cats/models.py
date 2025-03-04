from django.db import models

# Create your models here.

class Cat(models.Model):
    cat_name = models.CharField(max_length=200)

    def __str__(self):
        return self.cat_name

    def get_absolute_url(self):
        return "/cats/%i/" % self.id
