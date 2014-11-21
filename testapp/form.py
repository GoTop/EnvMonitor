# coding=utf-8
from __future__ import unicode_literals
from django import forms
from django.forms import ModelForm
import selectable.forms as selectable
from selectable.forms import AutoCompleteWidget

from testapp.function.lookups import CountryLookup
from testapp.models import Location

__author__ = 'GoTop'


class LocationForm(ModelForm):
    class Meta:
        model = Location


class CountryForm(forms.Form):
    autocomplete = forms.CharField(
        label='Type the name of a country (AutoCompleteWidget)',
        widget=AutoCompleteWidget(CountryLookup),
        required=False,
    )
