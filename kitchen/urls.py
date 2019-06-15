from django.urls import path, include
from kitchen.views import Index, WeekForm, WeekDetailView

urlpatterns = [
    path('<int:pk>/', WeekDetailView.as_view(), name='week-detail'),
    path('<int:pk>/', WeekForm.as_view(), name='week-form'),
    path('', Index.as_view(), name='week-list'),
]