from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def contacts(request):
    return render(request,'main/contacts.html')  

def about(request):
    return render(request,'main/about_us.html' )

def navig(request):
    return render(request, 'main/navigation.html')