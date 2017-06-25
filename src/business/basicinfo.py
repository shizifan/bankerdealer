#!/usr/bin/env python
#encoding:utf-8

import json
from collections import OrderedDict
from src.models import *
from src.ext import db

class BasicinfoBusiness(object):

    @classmethod
    def save(cls, info_dict, enterprise_id):
        ret = cls.get_by_id(enterprise_id)
        if(ret):
            Basicinfo.query.filter_by(enterprise_id=enterprise_id).update(info_dict)
            db.session.commit()
        else:
            info_dict['enterprise_id'] = enterprise_id
            basicinfo = Basicinfo(**info_dict)
            db.session.add(basicinfo)
            db.session.commit()

    @classmethod
    def get_by_id(cls, enterprise_id):
        ret = Basicinfo.query.filter(Basicinfo.enterprise_id == enterprise_id).first()
        return ret


        