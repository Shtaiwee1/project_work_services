from django.http import HttpResponse
from django.shortcuts import render , redirect
from django.contrib import messages#import error messages for display
import bcrypt#importing bcrypt after installing using pip install bcrypt used for hashing,encoding and decoding
from .models import User , Worker#importing class from models.py

#root page
def index(request):
    context={"all_users":User.objects.all()}#passes the models attributes to the rendered page
    return render(request, "log_reg.html",context)
#registration information processing function and validation
def check(request):
    errors = User.objects.basic_validator_second(request.POST)
    print("hello")
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')#if there are any errors redirect to the root page no access for the success page
    else:
        user = User.objects.filter(email=request.POST['email'])#searches the database for the email input in the login form
        if user: #if there is a user with the input email = true
            logged_user = user[0]#save the user info ina varibale called logged_user
        #check if the password form thelogin form equals the hashed password in the database
        #converts the password from the form from string to byte and the hashed password in the database from hash to byte and compares the two of them 
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):#if the passwords match redirect to success page and save the logged in users info to display them in the success page
            request.session['userid'] = logged_user.id
            request.session['firstname'] = logged_user.first_name
            request.session['lastname'] = logged_user.last_name
            request.session['email'] = logged_user.email
            return redirect('/hassan')
    return redirect('/')#if passwords don't match redirect to root page to let the user try again
#function induced upon succeful registration
def successful_register(request , user_id):#gets the user_id as a parameter from the process registration page which sends user_id via url route
    registered_user=User.objects.get(id=user_id)#get the specific user for that specific id
    context={"new_user" : registered_user}#use a dictionary to save info values of the user in a key named new_user
    return render(request, "success_register.html", context)#access the info values of the user in successs page using context dictionary to access the key:new_user andthe values:rigestered user ##page rendered upon successful registration
#function induced upon succeful logging in
def successful_login(request):
    if "email" not in request.session:#prevents users to access success page before logging in
        return redirect('/')#if email is not saved in session redirect to root
    return render(request, "success_login.html")#page rendered upon successful logging in
#function induced when pressing the logout url anchor in the success page
def delete(request):#the logout button redirects to the (destroy) route in the urls.py and then induces this function in the views.py to clear logged user info
    request.session.clear()
    return redirect('/')
    # user_log_out=User.objects.get(id=user_id)
    # user_log_out.delete()
    # log_out_user=User.objects.get(id=user_id)

def join_form(request):
    return render(request, "join_workers.html")

<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 5a1e3cf3fb480dcb345b74abf13ed41903c4b0d9
def create_user(request):
    first_name=request.POST['first_name']
    last_name=request.POST['last_name']
    email=request.POST['email']
    password=request.POST['password']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    User.objects.create(first_name=first_name,
                        last_name=last_name,
                        email=email,
                        password=pw_hash)
    return HttpResponse('')
<<<<<<< HEAD
=======


def create_worker(request):
    phone_number=request.POST['phone_number']
    location=request.POST['location']
    career=request.POST['career']
    price=request.POST['price']
    desc=request.POST['desc']
    Worker.objects.create(phone_number=phone_number,
                        location=location,
                        career=career,
                        price=price,
                        desc=desc)
    return HttpResponse('')
>>>>>>> 5a1e3cf3fb480dcb345b74abf13ed41903c4b0d9


def create_worker(request):
    phone_number=request.POST['phone_number']
    location=request.POST['location']
    career=request.POST['career']
    price=request.POST['price']
    desc=request.POST['desc']
    Worker.objects.create(phone_number=phone_number,
                        location=location,
                        career=career,
                        price=price,
                        desc=desc)
    return HttpResponse('')

>>>>>>> 5a1e3cf3fb480dcb345b74abf13ed41903c4b0d9
