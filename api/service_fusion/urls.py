"""service_fusion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from rest_framework import routers
from addresses.views import *

router = routers.DefaultRouter()

router.register(r'api/addresses', AddressViewSet)
router.register(r'api/phone_numbers', PhoneNumberViewSet)
router.register(r'api/emails', EmailViewSet)
router.register(r'api/people', PeopleViewSet, base_name='person')


urlpatterns = [
    url(r'^', include(router.urls), ),
    url(r'^api/add_person/', CreatePersonView.as_view()),
    url(r'^api/admin/', admin.site.urls),
    url(r'^api/api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]