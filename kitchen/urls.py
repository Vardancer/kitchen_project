from django.urls import path
from kitchen.views import Index, WeekForm, WeekDetailView, OrderView

urlpatterns = [
    path('<int:pk>/', WeekDetailView.as_view(), name='week-detail'),
    path('orders/<int:pk>', OrderView.as_view(), name='order-detail'),
    path('order/<int:pk>/', WeekForm.as_view(), name='week-form'),
    path('', Index.as_view(), name='week-list'),
]