from django.shortcuts import render,redirect
from item.models import Category, Item
from .forms import SignupForm
from django.contrib.auth import logout

def home(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    return render(request, 'marketApp/home.html', {
                  'categories' : categories,
                  'items' : items,})

def index(request):
    return render(request, 'marketApp/index.html')



def contact(request):
    return render(request, 'marketApp/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:   
        form = SignupForm()

    return render(request, 'marketApp/signup.html', {
        'form': form
    })

def logout_user(request):
    logout(request)
    return redirect('/')