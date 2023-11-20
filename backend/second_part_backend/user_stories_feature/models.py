#Django
from django.db import models

# Create your models here.

class QueryModel (models.Model):
    """
        Query Model

        Model with four fields: 'country_code', 'series_code', 'year', and 'value'.
        Each instance of this model represents a query.

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


class SavedQuery(models.Model):
    """
        SavedQuery

        Model with four fields: 'name', 'comment', 'username' 
        and 'query' is an instance of QueryModel as Foreign Key.

        Attributes:
            name (CharField): A string tnat represents the name, with 200 max length of characters.
            comment (TextField): A text field is a large text field to save the comments on the query.
            username (CharField): A string tnat represents the username, with 200 max length of characters.
            query (Foreign Key): References an instance of the model QueryModel, this is a many-to-one relationship,
                meaning each instance of this model can be associated with a single instance of QueryModel. 
                When the associated QueryModel instance is deleted, this instance will also be deleted (CASCADE)
    """
    name = models.CharField(max_length=200)
    comment = models.TextField()
    username = models.CharField(max_length=200)
    query = models.ForeignKey(QueryModel, on_delete=models.CASCADE)


class CommentModel(models.Model):
    """
        CommentModel

        Model with two fields: 'username' and 'comment'. 
        Each instance of this model represents a comment made by a user.

        Attributes:
            username (CharField): A string that represents the username, with 200 max length of characters.
            comment (TextField): A text field is a large text field to save the comments on the query.
            saved_query (Foreign Key): References an instance of the model SavedQuery, this is a many-to-one relationship,
                meaning each instance of this model can be associated with a single instance of SavedQuery. 
                When the associated SavedQuery instance is deleted, this instance will also be deleted (CASCADE)
    """
    username = models.CharField(max_length=200)
    comment = models.TextField()
    saved_query = models.ForeignKey(SavedQuery, on_delete=models.CASCADE)