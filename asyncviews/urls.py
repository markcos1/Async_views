from django.contrib import admin
from django.urls import path
from asyncviews.views import contador_tempo_view, api_ficticia_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contador/', contador_tempo_view, name='contador_tempo'),
    path('api-ficticia/', api_ficticia_view, name='api_ficticia'), 
]
