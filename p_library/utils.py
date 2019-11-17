from django.shortcuts import render
from django.shortcuts import get_object_or_404, get_list_or_404

from p_library.models import *


class ObjectDetailMixin:
    model = None
    template = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        obj_data = {
            self.model.__name__.lower(): obj
        }
        return render(request, self.template, context=obj_data)


# Миксин для вывода во вьюху списка значений
class ObjectsListMixin:
    model = None
    template = None
    title = None

    def get(self, request):
        obj = get_list_or_404(self.model)
        # obj = self.model.objects.all()
        obj_data = {
            self.model.__name__.lower(): obj,
            'title': self.title
        }
        return render(request, self.template, context=obj_data)

# Миксин для вывода во вьюху фильтрованного списка значений
# class ObjectsFiltredListMixin:
#     model = None
#     template = None
#     title = None
#     column = None
#     data = None

#     def get(self, request):
#         if self.column is None:
#             obj = self.model.objects.all()
#         else:
#             obj = self.model.objects.filter(**{self.column: self.data})
#         obj_data = {
#             self.model.__name__.lower(): obj,
#             'title': self.title

#         }
#         return render(request, self.template, context=obj_data)
