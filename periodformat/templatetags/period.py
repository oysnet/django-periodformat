# -*- coding: utf-8 -*-
from django import template
from django.template.defaultfilters import stringfilter, urlencode, date
    
register = template.Library()

def has_time(*args):
    for d in args:
        if d.hour != 0 or d.time != 0:
            return True
        
def has_minutes(*args):
    for d in args:
        if d.time().minute != 0:
            return True

formats = {}
formats['00000'] = u'Du %(start_day)s %(start_daynum)s %(start_month)s %(start_year)s au %(end_day)s %(end_daynum)s %(end_month)s %(end_year)s '
formats['00001'] = u'Du %(start_day)s %(start_daynum)s %(start_month)s %(start_year)s au %(end_day)s %(end_daynum)s %(end_month)s %(start_year)s '
formats['00010'] = u'Du %(start_day)s %(start_daynum)s %(start_month)s %(start_year)s au %(end_day)s %(end_daynum)s %(start_month)s %(end_year)s '
formats['00011'] = u'Du %(start_day)s %(start_daynum)s %(start_month)s %(start_year)s au %(end_day)s %(end_daynum)s %(start_month)s %(start_year)s '
formats['00100'] = u'Du %(start_day)s %(start_daynum)s %(start_month)s %(start_year)s au %(start_day)s %(start_daynum)s %(end_month)s %(end_year)s '
formats['00101'] = u'Du %(start_day)s %(start_daynum)s %(start_month)s %(start_year)s au %(start_day)s %(start_daynum)s %(end_month)s %(start_year)s '
formats['00110'] = u'Du %(start_day)s %(start_daynum)s %(start_month)s %(start_year)s au %(start_day)s %(start_daynum)s %(start_month)s %(end_year)s '
formats['00111'] = u'Du %(start_day)s %(start_daynum)s %(start_month)s %(start_year)s au %(start_day)s %(start_daynum)s %(start_month)s %(start_year)s '
formats['01000'] = u'Du %(start_day)s %(start_daynum)s %(start_month)s %(start_year)s au %(end_day)s %(end_daynum)s %(end_month)s %(end_year)s '
formats['01001'] = u'Du %(start_day)s %(start_daynum)s %(start_month)s %(start_year)s au %(end_day)s %(end_daynum)s %(end_month)s %(start_year)s '
formats['01010'] = u'Du %(start_day)s %(start_daynum)s %(start_month)s %(start_year)s au %(end_day)s %(end_daynum)s %(start_month)s %(end_year)s '
formats['01011'] = u'Du %(start_day)s %(start_daynum)s %(start_month)s %(start_year)s au %(end_day)s %(end_daynum)s %(start_month)s %(start_year)s '
formats['01100'] = u'Du %(start_day)s %(start_daynum)s %(start_month)s %(start_year)s au %(start_day)s %(start_daynum)s %(end_month)s %(end_year)s '
formats['01101'] = u'Du %(start_day)s %(start_daynum)s %(start_month)s %(start_year)s au %(start_day)s %(start_daynum)s %(end_month)s %(start_year)s '
formats['01110'] = u'Du %(start_day)s %(start_daynum)s %(start_month)s %(start_year)s au %(start_day)s %(start_daynum)s %(start_month)s %(end_year)s '
formats['01111'] = u'Du %(start_day)s %(start_daynum)s %(start_month)s %(start_year)s au %(start_day)s %(start_daynum)s %(start_month)s %(start_year)s '
formats['10000'] = u'Du %(start_day)s %(start_daynum)s %(start_month)s %(start_year)s %(start_time)s au %(end_day)s %(end_daynum)s %(end_month)s %(end_year)s %(end_time)s '
formats['10001'] = u'Du %(start_day)s %(start_daynum)s %(start_month)s %(start_year)s %(start_time)s au %(end_day)s %(end_daynum)s %(end_month)s %(start_year)s %(end_time)s '
formats['10010'] = u'Du %(start_day)s %(start_daynum)s %(start_month)s %(start_year)s %(start_time)s au %(end_day)s %(end_daynum)s %(start_month)s %(end_year)s %(end_time)s '
formats['10011'] = u'Du %(start_day)s %(start_daynum)s %(start_month)s %(start_year)s %(start_time)s au %(end_day)s %(end_daynum)s %(start_month)s %(start_year)s %(end_time)s '
formats['10100'] = u'Du %(start_day)s %(start_daynum)s %(start_month)s %(start_year)s %(start_time)s au %(start_day)s %(start_daynum)s %(end_month)s %(end_year)s %(end_time)s '
formats['10101'] = u'Du %(start_day)s %(start_daynum)s %(start_month)s %(start_year)s %(start_time)s au %(start_day)s %(start_daynum)s %(end_month)s %(start_year)s %(end_time)s '
formats['10110'] = u'Du %(start_day)s %(start_daynum)s %(start_month)s %(start_year)s %(start_time)s au %(start_day)s %(start_daynum)s %(start_month)s %(end_year)s %(end_time)s '
formats['10111'] = u'%(start_day)s %(start_daynum)s %(start_month)s %(start_year)s de %(start_time)s à %(end_time)s '
formats['11000'] = u'Du %(start_day)s %(start_daynum)s %(start_month)s %(start_year)s %(start_time)s au %(end_day)s %(end_daynum)s %(end_month)s %(end_year)s %(start_time)s '
formats['11001'] = u'Du %(start_day)s %(start_daynum)s %(start_month)s %(start_year)s %(start_time)s au %(end_day)s %(end_daynum)s %(end_month)s %(start_year)s %(start_time)s '
formats['11010'] = u'Du %(start_day)s %(start_daynum)s %(start_month)s %(start_year)s %(start_time)s au %(end_day)s %(end_daynum)s %(start_month)s %(end_year)s %(start_time)s '
formats['11011'] = u'Du %(start_day)s %(start_daynum)s %(start_month)s %(start_year)s %(start_time)s au %(end_day)s %(end_daynum)s %(start_month)s %(start_year)s %(start_time)s '
formats['11100'] = u'Du %(start_day)s %(start_daynum)s %(start_month)s %(start_year)s %(start_time)s au %(start_day)s %(start_daynum)s %(end_month)s %(end_year)s %(start_time)s '
formats['11101'] = u'Du %(start_day)s %(start_daynum)s %(start_month)s %(start_year)s %(start_time)s au %(start_day)s %(start_daynum)s %(end_month)s %(start_year)s %(start_time)s '
formats['11110'] = u'Du %(start_day)s %(start_daynum)s %(start_month)s %(start_year)s %(start_time)s au %(start_day)s %(start_daynum)s %(start_month)s %(end_year)s %(start_time)s '
formats['11111'] = u'Du %(start_day)s %(start_daynum)s %(start_month)s %(start_year)s %(start_time)s au %(start_day)s %(start_daynum)s %(start_month)s %(start_year)s %(start_time)s '


@register.tag(name="format_period")
def do_format_period(parser, token):
    try:
        tag_name, start_date, end_date = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError("%r tag requires exactly two arguments" % token.contents.split()[0])
    return FormatPeriodNode(start_date, end_date)

class FormatPeriodNode(template.Node):
    def __init__(self, start_date, end_date):
        self.start_date = template.Variable(start_date)
        self.end_date = template.Variable(end_date)

    def render(self, context):
        try:
            start_date = self.start_date.resolve(context)
            end_date = self.end_date.resolve(context)
            return format_period(start_date, end_date)
        except template.VariableDoesNotExist:
            return ''


def format_period(start_date, end_date=None):
    
    if end_date is not None and start_date != end_date:
        key  = '1' if has_time(start_date,end_date) else '0'
        key += '1' if start_date.time() == end_date.time() else '0'
        key += '1' if start_date.day == end_date.day else '0'
        key += '1' if start_date.month == end_date.month else '0'
        key += '1' if start_date.year == end_date.year else '0'
        data = {
                'start_time' : date(start_date,'H\hi') if has_minutes(start_date) else date(start_date,'H\h'),
                'start_day' : date(start_date,'l'),
                'start_daynum' : date(start_date,'j'),
                'start_month' : date(start_date,'F'),
                'start_year': date(start_date,'Y'),
                'end_time' : date(end_date,'H\hi') if has_minutes(end_date) else date(end_date,'H\h'),
                'end_daynum' : date(end_date,'j'),
                'end_day' : date(end_date,'l'),
                'end_month' : date(end_date,'F'),
                'end_year': date(end_date,'Y')
        }
        return (formats[key] % data).capitalize()
    else:
        return date(start_date,'l j F Y').capitalize()
         
    