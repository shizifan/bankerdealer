#!/usr/bin/env python
#encoding:utf-8

from src.models import *
from src.ext import db


class FinanceBusiness(object):

    @classmethod
    def save(cls, info):
        ret = cls.get_by_id(info.get('user_id'))
        if ret is None:
            finance = Finance(**info)
            db.session.add(finance)
            db.session.commit()
            return 0
        for k,v in info.iteritems():
            setattr(ret, k, v)
        db.session.add(ret)
        db.session.commit()
        return 0


    @classmethod
    def get_by_id(cls, id):
        return Operate.query.filter(Finance.user_id == id).first()