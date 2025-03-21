"""anwesha URL Configuration

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
import imp
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from user.urls import user_urls
from event.urls import event_urls
from participant.urls import participant_urls
from sponsor.urls import sponsor_urls
from campus_ambassador.urls import campus_ambassador_urls

# from rest_framework.routers import DefaultRouter
from user import views
# from user.views import UserViewSet




urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include(user_urls)),
    path('event/', include(event_urls)),
    path('participant/', include(participant_urls)),
    path('sponsors/', include(sponsor_urls)),
    path('campasambassador/', include(campus_ambassador_urls)),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
