from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, CreateView
from django.views import View
from django.urls import reverse_lazy

from .models import Medicament, Item
from .forms import MedicamentForm


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'my_first_aid_kit/index.html'


class Medicaments(View):
    template_name = 'my_first_aid_kit/medicaments.html'
    model = Medicament

    def get(self, request):
        # success_url = reverse_lazy('my_first_aid_kit:medicaments_list_url')
        context = {}
        medicaments = []
        if request.GET.get('med'):
            context['med'] = request.GET['med']
            medicaments = Medicament.objects.filter(slug=context['med']).all()
        else:
            medicaments = Medicament.objects.all()
        context['medicaments'] = medicaments
        return render(request, self.template_name, context=context)


'''
class Medicaments(ListView):
    model = Medicament
    template_name = 'my_first_aid_kit/medicaments.html'
    success_url = reverse_lazy('my_first_aid_kit:medicaments_list_url')
    context_object_name = 'medicaments'
'''

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


class Testing(View):
    template_name = 'my_first_aid_kit/testing.html'

    def get(self, request, **kwargs):
        print()
        print('ruquest')
        print(request)
        print()
        print('ruquest')
        print(request.GET['med'])
        print()
        print('kwargs')
        print(kwargs)
        print()
        context = {
            'request': request,
            'kwargs': kwargs,
        }
        return render(request, self.template_name, context=context)
