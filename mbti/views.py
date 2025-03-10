# -*- coding:utf-8 -*-
from __future__ import unicode_literals

import json
import random

from flask import Blueprint, abort, flash, render_template, request

from .utils import get_questions, get_result, get_types_desc

MBTI_BP = Blueprint('mbti', __name__)
QUESTIONS = get_questions()
TYPES_DESC = get_types_desc()


@MBTI_BP.route('/')
def welcome():
    '''欢迎页面，纯属装逼'''
    return render_template('mbti/welcome.html')


@MBTI_BP.route('/home/')
def home():
    '''尼玛逼这才是真正的首页啊'''
    return render_template('mbti/home.html')


@MBTI_BP.route('/about/')
def about():
    '''关于页面'''
    return render_template('mbti/about.html')


@MBTI_BP.route('/personalities/', defaults={'page': 'index'})
@MBTI_BP.route('/personalities/<page>/')
def personalities(page):
    '''SHOW MBTI TYPES'''
    try:
        page = page.lower()
        if page == 'index':
            return render_template('mbti/personalities/index.html',
                                   types_desc=TYPES_DESC)
        else:
            return render_template('mbti/personalities/%s.html' % page)
    except:
        abort(404)


@MBTI_BP.route('/test/', methods=('GET', 'POST'))
def test():
    '''测试页面视图'''
    if request.is_xhr:
        answers = json.loads(request.values.get('answers'))
        result = get_result(answers)
        flash('测试完成，你的性格分析结果为{}型'.format(result))
        return result.lower()
    random.shuffle(QUESTIONS)
    return render_template('mbti/test.html', questions=QUESTIONS)


@MBTI_BP.route('/messageboards/')
def messageboards():
    '''deer要求的留言板，偷懒用多说算了'''
    return render_template('mbti/duoshuo.html')
