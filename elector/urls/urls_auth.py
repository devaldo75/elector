

from django.urls import path
from elector.views.views_auth import dashboard, login_view

app_name = 'elector'

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('login/', login_view, name='login_view')
]