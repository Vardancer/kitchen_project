from django.urls import path
from kitchen.views import Index, OrderFormView, WeekDetailView, OrderListView, OrderUpdateView

urlpatterns = [
    path('<int:pk>/', WeekDetailView.as_view(), name='week-detail'),
    path('orders/', OrderListView.as_view(), name='orders-list'),
    path('order/<int:pk>/', OrderUpdateView.as_view(), name='order-edit'),
    path('buy/<int:pk>/', OrderFormView.as_view(), name='week-form'),
    path('', Index.as_view(), name='week-list'),
]