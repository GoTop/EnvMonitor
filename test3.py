# coding=utf-8
#from __future__ import unicode_literals

inner_dict = {'a': 'a'}

outer_dict = {'1': {}, '2': {}}
list = ['1', '2']
outer_dict = {}.fromkeys(list, {})

outer_dict['1'].update(inner_dict)

print(outer_dict)








