"""edit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from schedule.views import (
    FloorViewSet,
    ExhibitorViewSet,
    PointViewSet,
    InstallationViewSet,
    EventViewSet,
    SpeakerViewSet,
)

router = DefaultRouter()
router.register(r'schedule/floors', FloorViewSet)
router.register(r'schedule/exhibitors', ExhibitorViewSet)
router.register(r'schedule/points', PointViewSet)
router.register(r'schedule/installations', InstallationViewSet)
router.register(r'schedule/events', EventViewSet)
router.register(r'schedule/speakers', EventViewSet)

urlpatterns = [
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^admin/', admin.site.urls),
    url(r'^api/(?P<version>(v1))/', include(router.urls)),
    url(r'ckeditor/', include('ckeditor_uploader.urls')),
]
