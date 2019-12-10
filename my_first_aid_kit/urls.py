from django.urls import path
from . import views

app_name = 'my_first_aid_kit'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='my_first_aid_kit_url'),
    path('medicaments/', views.Medicaments.as_view(), name='medicaments_list_url'),
    path('mykit/', views.MyKit.as_view(), name='my_kit_url'),
    path('testing/', views.Testing.as_view(), name='testing_url')
    
]