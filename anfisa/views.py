from django.http import HttpResponse
from django.shortcuts import render
from . import anfisa


def about(request):
    return render(request, 'templates/about.html')


def index(request):
    html = ''
    if request.method == 'POST':
        query = request.POST['query']
        answer = anfisa.process_query(query)
        html = f'<mark>{answer}</mark>'
    context = {
        'response': html,
        'where': request.path
    }

    return render(request, 'templates/index.html', context)
