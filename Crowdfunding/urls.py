from django.urls import path
from .views import create_fundraiser, contribute, fundraiser_detail, my_fundraisers

app_name="crowdfunding"

urlpatterns = [
    path('<int:fundraiser_id>/', fundraiser_detail, name='fundraiser_detail'),
    path('my_fundraisers/', my_fundraisers, name='my_fundraisers'),
    #path('fundraisers/', view_campagins, name='view_fundraisers'),
    path('create/', create_fundraiser, name='create_fundraiser'),
]
