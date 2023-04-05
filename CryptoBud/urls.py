"""CryptoBud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import messages

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Home.urls')),
    path('Admin/', include('Admin.urls')),
    path('Analytics/', include('Analytics.urls')),
    path('Authentication/', include('Authentication.urls')),
    path('Creator/', include('Creator.urls')),
    path('Crowdfunding/', include('Crowdfunding.urls')),
    path('Messaging/', include('Messaging.urls')),
    #path('Notification/', include('Notification.urls')),
    #path('Transaction/', include('Transaction.urls')),
    # ... include other app URLs here ...
]

# Serve static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


'''
# Handle messages
urlpatterns += [
    path('messages/', include('django.contrib.messages.urls')),
]
'''
