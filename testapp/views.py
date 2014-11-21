from django.forms import forms
from django.shortcuts import render, render_to_response

# Create your views here.
from .form import LocationForm
from testapp.form import CountryForm


def smart_selects_form(request):
    if request.method == "POST":
        form = LocationForm(data=request.POST)
    else:
        form = LocationForm()
    return render_to_response('smart_selects_form.html', {'form': form})

def selectable_form(request):
    if request.method == "POST":
        form = CountryForm(data=request.POST)
    else:
        form = CountryForm()
    return render_to_response('selectable_form.html', {'form': form})