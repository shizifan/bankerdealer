#!/usr/bin/env python
#encoding:utf-8

from flask import Blueprint, request, render_template, \
    g, redirect, make_response, url_for, abort
from src.misc.auth import required
from src.misc.validation import validation
from src.misc.parse import parse_form
from src.business import *
from config.settings import AUTH_KEY


banker = Blueprint('banker', __name__)

@banker.route('/login', methods = ['GET', 'POST'])
@validation('POST:login')
def login_handler():
    role = u'银行'
    if request.method == 'POST':
        info = parse_form('login')
        token = AuthBusiness.login(**info)
        if token:
            resp = make_response(redirect(url_for('banker.index_handler')))
            resp.set_cookie(AUTH_KEY, token)
            return resp
        abort(314)
    return render_template('login.html', **locals())

@banker.route('/logout')
def logout_handler():
    resp = make_response(redirect(url_for('banker.login_handler')))
    resp.set_cookie(AUTH_KEY, "")
    return resp

@banker.route('/')
def index_handler():
    enterprise_list = []
    g.user = u"大连银行"
    enterprise_list.append({'name': u"大连龙缘化学有限公司", 'action': u'正在处理', 'time':'2017-06-01', 'id':'1', 'progress':'60'})
    return render_template('banker/bankindex.html', enterprise_list = enterprise_list)

@banker.route('/<int:enterprise_id>', methods = ['GET', 'POST'])
#@required('banker')
#@validation('POST:add_company')
def detail_handler(enterprise_id):
    g.user = u"大连银行"
    enterprise = BasicinfoBusiness.get_by_id(enterprise_id)
    return render_template('banker/detail.html',enterprise_id = enterprise_id, enterprise=enterprise)


