# -*- coding: utf-8 -*-
# Create your views here.
from django.db.models import Q
from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404
from billing.models import Invoices, Invoice_types, Contractors, Employees, Stores, Contract
import datetime
from forms import invoices_search, Other, IntervalField, interval, IntervalWidget

# Получить словарь verbose_name всех полей для модели (таблицы БД)
# {'имя_поля1_vn': 'verbose_name_поля1', 'имя_поля2_vn': 'verbose_name_поля2', ...}
def get_labels_for(model, lowCase=False):
        from django.template.defaultfilters import lower
        labels = {}
        for field in model._meta.fields:
            label = field.verbose_name
            if lowCase:
                label = lower(label)
            labels[field.name + '_vn'] = label
        return labels
# Получить список номеров страниц элементов модели в зависимости от количества элементов на странице
def get_pages_for(query, elemonpage=100):
    page_count = float(query.count())/elemonpage
    intpage = int(page_count)
    if page_count-intpage>0:
        page_count = intpage+1
    else:
        page_count = intpage
    #k = 0
    pages = []
    for i in range(1,page_count+1):
        #fr = (elemonpage*k)
        #to = i*elemonpage
        pages.append(i)
        #pages[i]= "%s-%s" %(fr, to)
        #k = k+1
    return pages

def home(request):
    return render_to_response('main.html')

def invoices(request, page=1):
    sortmode = {-1:['-','▲'],1:['','▼']}
    sort = [-1,'id']
    page = int(page)
    elements = 100
    url = request.GET.urlencode()
    get_param = request.GET.copy()
    if 'sort' in request.GET and  request.GET['sort']:
        sort = request.GET.getlist('sort')
        sort[0] = int(sort[0])
        del get_param['sort']
    sorturl = get_param.urlencode()
    if 'elements' in request.GET and request.GET['elements']:
        elements = int(request.GET['elements'])
    form = invoices_search(request.GET)
    tools = Other(initial={'elements': elements})
    if form.is_valid():
        cd = form.cleaned_data
        inv = field_search(Invoices, cd)
        #form = invoices_search(request.GET)
    else:
        inv = Invoices.objects.select_related(depth=1)
    to = elements * page
    fr = to - elements
    name = Invoices._meta.verbose_name_plural
    pages = get_pages_for(inv, elements)
    #assert False
    inv=inv.order_by(sortmode[sort[0]][0]+sort[1])[fr:to]
    column = sort[1]
    oldsort = sort[0]
    sym = sortmode[oldsort][1]
    newsort = sort[0]*-1
    newsym = sortmode[newsort][1]
    #else:
    #inv = Invoices.objects.select_related(depth=1).order_by('id')[fr:to]
    #inv = Invoices.objects.all()[fr:to]
    #inv = Invoices.objects.defer('contract').select_related(depth=1).order_by('-id').filter(
    #   Q(type__in='*'))[fr:to]
    #assert False
    labels = get_labels_for(Invoices)
    l = request.GET
    return render_to_response('invoices.html', locals())

def field_search(model, cd):
    query = model.objects.select_related(depth=1)
    for key, value in cd.items():
        if isinstance(value, int) and value is not None:
            kwargs = {key: value}
            query = query.filter(**kwargs)
        if isinstance(value, unicode) and value is not u'':
            key = key + '__icontains'
            kwargs = {key: value}
            query = query.filter(**kwargs)
        if isinstance(value, list) and value != []:
            i = 0
            for val in value:
                value[i] = int(val)
                i = i + 1
            key = key + '__in'
            kwargs = {key: value}
            query = query.filter(**kwargs)
        if isinstance(value, tuple) and value != ():
            i = 0
            for val in value:
                i = i + 1
            key = key + '__range'
            kwargs = {key: value}
            query = query.filter(**kwargs)

        #assert False
    return query

def invoice_edit(request, invoice):
    if invoice == u'new':
        return render_to_response('invoice_edit.html', locals())
    else:
        invoice = int(invoice)
        return render_to_response('invoice_edit.html', locals())
def form(request):
    q = Invoices.objects.select_related(depth=1).order_by('id')[0:10]
    if 'seller' in request.GET and request.GET['seller']:
        q = Invoices.objects.filter(seller__title__icontains= request.GET['seller'])[0:10]
    f = f_invoices(request.GET)
    if f.is_valid():
        f = f_invoices(request.GET)
    l=[]
    for i in request.GET.values():
        l.append(type(i))

    #assert False
    return render_to_response('inv.html', locals())

def fff(request):
    l = request.GET
    f = interval(request.GET)
    if request.method == "GET" and f.is_valid():
        cd = f.cleaned_data
    else:
        cd = 5
    from django.forms.models import inlineformset_factory
    InvFormSet = inlineformset_factory(Contract, Invoices)
    contract = Contract.objects.get(id=1)
    formset = InvFormSet(instance=contract)
    wgt = IntervalWidget()
    #x = wgt.render('name', 'A name')
    #s = f.intr.flds
    return  render_to_response('inv.html',locals())

def insert(request):
    t1 = Invoice_types.objects.get(id =5)
    t2 = Invoice_types.objects.get(id =3)
    s1 = Contractors.objects.get(id =1)
    s2 = Contractors.objects.get(id =2)
    s3 = Contractors.objects.get(id =3)
    s4 = Contractors.objects.get(id =4)
    e1 = Employees.objects.get(id =1)
    st = Stores.objects.get(id=1)
    dt = datetime.datetime.now()
    cn = Contract.objects.get(id=1)
    for i in range(1,550):
        Invoices(type=t1, seller=s1, customer=s3,store=st, creator=e1, contract=cn, date=dt).save()
        Invoices(type=t2, seller=s2, customer=s4,store=st, creator=e1, contract=cn, date=dt).save()
    return HttpResponse('Succes')