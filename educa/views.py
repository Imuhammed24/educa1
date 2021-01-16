from django.shortcuts import render


def index(request):
    context = {'html_title': 'WELCOME TO EDUCA',
               'page_name': 'home',}
    return render(request, 'index.html', context)
