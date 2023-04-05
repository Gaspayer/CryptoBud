from django.urls import path
from .views import create_campaign, contribute

app_name="crowdfunding"

urlpatterns = [
    #path('<int:pk>/', view_campagin, name='view_campaign'),
    #path('campaigns/', view_campagins, name='view_campaigns'),
    path('create/', create_campaign, name='create_campaign'),
]
