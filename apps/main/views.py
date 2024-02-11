from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def magazine(request):
    return render(request,'main/magaz.html')  