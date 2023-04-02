from django.urls import path
from .views import CreatorProfileView, CreateCreatorProfileView

app_name = 'creator'

urlpatterns = [
    path('<int:pk>/', CreatorProfileView, name='creator_profile'),
    path('create/', CreateCreatorProfileView.as_view(), name='create_creator_profile'),
]
