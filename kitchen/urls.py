from django.urls import path, include
from kitchen.views import Index

urlpatterns = [
    path('', Index.as_view(), name='week-list'),
]