from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    # return HttpResponse("Hello database")
    return render(request, 'website/index.html')

def about(request):
    # return HttpResponse("Hello about")
    return  render(request, 'about.html')


def contact(request):
    # return HttpResponse("Hello contact")
    return render(request, "contact.html")
