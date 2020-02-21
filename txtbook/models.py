import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Textbook(models.Model):
    title = models.CharField(max_length=200, default='N/A')
    author = models.CharField(max_length=200, default='N/A')
    dept = models.CharField(max_length=100, default='N/A')
    classnum = models.CharField(max_length=100, default='N/A')
    sect = models.CharField(max_length=100, default='N/A')
    newPriceBookstore = models.CharField(max_length=100, default='0.0')
    usedPriceBookstore = models.CharField(max_length=100, default='0.0')
    amazonPrice = models.CharField(max_length=100, default='0.0')
    amazonLink = models.TextField(max_length=1000, default='N/A')
    isbn = models.CharField(max_length=100, default='N/A')
    def __str__(self):
        return self.title


class TextbookPost(models.Model):
    title = models.CharField(max_length=200, default='N/A')
    author = models.CharField(max_length=200, default='N/A')
    dept = models.CharField(max_length=100, default='N/A')
    classnum = models.CharField(max_length=100, default='N/A')
    isbn = models.CharField(max_length=100, default='N/A')
    sect = models.CharField(max_length=100, default='N/A')
    price = models.CharField(max_length=100, default='0.0')
    negotiable = models.CharField(max_length=100, default='Yes')
    exchangable = models.CharField(max_length=100, default='Yes')
    maxDiff = models.CharField(max_length=100, default='0.0')
    payment = models.CharField(max_length=200, default='Venmo')
    condition = models.CharField(max_length=100, default='5')
    additionalInfo = models.TextField(max_length=10000, default='N/A')
    datePublished = models.DateTimeField('date published')
    format = models.CharField(max_length=200, default='N/A')
    def __str__(self):
        return str(self.id) + ' ' + self.title
