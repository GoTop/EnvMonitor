# coding=utf-8
from __future__ import unicode_literals

from selectable.base import ModelLookup
from selectable.registry import registry, LookupAlreadyRegistered
from ..models import Country

__author__ = 'GoTop'


class CountryLookup(ModelLookup):
    model = Country
    search_field = 'country__icontains'

try:
    registry.register(CountryLookup)
except LookupAlreadyRegistered:
    pass
