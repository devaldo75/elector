from os import path

from django.urls import include

from elector.urls.urls_auth import urlpatterns as auth_patterns


urlpatterns = [
    path('elector/', include('elector.urls'))
]