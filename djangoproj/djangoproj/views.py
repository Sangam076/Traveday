from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def time(request):
    return request(time.now, 'index.html')
