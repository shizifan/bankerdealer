#!/usr/bin/env python
#encoding:utf-8

from config.settings import YML_JSON
from flask import request
import json

def parse_baseinfo(form):
    info_dict = {}
    history_dict = {}
    for key in form:
        val = form[key]
        pairs = key.split('-')
        if(len(pairs)==1):
            info_dict[key] = val
        else:
            if(pairs[1]=='history'):
                if(history_dict).has_key(pairs[2]):
                    history_dict[pairs[2]][pairs[0]] = val
                else:
                    history_dict[pairs[2]] = {}
                    history_dict[pairs[2]][pairs[0]] = val
    info_dict['history'] = history_dict
    return info_dict

def parse_form(name):
    form_json = YML_JSON.get(name)
    returnvalue = form_json.get('returnvalue')
    return dict(zip(returnvalue, [request.form.get(x) for x in returnvalue]))

def parse_history(form):
    history_dict = {}
    times = len(form) / 4
    for time in xrange(times+1):
        if time != 0:
            history_dict[str(time)] = {k.split('-')[0]: v  for k,v in form.iteritems() if int(k.split('-')[1]) == time}
    return history_dict