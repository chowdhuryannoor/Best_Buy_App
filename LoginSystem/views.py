from django.shortcuts import render, redirect
from .forms import SignUpForm, EmployeeTypeForm
from django.contrib.auth import authenticate, login


# Create your views here.
def login(request):
    return render(request, 'LoginSystem/login.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        employee_type_form = EmployeeTypeForm(request.POST)

        if form.is_valid() and employee_type_form.is_valid():
            user = form.save()

            employee_type = employee_type_form.save(commit=False)
            employee_type.user = user
            employee_type.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            return redirect('login')
    else:
        form = SignUpForm()
        employee_type_form = EmployeeTypeForm(request.POST)
    context = {'form': form, 'employee_type_form': employee_type_form}
    return render(request, 'LoginSystem/signup.html', context)

