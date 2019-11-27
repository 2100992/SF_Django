from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from .models import *


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'my_first_aid_kit/index.html'


class Medicaments(ListView):
    model = Medicament
    context_object_name = 'medicaments'
    template_name = 'my_first_aid_kit/medicaments.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # context['now'] = timezone.now()
    #     return context

class MyKit(ListView):
    model = Item
    content_type = ''
    context_object_name = 'items'
    template_name = 'my_first_aid_kit/items.html'