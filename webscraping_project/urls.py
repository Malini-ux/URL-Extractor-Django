# urls.py
from django.urls import path
from django.urls import path, include
from URLExtractor import views

urlpatterns = [
    path('', views.extract, name="extract"),
    path('__debug__/', include('debug_toolbar.urls')),
]
