"""
URLs for user_stories_feature
"""

#django
from django.urls import  path

#Local Application
from user_stories_feature import views

#Define the application routes
urlpatterns = [
    path('', views.view_visual_query_builder, name='view_query'),   
]
