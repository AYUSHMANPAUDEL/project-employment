from django.shortcuts import render , HttpResponse,redirect
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to the home page after successful login
        else:
            # Handle invalid login credentials (you may want to show an error message)
            pass

    return render(request, 'login.html')
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