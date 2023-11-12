from django.urls import  path
from . import views


urlpatterns = [
    
    path('/', views.view_visual_query_builder, name='view_query')
    
]
