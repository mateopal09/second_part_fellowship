from django.shortcuts import render
from django.http import HttpResponse
from .queries import visual_query_builder

# Create your views here.

def view_visual_query_builder(request):
    results = visual_query_builder()
    result_str = ','.join([str(result[0]) for result in results])
    return HttpResponse("using django query builder " + result_str)    
