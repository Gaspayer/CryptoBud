from django.urls import path
from .views import SignUpView, LoginView, LogoutView

app_name = 'authentication'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView, name='login'),
    path('logout/', LogoutView, name='logout'),
]
