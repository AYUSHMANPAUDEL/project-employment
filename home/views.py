from django.shortcuts import render , HttpResponse

# Create your views here.
def index (requests):
    # context={
    #     'variable' :"this is variable attached to the text"

    # }
    return render(requests, 'index.html')
def login (requests):
   return render(requests, 'login.html')
def work (requests):
    return render(requests, 'work.html')
def home (requests):
    return render(requests, 'index.html')
def request (requests):
    return render(requests, 'request.html')
def forget (requests):
    return render(requests, 'forget.html')