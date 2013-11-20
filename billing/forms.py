# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from models import *
from multifield import *
DATE_FORMAT = ('%d.%m.%y',)
CHOICES = ((50, '50'), (100, '100'), (200, '200'), (300, '300'))
def getTuple(model, *fields):
    t = tuple(model.objects.values_list(*fields))
    return t

class MyModelMultipleChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return "%s" % obj.type

class invoices_search(forms.Form):
    id = forms.IntegerField(required=False, label='Код')
    invno = forms.IntegerField(required=False, label='№')
    #type = MyModelMultipleChoiceField(queryset=Invoice_types.objects.only('id'), required=False, label='Тип заказа')
    type = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=getTuple(Invoice_types), required=False, label='Тип заказа')
    seller__title = forms.CharField(required=False,  label='Отпускающий')
    customer__title = forms.CharField(required=False, label='Покупатель')
    date = IntervalField(required=False, label='Дата')
    sum = forms.DecimalField(required=False,label='Сумма')
    sumB = forms.DecimalField(required=False,label='СуммаБ')
    released = forms.NullBooleanField(required=False,label='Отпущено')
    releasedB = forms.NullBooleanField(required=False,label='ОтпущеноБ')
    payed = forms.DecimalField(required=False,label='Оплачено')
    compl_date = forms.DateField(required=False,label='')
    ID_SW = forms.IntegerField(required=False, label='Код СО')
    store = forms.MultipleChoiceField(choices=getTuple(Stores), required=False, label='Склад')
    def clean(self):
        for key in self.cleaned_data:
            if not ((self.cleaned_data[key] == None) or
                    (self.cleaned_data[key] == u'') or
                    (self.cleaned_data[key] == [])):
                break
        else:
            raise forms.ValidationError('Укажите хотябы одно условие для фильтрации')
        return self.cleaned_data
class Other(forms.Form):
    elements = forms.ChoiceField(widget=forms.Select, choices=CHOICES, label='эл. на стр.')

class interval(forms.Form):
    intr = IntervalField(required=False, widget=IntervalWidget)
    note = forms.CharField(required=False)
    #date = forms.SplitDateTimeField(required=False)