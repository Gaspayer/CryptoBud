from django.urls import path
from .views import DashboardView, LogEntryListView, LogEntryDetailView, ContentTypeListView, ContentTypeDetailView, PermissionListView

app_name = 'admin_app'

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('log-entries/', LogEntryListView.as_view(), name='log_entry_list'),
    path('log-entries/<int:pk>/', LogEntryDetailView.as_view(), name='log_entry_detail'),
    path('content-types/', ContentTypeListView.as_view(), name='content_type_list'),
    path('content-types/<int:pk>/', ContentTypeDetailView.as_view(), name='content_type_detail'),
    path('permissions/', PermissionListView.as_view(), name='permission_list'),
]
