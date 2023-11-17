"""
Views for user_stories_feature
"""
#Python
import json

#Django rest-framework
from rest_framework import viewsets

#Django
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse

#Local Aplication
from user_stories_feature.queries import visual_query_builder
from user_stories_feature.models import QueryModel
from user_stories_feature.serializers import QueryModelSerializer


@csrf_exempt
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
    if request.method == 'POST':
        data = json.loads(request.body)
        country_code = data.get('country_code')
        series_code = data.get('series_code')
        year = data.get('year')
        value = data.get('value')
        results = visual_query_builder(country_code,series_code, year, value)
        print(f'Results: {results}')
        result_list = [{'country_count': row.country_count,
                        'series_count': row.series_count,
                        'year_count': row.year_count, 
                        'value_count': row.value_count} for row in results]
        
        print(f'Sending response: {result_list}')
        response = JsonResponse(result_list, safe=False)
        print(f'Response of JSON: {response.getvalue().decode("utf-8")}')
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
