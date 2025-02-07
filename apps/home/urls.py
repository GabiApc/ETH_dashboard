
from django.urls import path, re_path
from requests import patch
from apps.home import views


urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('voluntari', views.all_volunteers, name="vol-list"),
    path('evenimente', views.all_events, name="event-list"),
    path('add_vol', views.add_vol, name='add_vol'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),
        
]
