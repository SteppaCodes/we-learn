from django.shortcuts import render, redirect
from django.views import View
from . forms import RegisterForm,  LoginForm
from django.contrib.auth import authenticate, login, logout

class RegisterView(View):
    def get(self,request):
        form = RegisterForm()

        context = {'form':form}
        return render(request, 'accounts/register.html', context)
    
    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        
        context = {'form':form}
        return render(request, 'accounts/register.html', context)

class LoginView(View):
    def get(self,  request):
        form = LoginForm()

        context = {"form":form}
        return render(request, 'accounts/login.html', context)
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = authenticate(request, username=email, password=password)
            if not user:
                print('Not a user')
            else:
                login(request, user)
                return redirect('home')
                
        context = {"form":form}
        return render(request, 'accounts/login.html', context)

# class LogoutView(View):
#     def get(self, request):
#         user = request.user
#         logout(user) 
#         return redirect('home')       