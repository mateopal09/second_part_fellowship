"""
Views for user_stories_feature
"""
#Django rest-framework
from rest_framework import viewsets

#Django
from django.shortcuts import render
from django.http import HttpResponse

#Local Aplication
from user_stories_feature.queries import visual_query_builder
from user_stories_feature.models import QueryModel
from user_stories_feature.serializers import QueryModelSerializer



def view_visual_query_builder(request):
    """
        View for Visual Query Builder

        This view function calls the 'visual_query_builder' function and returns
        an HTTP response with the query results.
        
        Args:
            request (django.http.HTTpRequest): The request instance

        Returns:
            django.http.HTTpResponse: The HTTp response
    """

    results = visual_query_builder()
    result_str = ','.join([str(result[0]) for result in results])
    return HttpResponse("using django query builder " + result_str)    


class QueryModelViewSet(viewsets.ModelViewSet):
    """
    ViewSet for the QueryModel

    This ViewSet provides the CRUD operations for the QueryModel Instances.

    Attributes:
        - queryset (django.db.models.query.Queryset): The QueryModel queryset.
        - serializer_class (rest_framework.serializers.ModelSerializer). The serializer class.
    """
    queryset = QueryModel.objects.all()
    serializer_class = QueryModelSerializer
