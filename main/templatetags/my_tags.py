from django import template
from django.template.defaultfilters import stringfilter
from django.utils.html import escape

register = template.Library()


@register.filter(needs_autoescape=True)
@stringfilter
def upper_my(value, autoescape=True):
    if autoescape:
        value = escape(value)
    return value.upper()


@register.filter(needs_autoescape=True)
def kwarg(value, name, autoescape=True):
    if autoescape:
        value = escape(value.resolver_match.kwargs.get(name))
    return value


@register.simple_tag(takes_context=True)
def get_id(context, value):
    return context['request'].resolver_match.kwargs.get(value)


@register.filter
def get_items(value):
    value = value.all()
    if value.count() == 1:
        return str(value[0])
    return ', '.join([str(item) for item in value])


@register.simple_tag(takes_context=True)
def len_paginator_bar(context, number=3):
    current_page_num = context['page_obj'].number
    last_page_num = context['paginator'].page_range[-1] + 1
    if last_page_num <= number:
        return range(1, last_page_num)
    # if not isinstance(number, int):
    #     raise AttributeError('Need enter number(int) ')
    add = current_page_num + number
    if last_page_num >= add:
        pages = range(current_page_num, add)
    else:
        pages = range(current_page_num - (add - last_page_num), last_page_num)
    return pages
