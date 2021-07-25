from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from .models import *
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.
def Login(response):
    if response.method == 'POST' :
        email = response.form.get('email')
        password = response.form.get('password')

        user = User.query.filter_by(email= email).first()
        if user:
            if check_password(user.password, password):
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                return render("login.html")
        else:
            return render("login.html")

    return render("login.html")
    return render( response, "login.html")



def Signup(response):
    if response.method == 'POST':
        email = response.form.get('email')
        first_name = response.form.get('firstName')
        username = response.form.get('username')
        password1 = response.form.get('password1')
        password2 = response.form.get('password2')
        profile_pic= response.files.get("profilepic")
        

        

        user = Users.objects.get(email= email).first()
        if user:
            return render("signup.html")

        if len(email)< 4:
            pass
        elif len(first_name)< 2:
            pass
        elif password1 != password2:
            pass
        elif len(password1) <7:
            pass
        else:
            register = Users(name= first_name, email= email, password= make_password(password1), university= university, degree= degree, course= course)


    else:
        return render("signup.html")