#Django
from django.db import models

# Create your models here.

class QueryModel (models.Model):
    """
        Query Model

        Model with four fields: 'country_code', 'series_code', 'year', adn 'value'.
        Each instance of this model represents a queyr

        Attributes:
            country_code (CharField): A string that represents the country code, with 200 limit of characters.
            series_code (CharField): A string that represents the series code,with 200 limit of characters.
            year (IntegerField): An integer that represents the year.
            value (FloatField): A float that represents the value.
        

    """
    country_code = models.CharField(max_length=200)
    series_code = models.CharField(max_length=200)
    year = models.IntegerField()
    value = models.FloatField()
