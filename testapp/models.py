from django.db import models

# Create your models here.
from django.forms import ModelForm
from smart_selects.db_fields import ChainedForeignKey


class Continent(models.Model):
    continent = models.CharField(max_length=45)

    def __unicode__(self):
        return unicode(self.continent)


class Country(models.Model):
    continent = models.ForeignKey(Continent)
    country = models.CharField(max_length=45)

    def __unicode__(self):
        return unicode(self.country)


class Area(models.Model):
    country = models.ForeignKey(Country)
    area = models.CharField(max_length=45)

    def __unicode__(self):
        return unicode(self.area)


class Location(models.Model):
    continent = models.ForeignKey(Continent)
    country = ChainedForeignKey(
        Country,
        chained_field='continent',
        chained_model_field='continent',
        show_all=False, auto_choose=True,
    )
    area = ChainedForeignKey(Area, chained_field="country", chained_model_field="country")
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=100)


