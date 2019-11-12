from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('index.html')
    data = {
        "title": 'Мой проект',
    }
    return HttpResponse(template.render(data, request))
