from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth


# Create your views here.

def registration(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # if password == password2:
        #     if User.objects.filter(username=username).exist():
        #         print('User name is already taken')
        #     elif User.objects.filter(email=email).exist():
        #         print('email already exists')
        #     else:
        register = User.objects.create_user(username=username, email=email, password=password)
        register.save()
            # print('User Created!!')

        # else:
        #     print('password did not match')

        return redirect("../")

    else:
        return render(request, 'register.html')
