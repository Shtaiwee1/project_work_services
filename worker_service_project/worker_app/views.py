from django.shortcuts import render , redirect
from django.contrib import messages#import error messages for display
import bcrypt#importing bcrypt after installing using pip install bcrypt used for hashing,encoding and decoding
from login_registration_app.models import User , Worker , Service#importing class from models.py

#root page
def index(request):
    context={"all_users":User.objects.all()}#passes the models attributes to the rendered page
    return render(request, "log_reg.html",context)

def hassan(request):
    return render(request,'Main.html')

# method to render/show the edit page :
def show(request):
    return render(request , 'edit.html')

# update profile 
def edit(request):
    print("hello")
    this_user = User.objects.get(id = request.session['userid'])
    this_user.first_name = request.POST['updated_first-name']
    this_user.last_name = request.POST['updated_last-name']
    this_user.email = request.POST['updated_email']
    this_user.save()
    return redirect('/hassan')

# method to render join our worker page which contains the registration form for workers
def join(request):
    return render(request , 'join_workers.html')

# create the registration form for workers and redirect the results to home page :
def register_worker(request):
    Worker.objects.create(
        phone_number = request.POST['phone_number'],
        price = request.POST['price'],
        location = request.POST['location'],
        career = request.POST['career'],
        desc = request.POST['description'],
        user_has_worker = User.objects.get(id=request.session['userid'])
    )
    return redirect('/hassan')

#render the page that shows the worker details :
def details(request):
    # this_user = User.objects.get(id = request.session['userid'])
    # context={
    #     'this_user' : this_user,
    #     'all_workers' : Worker.objects.all()
    # }
    return render(request , 'workers.html')