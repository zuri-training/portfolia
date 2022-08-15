from django.shortcuts import render, redirect
from django.contrib import messages
from validate_email import validate_email
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout

# Create your views here.

User = get_user_model()

def register_view(request):

    if request.method == 'POST':
        data = request.POST
        context={
        'has_error':False
        }
        email = request.POST.get('email', None)
        first_name = request.POST.get('first_name', None)
        last_name = request.POST.get('last_name', None)
        password = request.POST.get('password', None)
        password2 = request.POST.get('password2', None)

        if len(password) < 6:
            messages.add_message(request, messages.ERROR, 'Passwords should be at least 6 characters long')
            context['has_error'] = True

        if password!=password2:
            messages.add_message(request, messages.ERROR, 'Passwords do not match')
            context['has_error'] = True

        if not validate_email(email):
            messages.add_message(request, messages.ERROR, 'please provide a valid email')
            context['has_error'] = True


        try:
            if User.objects.get(email=email).exists():
                messages.add_message(request, messages.ERROR, 'Email is taken')
                context['has_error'] = True

        except Exception as identifier:
            pass 

        # if User.objects.filter(email=email).exists():
        #     messages.add_message(request, messages.ERROR, 'Email is taken')
        #     context['has_error'] = True

        if context['has_error']:
            return render(request, 'accounts/signup.html', context, status=400)
        
        user = User.objects.create_user(email=email, password=None)
        user.set_password(password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        messages.add_message(request, messages.SUCCESS, 'Account created successfully')

        return redirect('dashboard')
    return render(request, 'accounts/signup.html')

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')


    if request.method =='POST':
        context={
        'has_error':False
        }
        email = request.POST.get('email').lower()
        password = request.POST.get('password')
        if email == '':
            messages.add_message(request, messages.ERROR, 'email is required')
            context['has_error'] = True
        
        if password == '':
            messages.add_message(request, messages.ERROR, 'password is required')
            context['has_error'] = True
        
        user = authenticate(request, email=email, password=password)

        if not user and not context['has_error']:
            messages.add_message(request, messages.ERROR, 'invalid login credentials')
            context['has_error'] = True

        if context['has_error']:
            return render(request, 'accounts/login.html', status=401, context=context)
        
        login(request, user)
        return redirect('dashboard')
    return render(request, 'accounts/login.html')



def logout_view(request):
    logout(request)
    return redirect('login')
        

