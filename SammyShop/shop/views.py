from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm
# Create your views here.

#when the user_login view is called with a GET method.
#we create a new login  form with form = LoginForm() to display it in the template


def home(request):
    return render(request, 'shop/product/homepage.html')

def error(request):
    return render(request, 'shop/error.html')

def user_login(request):
    #when user submit form with the POST method, we will perform the following actions:
    if request.method == "POST":
        #initialization shows the submit data form with form = LoginForm(request.POST)
        form = LoginForm(request.POST)
        #check if form is valid. if the data is not valid we will display a form error in the template
        if form.is_valid():
            #if you submit the valid data, we will authenticate the user with the data in the database using the authenticate() method
            #this method takes the Username and Password and returns a User object if  the user succesfully authenticates, otherwise returns None
            #if the user is not authenticated, we will return HttpResponse displaying a message
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                #if the user succesfully authenticates, we will check if the user is active with the is_active attribute.
                #this is an attibute of User model in Django
                #if  the user is not active, we will return HttpResponse displaying information
                if user.is_active:
                    #if the user is active, we will allow the user to login to the website.
                    #we will set up the user in the session by calling login() method and returning the login message succesfully
                    login(request, user)
                    return redirect('shop:homepage')
                else:
                    return HttpResponse('Disable account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'shop/login.html', {'form':form})
