from django.forms import forms
from django.shortcuts import render, render_to_response

# Create your views here.
from .models import LocationForm


def save_form(request):
    if request.method == "POST":
        form = LocationForm(data=request.POST)
    else:
        form = LocationForm()
    return render_to_response('form.html', {'form': form})