from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .forms import CreateUserForm , UpdateProfileForm ,UpdateUserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required




# Create your views here.

def registrar_usuario(request):
    form = CreateUserForm()
    if request.user.is_authenticated:
        return redirect('estante')
    else:
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')

    context = {'form':form}
    return render(request, 'register_user.html', context)

@login_required
def profile(request):
    user = request.user
    if request.method == "POST":
        u_form = UpdateUserForm(request.POST,request.FILES,instance=user)
        p_form = UpdateProfileForm(request.POST,request.FILES,instance=user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Sua conta foi atualizada com sucesso')
            return redirect('profile')
    else:
        u_form = UpdateUserForm(instance=user)
        p_form = UpdateProfileForm(instance=user.profile)

    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }


    return render(request, "profile_user.html", context)

def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('estante')
        else:
            messages.info(request,'Username ou password esta incorreta.')
            return render(request, 'login_user.html', {})

    context = {}
    return render (request,'login_user.html',context)


def logoutuser(request):
    logout(request)
    return redirect('estante')






