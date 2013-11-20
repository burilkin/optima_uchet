# -*- coding: utf-8 -*-
from django.forms import fields, widgets
from django import forms
import datetime
DATE_FORMAT = ('%d.%m.%y',)

class IntervalWidget(widgets.MultiWidget):
    def __init__(self, attrs=None):
        wdgts = (widgets.DateInput(attrs), widgets.DateInput(attrs))
        super(IntervalWidget, self).__init__(wdgts, attrs)

    def decompress(self, value):
        return value or (None, None)
    def format_output(self, rendered_widgets):
        rendered_widgets.insert(0, u'<label>с:')
        rendered_widgets.insert(2, u'</label><label>по:')
        rendered_widgets.insert(4, u'</label>')
        return u''.join(rendered_widgets)

class IntervalField(fields.MultiValueField):
    flds = ()
    widget = IntervalWidget
    def __init__(self, *args, **kwargs):
        flds = (forms.DateField(required=False,input_formats=DATE_FORMAT,),
                forms.DateField(required=False,input_formats=DATE_FORMAT))
        super(IntervalField, self).__init__(flds, *args, **kwargs)

    def compress(self, data_list):
        if data_list:
            if data_list[0] in fields.EMPTY_VALUES:
                data_list[0] = datetime.date(datetime.date.today().year, 1, 1)
                #raise fields.ValidationError(u'Enter a valid latitude.')
            if data_list[1] in fields.EMPTY_VALUES:
                data_list[1] = datetime.date.today()
                #raise fields.ValidationError(u'Enter a valid longitude.')
            return tuple(data_list)
        return None