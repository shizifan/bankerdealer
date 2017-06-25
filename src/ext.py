#!/usr/bin/env python
#encoding:utf-8

from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from sqlalchemy.ext import mutable
import json

db      = SQLAlchemy()
admin   = Admin()

class JsonEncodedDict(db.TypeDecorator):
    """Enables JSON storage by encoding and decoding on the fly."""
    impl = db.Text

    def process_bind_param(self, value, dialect):
        if value is None:
            return '{}'
        else:
            return json.dumps(value)

    def process_result_value(self, value, dialect):
        if value is None:
            return {}
        else:
            return json.loads(value)

mutable.MutableDict.associate_with(JsonEncodedDict)