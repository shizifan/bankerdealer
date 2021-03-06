#!/usr/bin/env python
#encoding:utf-8

from flask import Blueprint, request, render_template, \
    g, redirect, make_response, url_for, abort
from src.misc.auth import required
from src.misc.validation import validation
from src.misc.parse import parse_form, parse_history, parse_baseinfo
from src.business import *
from config.settings import AUTH_KEY
import json

enterprise = Blueprint('enterprise', __name__)


@enterprise.route('/login', methods = ['GET', 'POST'])
#@validation('POST:login')
def login_handler():
    role = u'企业'
    if request.method == 'POST':
        info = parse_form('login')
        token = AuthBusiness.login(**info)
        if token:
            resp = make_response(redirect(url_for('enterprise.index_handler')))
            resp.set_cookie(AUTH_KEY, token)
            return resp
        abort(314)
    return render_template('login.html', **locals())

@enterprise.route('/logout')
def logout_handler():
    resp = make_response(redirect(url_for('enterprise.login_handler')))
    resp.set_cookie(AUTH_KEY, "")
    return resp

@enterprise.route('/')
#@required('enterprise')
def index_handler():
    return render_template('enterprise/list.html', menus = g.menus)



@enterprise.route('/basicinfo', methods = ['GET', 'POST'])
#@required('enterprise')
#@validation('POST:add_company')
def basicinfo_handler():
    enterprise_id = 1
    enterprise = BasicinfoBusiness.get_by_id(enterprise_id)
    if request.method == 'POST':
        enterprise = parse_baseinfo(request.form)
        BasicinfoBusiness.save(enterprise, enterprise_id)
        return render_template('enterprise/basicinfo.html',  enterprise_id = enterprise_id, menus = g.menus, enterprise=enterprise)
    return render_template('enterprise/basicinfo.html', enterprise_id = enterprise_id, menus = g.menus, enterprise=enterprise)


@enterprise.route('/industry', methods = ['GET', 'POST'])
#@required('enterprise')
#@validation('POST:add_industry')
def industry_handler():
    user_id = 100;
    industry = IndustryBusiness.get_by_id(user_id)
    if request.method == 'POST':
        info = parse_form('add_industry')
        info.update(dict(user_id=user_id))
        IndustryBusiness.save(info)
    return render_template('enterprise/industry.html', menus = g.menus, industry=industry)


@enterprise.route('/operate', methods = ['GET', 'POST'])
#@required('enterprise')
#@validation('POST:add_operate')
def operate_handler():
    user_id = 100;
    operate = OperateBusiness.get_by_id(user_id)
    if request.method == 'POST':
        return render_template('enterprise/operate.html', user_id = user_id, menus=g.menus, operate=operate)
    return render_template('enterprise/operate.html', user_id = user_id, menus = g.menus, operate=operate)

@enterprise.route('/revenue', methods = ['GET', 'POST'])
#@required('enterprise')
def revenue_handler():
    enterprise_id = g.userid
    revenue = RevenueBusiness.get_by_id(enterprise_id)
    if request.method == 'POST':
        revenue = parse_history(request.form)
        HistoryBusiness.save(revenue, g.userid)
        return render_template('enterprise/revenue.html',user_id = enterprise_id, menus = g.menus, revenue=revenue)
    return render_template('enterprise/revenue.html',user_id = enterprise_id, menus = g.menus, revenue=revenue)


@enterprise.route('/finance', methods = ['GET', 'POST'])
#@required('enterprise')
#@validation('POST:add_finance')
def finance_handler():
    if request.method == 'POST':
        print request.form
    return render_template('enterprise/finance.html', menus = g.menus, finance=finance)


@enterprise.route('/credit', methods = ['GET', 'POST'])
#@required('enterprise')
#@validation('POST:add_credit')
def credit_handler():
    return render_template('enterprise/credit.html', menus = g.menus, credit=credit)
