# coding=utf-8
from __future__ import unicode_literals

__author__ = 'GoTop'


from datetime import date

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

class DistrictListFilter(admin.SimpleListFilter):
    # https://docs.djangoproject.com/en/1.6/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_filter

    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _('县区')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'district'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
            ('右江区', _('右江区')),
            ('田阳', _('田阳')),
            ('田东', _('田东')),
            ('平果', _('平果')),
            ('靖西', _('靖西')),
            ('德保', _('德保')),
            ('那坡', _('那坡')),
            ('凌云', _('凌云')),
            ('乐业', _('乐业')),
            ('田林', _('田林')),
            ('隆林', _('隆林')),
            ('西林', _('西林')),

        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        # Compare the requested value (either '80s' or '90s')
        # to decide how to filter the queryset.

        # https://docs.djangoproject.com/en/dev/topics/db/queries/#lookups-that-span-relationships
        if self.value() == '右江区':
            return queryset.filter(company__district='右江区')
        if self.value() == '田阳':
            return queryset.filter(company__district='田阳')
        if self.value() == '田东':
            return queryset.filter(company__district='田东')
        if self.value() == '平果':
            return queryset.filter(company__district='平果')
        if self.value() == '靖西':
            return queryset.filter(company__district='靖西')
        if self.value() == '德保':
            return queryset.filter(company__district='德保')
        if self.value() == '那坡':
            return queryset.filter(company__district='那坡')
        if self.value() == '凌云':
            return queryset.filter(company__district='凌云')
        if self.value() == '乐业':
            return queryset.filter(company__district='乐业')
        if self.value() == '田林':
            return queryset.filter(company__district='田林')
        if self.value() == '隆林':
            return queryset.filter(company__district='隆林')
        if self.value() == '西林':
            return queryset.filter(company__district='西林')



