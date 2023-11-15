"""
Urls for second_part_backend
"""
#Django rest-framework
from rest_framework import routers

#Django 
from django.contrib import admin
from django.urls import path, include

#Local Application
from user_stories_feature.views import QueryModelViewSet

#Create a router and register our viewsets with it.
router = routers.DefaultRouter()
router.register(r'QueryModel', QueryModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user-storie',include('user_stories_feature.urls')),
    path('', include(router.urls))
]
