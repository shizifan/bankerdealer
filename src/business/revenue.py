#!/usr/bin/env python
#encoding:utf-8

import json
from collections import OrderedDict
from src.models import *
from src.ext import db


class RevenueBusiness(object):

    @classmethod
    def save(cls, info_dict, user_id):
        ret = cls._get_by_id(user_id)
        if ret is None:
            revenue = Revenue(
                content = json.dumps(info_dict),
                user_id = user_id
            )
            db.session.add(revenue)
            db.session.commit()
            return 0
        ret.content = json.dumps(info_dict)
        db.session.add(ret)
        db.session.commit()
        return 0

    @classmethod
    def _get_by_id(cls, enterprise_id):
        return Revenue.query.filter(Revenue.user_id == enterprise_id).first()

    @classmethod
    def get_by_id(cls, enterprise_id):
        ret = Revenue.query.filter(Revenue.user_id == enterprise_id).first()
        if ret:
            ori_history = json.loads(ret.content)
            pipe_history = OrderedDict(sorted(ori_history.items(), key=lambda t: t[0]))
            return [v for k,v in pipe_history.iteritems()]
        return None


        