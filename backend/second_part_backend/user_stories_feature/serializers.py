#Django rest-framework
from rest_framework import serializers

#Local Application
from user_stories_feature.models import QueryModel, SavedQuery, CommentModel

class QueryModelSerializer(serializers.ModelSerializer):
    """
        Query Model Serializer

        This will convert between complex types like QueryModel instances to Python native datatypes,
        which can then be easily rendered into JSON.

        Attributes:
            Meta.Model (QueryModel): The model class to which this serializer is tied.
            Meta.fields (list): The fields to be included in the serialized representation.
    
    """
    class Meta:
        model = QueryModel
        fields = ['id','country_code', 'series_code', 'year', 'value']

class CommentModelSerializer(serializers.ModelSerializer):
    """
        Comment Model Serializer

        This will be used for Comment Model and serialize the data

        Attributes:
            Meta.Model (SavedQuery): The model class to which this serializer is tied.
            Meta.fields (list): The fields to be included in the serialized representation.
    """
    class Meta:
        model =  CommentModel
        fields = ['id','username','comment','saved_query']


class SavedQuerySerializer(serializers.ModelSerializer):
    """
        Saved Query Serializer

        This will be used for Save the query that the user wants to save

        Attributes:
            Meta.Model (SavedQuery): The model class to which this serializer is tied.
            Meta.fields (list): The fields to be included in the serialized representation.
    """
    comments = CommentModelSerializer(many=True, read_only=True)
    class Meta:
        model = SavedQuery
        fields = ['id','name','comment', 'username', 'query', 'comments']

