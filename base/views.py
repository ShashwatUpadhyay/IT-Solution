from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def service(request):
    return render(request, 'service.html')

def work(request):
    return render(request, 'work.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def career(request):
    return render(request, 'career.html')

def team(request):
    return render(request, 'team.html')