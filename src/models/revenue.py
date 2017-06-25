#!/usr/bin/env python
#encoding:utf-8

from src.models.basemodel import EntityModel
from src.ext import db


class Revenue(EntityModel):

    content = db.Column(db.Text)
    user_id = db.Column(db.Integer)
    company_id = db.Column(db.Integer)