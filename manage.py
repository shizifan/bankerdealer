#!/usr/bin/env python
#encoding:utf-8

from flask import current_app
from flask_script import Manager, Server, Shell

from src import create_app
from src.models import *
from src.ext import db
import json

manager = Manager(create_app)
server = Server(host='0.0.0.0',port=5001,use_debugger=True)

def make_shell_context():
    return dict(
            app     = current_app,
            )

manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('runserver', server)


def dadd(inputs):
    for i in inputs:
        db.session.add(i)
    db.session.commit()

@manager.command
def createdb():
    db.create_all()

    #固定配置 初始化
    #----------------------------------------------------------
    r1 = Role(name='administrator')
    r2 = Role(name='banker')
    r3 = Role(name='enterprise')

    dadd([r1, r2, r3])
    #----------------------------------------------------------

    u1 = User(real_name=u"", name=u'admin', password=User.gen_password('1q2w3e4r'), role_id = r1.id)
    u2 = User(real_name=u"", name=u'bank', password=User.gen_password('1q2w3e4r'), role_id = r2.id)
    u3 = User(real_name=u"", name=u'enterprise', password=User.gen_password('1q2w3e4r'), role_id = r3.id)

    dadd([u1, u2, u3])

    h1 = {
        '1':
        {'content': u'经营范围变更（含业务范围变更）	',
         'before': u'催化剂及精细化工产品生产项目筹建（项目筹建，不得开展生产经营）；化工商品（不含化学危险品）的销售；货物及技术进出口。（依法须经批准的项目，经相关部门批准后方可开展经营活动）***	',
         'after': u'催化剂及精细化工产品（不含化学危险品）生产；化工商品（不含化学危险品）的销售；货物及技术进出口。（依法须经批准的项目，经相关部门批准后方可开展经营活动）***	',
         'time': u'2017年05月17日'
         }
    }
    c1 = Basicinfo(enterprise_id=1,
                 user_id=1,
                 name=u'大连龙缘化学有限公司',
                 credit_code='912102440580649631',
                 register_addr=u'辽宁省大连长兴岛经济区西部产业园区',
                 register_capital=u'4000 万人民币',
                 representative=u'王刃',
                 establish_time=u'2012年12月14日',
                 business_scope=u'催化剂及精细化工产品（不含化学危险品）生产；化工商品（不含化学危险品）的销售；货物及技术进出口。（依法须经批准的项目，经相关部门批准后方可开展经营活动）***',
                 history = h1
                )
    dadd([c1])


@manager.command
def dropdb():
    db.drop_all()




@manager.command
def initdb():
    dropdb()
    createdb()

if __name__ == "__main__":
    manager.run()
