#Django rest-framework
from rest_framework import serializers

#Local Application
from user_stories_feature.models import QueryModel

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