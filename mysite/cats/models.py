from django.db import models

# Create your models here.

class Cat(models.Model):
    cat_text = models.CharField(max_length=200)

    def __str__(self):
        return self.cat_text

    def get_absolute_url(self):
        return "/cats/%i/" % self.id
