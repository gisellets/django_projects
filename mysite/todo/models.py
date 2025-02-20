from django.db import models

# Create your models here.

class Item(model.Model):
    item_text = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text
