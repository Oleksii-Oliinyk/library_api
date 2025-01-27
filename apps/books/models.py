import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    published_year = models.PositiveIntegerField(default=datetime.date.today().year, 
                                                 validators=[MinValueValidator(1000), 
                                                 MaxValueValidator(datetime.date.today().year)])
    description = models.CharField(max_length=300)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.name + " | " + self.author
