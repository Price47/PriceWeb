from __future__ import unicode_literals
from django.db import models


from django.db import models
from datetime import date

# Create your models here.


class Television(models.Model):
    search_rank = models.IntegerField()
    search_date = models.DateField(default=date.today())
    search_term = models.CharField(max_length=256, default="none")
    name = models.CharField(max_length=256)
    rating = models.FloatField()
    reviews = models.IntegerField()
    top_3 = models.BooleanField(default=False)

    def __str__(self):
        return "[" + str(self.search_rank) + "] " + str(self.name) + "(" + str(self.rating) + ")\n"