"""
Views for user_stories_feature
"""
# Python
import json
import pandas as pd

# Django rest-framework
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

# Django
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse

# Local Aplication
from user_stories_feature.queries import visual_query_builder
from user_stories_feature.models import QueryModel, SavedQuery, CommentModel
from user_stories_feature.serializers import QueryModelSerializer, SavedQuerySerializer, CommentModelSerializer


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
            # If the request method is POST, parse the request body as JSON
        data = json.loads(request.body)
        
        # Extract the country code, series code, year, and value from the data
        country_code = data.get('country_code')
        series_code = data.get('series_code')
        year = data.get('year')
        value = data.get('value')
        
        # Call the visual_query_builder function with the extracted data
        results = visual_query_builder(country_code, series_code, year, value)
        
        # Create a DataFrame with the table names
        df = pd.DataFrame({'Tables': ['country_summary', 'series_summary',
                        'international_education', 'country_series_definitions']})
        
        # Loop through the results and update the DataFrame
        for row in results:
            i = df[df['Tables'] == row['table_name']].index[0]
            df.loc[i, 'country_code'] = row['country_count']
            df.loc[i, 'series_code'] = row['series_count']
            df.loc[i, 'year'] = row['year_count']
            df.loc[i, 'value'] = row['value_count']
        
        # Fill any missing values in the DataFrame with 0
        df = df.fillna(0)
        
        # Convert the DataFrame to a list of dictionaries
        result_list = df.to_dict('records')
        
        # Return a JSON response with the result list
        return JsonResponse(result_list, safe=False)
    else:
        # If the request method is not POST, return an HTTP 405 Method Not Allowed response
        return HttpResponse('This view only accepts POST requests', status=405)


def view_show_saved_queries(request):
    # Fetch all SavedQuery objects from the database
    saved_queries = SavedQuery.objects.all()
    
    # Initialize an empty list to store the queries
    queries_list = []
    
    # Loop through each SavedQuery object
    for query in saved_queries:
        # Create a dictionary with the query information
        query_info = {
            'id': query.id,
            'name': query.name,
            'comment': query.comment,
            'username': query.username,
            'country_code': query.query.country_code,
            'series_code': query.query.series_code,
            'year': query.query.year,
            'value': query.query.value,
            # Use a list comprehension to create a list of comments for the query
            'comments': [{'username': comment.username, 'comment': comment.comment} for comment in query.comments.all()]
        }
        
        # Append the query information to the list of queries
        queries_list.append(query_info)
    
    # Return a JSON response with the list of queries
    # The safe parameter is set to False because we're passing a non-dict object
    return JsonResponse(queries_list, safe=False)


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

    This ViewSet provides the CRUD operations for the SavedQuery Instances.

    Attributes:
        - queryset (django.db.models.query.SavedQuery): The SavedQuery queryset.
        - serializer_class (rest_framework.serializers.ModelSerializer). The serializer class.
    """
    queryset = SavedQuery.objects.all()
    serializer_class = SavedQuerySerializer

    @action(detail=True, methods=['get', 'post'])
    def create_comment(self, request, pk=None):
        # Get the SavedQuery object
        saved_query = self.get_object()
        
        # Check if the request method is POST
        if request.method == 'POST':
            # Create a new CommentModel object with the data from the request
            comment = CommentModel.objects.create(
                username=request.data['username'],
                comment=request.data['comment'],
                saved_query=saved_query
            )
            
        # Serialize the SavedQuery object
        saved_query_serializer = SavedQuerySerializer(saved_query)
        
        # Return a response with the serialized data
        return Response(saved_query_serializer.data)


class CommentModelViewSet(viewsets.ModelViewSet):
    """
    ViewSet for the CommentModel

    This ViewSet provides the CRUD operations for the CommentModel Instances.

    Attributes:
        - queryset (django.db.models.query.CommentModel): The CommentModel queryset.
        - serializer_class (rest_framework.serializers.ModelSerializer). The serializer class.
    """
    queryset = CommentModel.objects.all()
    serializer_class = CommentModelSerializer
