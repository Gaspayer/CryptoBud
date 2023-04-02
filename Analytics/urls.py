from django.urls import path
from .views import DashboardView, EventDetailView

app_name = 'analytics'

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('events/<int:pk>/', EventDetailView.as_view(), name='event_detail'),
]
