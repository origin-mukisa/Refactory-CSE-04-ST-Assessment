from django.shortcuts import render, redirect
from .forms import PlanePassengerForm
from .models import *
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = PlanePassengerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form has been submitted successfully')
            return redirect('/')
        else:
            messages.error(request, 'Form is not valid')
    else:
        form = PlanePassengerForm()
    return render(request, 'index.html', {'form': form})



