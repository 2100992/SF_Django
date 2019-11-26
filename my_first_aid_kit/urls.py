from django.urls import path
from . import views

app_name = 'my_first_aid_kit'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    
]