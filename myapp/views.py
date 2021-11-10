from django.shortcuts import render


def overview(response):
    return render(response, 'myapp/overview.html')


def about(response):
    return render(response, 'myapp/about.html')
