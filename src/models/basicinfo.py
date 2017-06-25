#!/usr/bin/env python
#encoding:utf-8

from src.models.basemodel import EntityModel
from src.ext import db
from src.ext import JsonEncodedDict


class Basicinfo(EntityModel):

    name = db.Column(db.String(120))
    credit_code = db.Column(db.String(120))
    register_addr = db.Column(db.String(120))
    register_capital = db.Column(db.String(120))
    representative = db.Column(db.String(120))
    establish_time = db.Column(db.String(120))
    business_scope = db.Column(db.Text)
    history = db.Column(JsonEncodedDict)
    user_id = db.Column(db.Integer)
    enterprise_id = db.Column(db.Integer)
