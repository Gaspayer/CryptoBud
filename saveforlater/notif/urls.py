'''
from django.urls import path
from .views import (
    NotificationListView,
    NotificationDetailView,
)

urlpatterns = [
    path('notifications/', NotificationListView.as_view(), name='notification_list'),
    path('notifications/<int:pk>/', NotificationDetailView.as_view(), name='notification_detail'),
]
'''
