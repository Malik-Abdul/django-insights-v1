from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("posts:list") # name of the app: name of the url reference
    else:
            form = UserCreationForm()
    return render(request, 'users/register.html', {"form": form})
