from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, CreateView
from django.views import View
from django.urls import reverse_lazy

from .models import *
from .forms import MedicamentForm


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'my_first_aid_kit/index.html'


class Medicaments(ListView):
    model = Medicament
    template_name = 'my_first_aid_kit/medicaments.html'
    success_url = reverse_lazy('my_first_aid_kit:medicaments_list_url')
    context_object_name = 'medicaments'
    
    # form_class = MedicamentForm

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     medicaments = Medicament.objects.all()
    #     # context['now'] = timezone.now()
    #     return context


class MyKit(ListView):
    model = Item
    content_type = ''
    context_object_name = 'items'
    template_name = 'my_first_aid_kit/items.html'
