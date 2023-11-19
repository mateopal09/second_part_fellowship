"""
Views for user_stories_feature
"""
#Python
import json
import pandas as pd

#Django rest-framework
from rest_framework import viewsets

#Django
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse

#Local Aplication
from user_stories_feature.queries import visual_query_builder
from user_stories_feature.models import QueryModel, SavedQuery
from user_stories_feature.serializers import QueryModelSerializer, SavedQuerySerializer

@csrf_exempt
def view_visual_query_builder(request):
    """
    View for Visual Query Builder

    This view function calls the 'visual_query_builder' function and returns
    an JSON response with the query results.

    Args:
        request (django.http.HttpRequest): The request instance.

    Returns:
        django.http.HttpResponse: The HTTP response. If the request method is 'POST',
        the response will be a JSON response containing the query results. If the request
        method is not 'POST', the response will be an HTTP 405 error.
    """
    if request.method == 'POST':
        data = json.loads(request.body)
        country_code = data.get('country_code')
        series_code = data.get('series_code')
        year = data.get('year')
        value = data.get('value')
        results = visual_query_builder(country_code,series_code, year, value) 
        df = pd.DataFrame({ 'Tables': ['country_summary', 'series_summary','international_education', 'country_series_definitions']})
        for row in results:
            i = df[df['Tables'] == row['table_name']].index[0]
            df.loc[i, 'country_code'] = row['country_count']
            df.loc[i, 'series_code'] = row['series_count']
            df.loc[i, 'year'] = row['year_count']
            df.loc[i, 'value'] = row['value_count']
        df = df.fillna(0) 
        result_list = df.to_dict('records')
        return JsonResponse(result_list, safe=False)
    else:
        return HttpResponse('This view only accepts POST requests', status=405)
        
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

class SavedQueryViewSet(viewsets.ModelViewSet):
    """
    ViewSet for the Saved Query
    """
    queryset = SavedQuery.objects.all()
    serializer_class = SavedQuerySerializer
