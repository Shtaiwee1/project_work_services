from django.shortcuts import render , redirect
from django.contrib import messages#import error messages for display
import bcrypt#importing bcrypt after installing using pip install bcrypt used for hashing,encoding and decoding
from login_registration_app.models import User , Worker#importing class from models.py

#root page
def index(request):
    context={"all_users":User.objects.all()}#passes the models attributes to the rendered page
    return render(request, "log_reg.html",context)
