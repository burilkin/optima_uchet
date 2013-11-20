# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Imprest_reports(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(verbose_name='Дата')

    def __unicode__(self):
        return u'%s %s' % (self.id, self.date)

    class Meta:
        db_table = 'imprest_reports'
        verbose_name_plural = 'Авансовые отчеты'

class Devices(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=30, verbose_name='Тип')
    model = models.CharField(max_length=30, verbose_name='Модель')
    sn = models.CharField(max_length=30, verbose_name='с/н', unique=True)
    location = models.CharField(max_length=30, blank=True, verbose_name='Местонахождение')

    def __unicode__(self):
        return u'%s %s %s %s %s' % (self.id, self.type, self.model, self.sn, self.location)

    class Meta:
        db_table = 'devices'
        verbose_name_plural = 'Аппараты'

class Contractor_types(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=11, verbose_name='Тип')

    def __unicode__(self):
        return u'%s %s' % (self.id, self.type)

    class Meta:
        db_table = 'contractor_types'
        verbose_name_plural = 'Типы Контрагентов'

class Employees(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name='Сотрудник')
    speciality = models.CharField(max_length=30, verbose_name='Должность')
    wage_rate = models.SmallIntegerField(null=True, verbose_name='Ставка')

    def __unicode__(self):
        return u'%s %s %s %s' % (self.id, self.name, self.speciality, self.wage_rate)

    class Meta:
        db_table = 'employees'
        verbose_name_plural = 'Сотрудники'

class Contractors(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.ForeignKey(Contractor_types, db_column='type_id', verbose_name='Тип')
    title = models.CharField(max_length=100, verbose_name='Контрагент')
    country = models.CharField(max_length=20, verbose_name='Страна', default='Российская Федерация')
    region = models.CharField(max_length=30, verbose_name='Регион', default='Смоленская область')
    city = models.CharField(max_length=20, verbose_name='Город', default='Смоленск')
    ZIP = models.CharField(max_length=10,blank=True, verbose_name='Индекс')
    address = models.CharField(max_length=100,blank=True, verbose_name='Адрес')
    phone = models.CharField(max_length=50, blank=True, verbose_name='Телефон')
    e_mail = models.EmailField(blank=True, verbose_name='Эл. почта')
    INN = models.CharField(max_length=12, verbose_name='ИНН', unique=True)
    KPP = models.CharField(max_length=9, verbose_name='КПП')
    OGRN = models.CharField(max_length=13, verbose_name='ОГРН', unique=True)
    VAT = models.SmallIntegerField(default=0, verbose_name='НДС')
    director = models.CharField(max_length=50, blank=True, verbose_name='Директор')
    accountant = models.CharField(max_length=50, blank=True, verbose_name='Бухгалтер')
    clerk = models.CharField(max_length=50, blank=True, verbose_name='Менеджер')

    def __unicode__(self):
        return u'%s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s' %\
               (self.id, self.type, self.title, self.country, self.region, self.city, self.ZIP,
                   self.address, self.phone, self.e_mail, self.INN, self.KPP, self.OGRN,
                   self.VAT, self.director, self.accountant, self.clerk)

    class Meta:
        db_table = 'contractors'
        verbose_name_plural = 'Контрагенты'

class Contract_types(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=20, verbose_name='Тип')

    def __unicode__(self):
        return u'%s %s' % (self.id, self.type)

    class Meta:
        db_table = 'contract_types'
        verbose_name_plural = 'Типы Договоров'

class Contract(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.ForeignKey(Contract_types, db_column='type_id', verbose_name='Тип')
    contr_num = models.CharField(max_length=10, verbose_name='№ дог.')
    seller = models.ForeignKey(Contractors, db_column='seller_id', related_name='seller.contract_set',
                               verbose_name='Отпускающий')
    customer = models.ForeignKey(Contractors, db_column='customer_id', related_name='customer.contract_set',
                                 verbose_name='Покупатель')
    sum = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='Сумма')

    def __unicode__(self):
        return u'%s %s %s %s %s %s' %\
               (self.id, self.type, self.contr_num, self.seller, self.customer, self.sum)

    class Meta:
        db_table = 'contract'
        verbose_name_plural = 'Договора'

class Units(models.Model):
    id = models.CharField(max_length=3, primary_key=True)
    title = models.CharField(max_length=30, unique=True, verbose_name='Название')
    symbol = models.CharField(max_length=6, unique=True, verbose_name='Ед.Изм.')

    def __unicode__(self):
        return u'%s %s %s' % (self.id, self.title, self.symbol)

    class Meta:
        db_table = 'units'
        verbose_name_plural = 'Еденицы Изм.'

class Prod_types1(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20, verbose_name='Группа', unique=True)

    def __unicode__(self):
        return u'%s %s' % (self.id, self.title)

    class Meta:
        db_table = 'prod_types1'
        verbose_name_plural = 'Группы'

class Prod_types2(models.Model):
    id = models.AutoField(primary_key=True)
    type1 = models.ForeignKey(Prod_types1, db_column='type1')
    title = models.CharField(max_length=20, verbose_name='Тип', unique=True)

    def __unicode__(self):
        return u'%s %s' % (self.id, self.title)

    class Meta:
        db_table = 'prod_types2'
        verbose_name_plural = 'Типы'

class Prod_types3(models.Model):
    id = models.AutoField(primary_key=True)
    type2 = models.ForeignKey(Prod_types2, db_column='type2')
    title = models.CharField(max_length=20, verbose_name='Подтип', unique=True)

    def __unicode__(self):
        return u'%s %s' % (self.id, self.title)

    class Meta:
        db_table = 'prod_types3'
        verbose_name_plural = 'Подтипы'

class Products(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.ForeignKey(Prod_types3, db_column='type_id', verbose_name='Тип')
    title = models.CharField(max_length=20, verbose_name='Наименование', unique=True)
    man_code = models.CharField(max_length=20, verbose_name='Артикул', unique=True)
    unit = models.ForeignKey(Units, db_column='unit_id', verbose_name='Ед.изм.')
    price = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='Цена')
    warranty_period = models.SmallIntegerField(null=True, verbose_name='Гар.срок')
    wage_rate = models.SmallIntegerField(null=True, verbose_name='Ставка')
    limit = models.SmallIntegerField(null=True, verbose_name='Лимит')
    note = models.CharField(max_length=20, blank=True, verbose_name='Примечание')
    weight = models.SmallIntegerField(null=True, verbose_name='Вес')

    def __unicode__(self):
        return u'%s %s %s %s %s %s %s %s %s %s %s' %\
               (self.id, self.type, self.title, self.man_code, self.unit, self.price,
                self.warranty_period, self.wage_rate, self.limit, self.note, self.weight)

    class Meta:
        db_table = 'products'
        verbose_name_plural = 'Товары'

class Invoice_types(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=10, verbose_name='Тип')

    def __unicode__(self):
        return u'%s %s' % (self.id, self.type)

    class Meta:
        db_table = 'invoice_types'
        verbose_name_plural = 'Типы заказа'

class Stores(models.Model):
    id = models.AutoField(primary_key=True)
    store = models.CharField(max_length=10, verbose_name='Склад')

    def __unicode__(self):
        return u'%s %s' % (self.id, self.store)

    class Meta:
        db_table = 'stores'
        verbose_name_plural = 'Склады'

class Invoices(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='Код')
    invno = models.SmallIntegerField(default=0, verbose_name='№')
    type = models.ForeignKey(Invoice_types, db_column='type_id', verbose_name='Тип')
    seller = models.ForeignKey(Contractors, db_column='seller_id', related_name='seller.invoice_set', verbose_name='Отпускающий')
    customer = models.ForeignKey(Contractors, db_column='customer_id', related_name='customer.invoice_set', verbose_name='Покупатель')
    date = models.DateField(verbose_name='Дата')
    note = models.CharField(max_length=30, blank=True, verbose_name='Примечание')
    contract = models.ForeignKey(Contract, db_column='contr_id', verbose_name='Договор')
    VAT = models.SmallIntegerField(default=0, verbose_name='НДС')
    creator = models.ForeignKey(Employees, db_column='creator', verbose_name='Создал')
    to_exp = models.DateField(null=True, blank=True, verbose_name='Экспертиза')
    to_reg = models.DateField(null=True, blank=True, verbose_name='Техконтроль')
    to_fabric = models.DateField(null=True, blank=True, verbose_name='В производство')
    sum = models.DecimalField(max_digits=11, decimal_places=2, null=True, blank=True, verbose_name='Сумма')
    sumB = models.DecimalField(max_digits=11, decimal_places=2, null=True, blank=True, verbose_name='СуммаБ')
    released = models.BooleanField(default=False,verbose_name='Отпущено')
    releasedB = models.BooleanField(default=False,verbose_name='ОтпущеноБ')
    payed = models.DecimalField(max_digits=11, decimal_places=2, null=True, blank=True, verbose_name='Оплачено')
    compl_date = models.DateField(null=True, blank=True, verbose_name='Закрыт')
    ID_SW = models.SmallIntegerField(null=True, blank=True, verbose_name='КодСО')
    store = models.ForeignKey(Stores, db_column='store_id', verbose_name='Склад')

    def __unicode__(self):
        return u'%s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s' %\
               (self.id, self.invno, self.type, self.seller, self.customer, self.date,
                self.note, self.contract, self.VAT, self.creator, self.to_exp, self.to_reg,
                self.to_fabric, self.sum, self.sumB, self.released, self.releasedB, self.payed,
                self.compl_date, self.ID_SW, self.store)
    class Meta:
        db_table = 'invoices'
        verbose_name_plural = 'Заказы'

class Sub_invoices(models.Model):
    id = models.AutoField(primary_key=True)
    invoice = models.ForeignKey(Invoices, db_column='inv_id', verbose_name='Заказ')
    date = models.DateField(verbose_name='Дата')
    reason = models.CharField(max_length=50, blank=True, verbose_name='Основание')
    customer = models.ForeignKey(Contractors, db_column='customer_id', verbose_name='Покупатель')

    def __unicode__(self):
        return u'%s %s %s %s %s' % (self.id, self.invoice, self.date, self.reason,
                                    self.customer)

    class Meta:
        db_table = 'sub_invoices'
        verbose_name_plural = 'Рукописные счета'

class Sub_articles(models.Model):
    id = models.AutoField(primary_key=True)
    subinvoice = models.ForeignKey(Sub_invoices, db_column='subinv_id', verbose_name='Рук.счет')
    qty = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Кол-во')
    price = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='Цена')
    discount = models.SmallIntegerField(default=0, verbose_name='Скидка')
    sum = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='Сумма')
    product = models.ForeignKey(Products, db_column='prod_id', verbose_name='Товар')
    parameters = models.CharField(max_length=20, blank=True, verbose_name='Параметр')

    def __unicode__(self):
        return u'%s %s %s %s %s %s %s %s' %\
               (self.id, self.subinvoice, self.product, self.parameters, self.qty, self.price,
                           self.discount, self.sum)

    class Meta:
        db_table = 'sub_articles'
        verbose_name_plural = 'Детали Счета'

class Banks(models.Model):
    id = models.AutoField(primary_key=True)
    bank = models.CharField(max_length=70, verbose_name='Банк')
    BIK = models.CharField(max_length=9, verbose_name='БИК',)
    k_c = models.CharField(max_length=20, verbose_name='Кор.счет', unique=True)

    def __unicode__(self):
        return u'%s %s %s %s' % (self.id, self.bank, self.BIK, self.k_c)

    class Meta:
        db_table = 'banks'
        verbose_name_plural = 'Банки'

class Account_types(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=8, verbose_name='Тип')

    def __unicode__(self):
        return u'%s %s' % (self.id, self.type)

    class Meta:
        db_table = 'account_types'
        verbose_name_plural = 'Типы счетов'

class Current_accounts(models.Model):
    id = models.AutoField(primary_key=True)
    num = models.CharField(max_length=25, verbose_name='Р/с', unique=True)
    contractor = models.ForeignKey(Contractors, db_column='contractor_id', verbose_name='Контрагент')
    type = models.ForeignKey(Account_types, db_column='type_id', verbose_name='Тип')
    bank = models.ForeignKey(Banks, db_column='bank_id', verbose_name='Банк')

    def __unicode__(self):
        return u'%s %s %s %s %s' % (self.id, self.num, self.contractor, self.type, self.bank)

    class Meta:
        db_table = 'current_accounts'
        verbose_name_plural = 'Расчетные счета'

class Articles(models.Model):
    id = models.AutoField(primary_key=True)
    invoice = models.ForeignKey(Invoices, db_column='inv_id', verbose_name='Заказ')
    product = models.ForeignKey(Products, db_column='prod_id', verbose_name='Товар')
    parameters = models.CharField(max_length=20, blank=True, verbose_name='Параметры')
    qty = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Кол-во')
    price = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='Цена')
    discount = models.SmallIntegerField(default=0, verbose_name='Скидка')
    sum = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='Сумма')
    device = models.ForeignKey(Devices, db_column='device_id', verbose_name='Аппарат')
    page_count = models.BigIntegerField(null=True, verbose_name='Кол.стр.')
    warranty_period = models.SmallIntegerField(null=True, verbose_name='Гар.срок')
    warranty_pages = models.IntegerField(null=True, verbose_name='Гар.стр.')
    comment = models.CharField(max_length=50, blank=True, verbose_name='Примечания')
    performer = models.ForeignKey(Employees, db_column='performer')
    perform_date = models.DateField(null=True, verbose_name='Исполнено')
    end_date = models.DateField(null=True, verbose_name='Закрыто')

    def __unicode__(self):
        return u'%s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s' %\
               (self.id, self.invoice,self.product, self.parameters, self.qty, self.price,
                   self.discount, self.sum, self.device, self.page_count, self.warranty_period,
                   self.warranty_pages, self.comment, self.performer, self.perform_date,
                   self.end_date)

    class Meta:
        db_table = 'articles'
        verbose_name_plural = 'Заказано'


class Components(models.Model):
    id = models.AutoField(primary_key=True)
    article = models.ForeignKey(Articles, db_column='art_id', verbose_name='Позиция')
    product = models.ForeignKey(Products, db_column='prod_id', verbose_name='Товар')
    parameters = models.CharField(max_length=20, blank=True, verbose_name='Параметры')
    qty = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Кол-во')
    price = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='Цена')
    sum = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='Сумма')

    def __unicode__(self):
        return u'%s %s %s %s %s %s %s' % (self.id, self.article,self.product,
                                          self.parameters, self.qty, self.price,
                                          self.sum)

    class Meta:
        db_table = 'components'
        verbose_name_plural = 'Комплектация'

class ArticlesB(models.Model):
    id = models.AutoField(primary_key=True)
    invoice = models.ForeignKey(Invoices, db_column='inv_id', verbose_name='Заказ')
    product = models.ForeignKey(Products, db_column='prod_id', verbose_name='Товар')
    parameters = models.CharField(max_length=20, blank=True, verbose_name='Параметр')
    qty = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Кол-во')
    price = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='Цена')
    discount = models.SmallIntegerField(default=0, verbose_name='Скидка' )
    sum = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='Сумма')
    performer = models.ForeignKey(Employees, db_column='performer')

    def __unicode__(self):
        return u'%s %s %s %s %s %s %s %s %s' %\
               (self.id, self.invoice,self.product, self.parameters,
                self.qty, self.price, self.discount, self.sum, self.performer)

    class Meta:
        db_table = 'articlesb'
        verbose_name_plural = 'ЗаказаноБ'

class ComponentsB(models.Model):
    id = models.AutoField(primary_key=True)
    article = models.ForeignKey(ArticlesB, db_column='artB_id', verbose_name='Позиция')
    product = models.ForeignKey(Products, db_column='prod_id', verbose_name='Товар')
    parameters = models.CharField(max_length=20, blank=True, verbose_name='Параметр')
    qty = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Кол-во')
    price = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='Цена')
    sum = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='Сумма')

    def __unicode__(self):
        return u'%s %s %s %s %s %s %s' % (self.id, self.article,self.product,
                                          self.parameters, self.qty, self.price,
                                          self.sum)

    class Meta:
        db_table = 'componentsb'
        verbose_name_plural = 'КомплектацияБ'

class Demands(models.Model):
    id = models.AutoField(primary_key=True)
    invoice = models.ForeignKey(Invoices, db_column='inv_id', verbose_name='Заказ')
    date = models.DateField(verbose_name='Дата')
    note = models.CharField(max_length=20, blank=True, verbose_name='Примечание')
    store = models.ForeignKey(Stores, db_column='store_id', verbose_name='Склад')

    def __unicode__(self):
        return u'%s %s %s %s %s' % (self.id, self.invoice,self.date, self.note, self.store)

    class Meta:
        db_table = 'demands'
        verbose_name_plural = 'Требования'

class Demand_details(models.Model):
    demand = models.ForeignKey(Demands, db_column='demand_id', verbose_name='Требование')
    component = models.ForeignKey(Components, db_column='comp_id', verbose_name='Компонент')
    qty = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Кол-во')

    def __unicode__(self):
        return u'%s %s %s' % (self.demand, self.component,self.qty)

    class Meta:
        db_table = 'demand_details'
        verbose_name_plural = 'Детали требования'
        unique_together = ('demand', 'component')

class Out_waybills(models.Model):
    id = models.AutoField(primary_key=True)
    invoice = models.ForeignKey(Invoices, db_column='inv_id', verbose_name='Заказ')
    account = models.ForeignKey(Current_accounts, db_column='account_id', verbose_name='Счет')
    date = models.DateField(verbose_name='Дата')
    note = models.CharField(max_length=20, blank=True, verbose_name='Примечание')
    store = models.ForeignKey(Stores, db_column='store_id', verbose_name='Склад')
    declaration_no = models.CharField(max_length=20, blank=True, verbose_name='№ Декларации')

    def __unicode__(self):
        return u'%s %s %s %s %s %s %s' % (self.id, self.invoice, self.account,self.date,
                                          self.note, self.store, self.declaration_no)

    class Meta:
        db_table = 'out_waybills'
        verbose_name_plural = 'Накладные'

class Out_waybill_details(models.Model):
    waybill = models.ForeignKey(Out_waybills, db_column='wbl_id', verbose_name='Накладная')
    article = models.ForeignKey(ArticlesB, db_column='artB_id', verbose_name='Позиция')
    qty = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Кол-во')

    def __unicode__(self):
        return u'%s %s %s' % (self.waybill, self.article, self.qty)

    class Meta:
        db_table = 'out_waybill_details'
        verbose_name_plural = 'Детали накладной'
        unique_together = ('waybill', 'article')

class Payments(models.Model):
    id = models.AutoField(primary_key=True)
    payee = models.ForeignKey(Current_accounts, db_column='payee', related_name='payee.payments_set',
                              verbose_name='Получатель')
    payer = models.ForeignKey(Current_accounts, db_column='payer', related_name='payer.payments_set',
                              verbose_name='Плательщик')
    pay_date = models.DateField(verbose_name='Дата')
    pay_order = models.CharField(max_length=20, blank=True, verbose_name='№ Квит.')
    sum = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='Сумма')
    note = models.CharField(max_length=30, blank=True, verbose_name='Примечание')

    def __unicode__(self):
        return u'%s %s %s %s %s %s %s' % (self.id, self.payee, self.payer, self.pay_date,
            self.pay_order, self.sum, self.note)

    class Meta:
        db_table = 'payments'
        verbose_name_plural = 'Платежи'

class Pay_details(models.Model):
    invoice = models.ForeignKey(Invoices, db_column='inv_id', verbose_name='Заказ')
    payment = models.ForeignKey(Payments, db_column='payment_id', verbose_name='Платеж')
    sum = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='Сумма')

    def __unicode__(self):
        return u'%s %s %s' % (self.invoice, self.payment, self.sum)

    class Meta:
        db_table = 'pay_details'
        verbose_name_plural = 'Оплата заказа'
        unique_together = ('invoice', 'payment')

class Payed_waybills(models.Model):
    waybill = models.ForeignKey(Out_waybills, db_column='wbl_id', verbose_name='Накладная')
    payment = models.ForeignKey(Payments, db_column='payment_id', verbose_name='Платеж')
    sum = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='Сумма')

    def __unicode__(self):
        return u'%s %s %s' % (self.waybill, self.payment, self.sum)

    class Meta:
        db_table = 'payed_waybills'
        verbose_name_plural = 'Оплата накладной'
        unique_together = ('waybill', 'payment')

class Waybill_types(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=10, verbose_name='Тип')

    def __unicode__(self):
        return u'%s %s' % (self.id, self.type)

    class Meta:
        db_table = 'waybill_types'
        verbose_name_plural = 'Типы_накладной'

class In_waybills(models.Model):
    id = models.AutoField(primary_key=True)
    store = models.ForeignKey(Stores, db_column='store_id', verbose_name='Склад')
    sypplier = models.ForeignKey(Contractors, db_column='supplier', related_name='sypplier.inwaybills_set',
                                 verbose_name='Поставщик')
    recipient = models.ForeignKey(Contractors, db_column='recipient', related_name='recipient.inwaybills_set',
                                  verbose_name='Получатель')
    date = models.DateField(verbose_name='Дата')
    doc_no = models.CharField(max_length=20, blank=True, verbose_name='№ Док.')
    note = models.CharField(max_length=30, blank=True, verbose_name='Примечание')
    doc_type = models.ForeignKey(Waybill_types, db_column='doc_type')
    doc_date = models.DateField(null=True, verbose_name='Дата Док.')
    sum = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='Сумма')
    VAT = models.SmallIntegerField(default=0, verbose_name='НДС')
    VAT_val = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='СуммаНДС')
    total = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='Итого')
    except_sum = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='В затраты')
    employee = models.ForeignKey(Employees, null=True, db_column='emp_id', verbose_name='Сотрудник')
    report = models.ForeignKey(Imprest_reports, null=True, db_column='report_id', verbose_name='Отчет')
    declaration_no = models.CharField(max_length=20, blank=True, verbose_name='№ Декларации')

    def __unicode__(self):
        return u'%s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s' % \
               (self.id, self.store, self.sypplier, self.recipient, self.date, self.doc_no,
                self.note, self.doc_type, self.doc_date, self.sum, self.VAT, self.VAT_val,
                self.total, self.except_sum, self.employee, self.report, self.declaration_no)

    class Meta:
        db_table = 'in_waybills'
        verbose_name_plural = 'Вх.Накладные'

class In_waybill_details(models.Model):
    inwaybill = models.ForeignKey(In_waybills, db_column='inwbl_id', verbose_name='Накладная')
    product = models.ForeignKey(Products, db_column='prod_id', verbose_name='Товар')
    qty = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Кол-во')
    price = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='Цена')
    sum = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='Сумма')

    def __unicode__(self):
        return u'%s %s %s %s %s' % (self.inwaybill, self.product, self.qty, self.price, self.sum)

    class Meta:
        db_table = 'in_waybill_details'
        verbose_name_plural = 'Детали вх.накладной'
        unique_together = ('inwaybill', 'product')

class Factures(models.Model):
    id = models.AutoField(primary_key=True)
    sypplier = models.ForeignKey(Contractors, db_column='sypplier', related_name='sypplier.factures_set')
    recipient = models.ForeignKey(Contractors, db_column='recipient', related_name='recipient.factures_set')
    doc_no = models.CharField(max_length=20, verbose_name='№ Док.')
    doc_date = models.DateField(verbose_name='Дата Док.')
    sum = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='Сумма')
    VAT = models.SmallIntegerField(default=0, verbose_name='НДС')
    VAT_val = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='СуммаНДС')
    total = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='Итого')

    def __unicode__(self):
        return u'%s %s %s %s %s %s %s %s %s)' %\
               (self.id, self.sypplier, self.recipient, self.doc_no,
                self.doc_date, self.sum, self.VAT, self.VAT_val, self.total)

    class Meta:
        db_table = 'factures'
        verbose_name_plural = 'Счета-Фактуры'

class Payment_orders_type(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)

    def __unicode__(self):
        return u'%s %s' % (self.id, self.name)

    class Meta:
        db_table = 'payment_orders_type'
        verbose_name_plural = 'Типы пп'
class Payment_orders_method(models.Model):
    id = models.AutoField(primary_key=True)
    method = models.CharField(max_length=10, verbose_name='Вид')

    def __unicode__(self):
        return u'%s %s' % (self.id, self.method)

    class Meta:
        db_table = 'payment_orders_method'
        verbose_name_plural = 'Выды платежа'

class Bills(models.Model):
    id = models.AutoField(primary_key=True)
    bill_no = models.CharField(max_length=10, verbose_name='№ Счета')
    payee = models.ForeignKey(Current_accounts, verbose_name='Получатель', db_column='payee', related_name='payee.bills_set')
    payer = models.ForeignKey(Current_accounts, verbose_name='Плательщик', db_column='payer', related_name='payer.bills_set')
    nomination = models.CharField(max_length=50, verbose_name='Назначение')
    sum = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='Сумма')

    def __unicode__(self):
        return u'%s %s %s %s %s %s' %\
               (self.id, self.bill_no, self.payer, self.payee, self.sum, self.nomination)

    class Meta:
        db_table = 'bills'
        verbose_name_plural = 'Счета на оплату'

class Payment_orders(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.ForeignKey(Payment_orders_type, verbose_name='Тип пп', db_column='type_id')
    po_num = models.SmallIntegerField(verbose_name='№ пп')
    date = models.DateField(verbose_name='Дата')
    method = models.ForeignKey(Payment_orders_method, verbose_name='Вид пл', db_column='method_id')
    payee = models.ForeignKey(Current_accounts, verbose_name='Получатель', db_column='payee', related_name='payee.payment_orders_set')
    payer = models.ForeignKey(Current_accounts, verbose_name='Плательщик', db_column='payer', related_name='payer.payment_orders_set')
    nomination = models.CharField(max_length=50, verbose_name='Назначение')
    sum = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='Сумма')
    VAT = models.SmallIntegerField(default=0, verbose_name='НДС')
    total = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='Итого')
    f101 = models.CharField(max_length=2, blank=True, verbose_name='Статус')
    f104 = models.CharField(max_length=20, blank=True, verbose_name='КБК')
    f105 = models.CharField(max_length=13, blank=True, verbose_name='ОКАТО')
    f106 = models.CharField(max_length=2, blank=True, verbose_name='Осн.пл.')
    f107 = models.CharField(max_length=10, blank=True, verbose_name='Нал.пер.')
    f108 = models.CharField(max_length=10, blank=True, verbose_name='№ док.')
    f109 = models.DateField(null=True, verbose_name='Дата. док')
    f110 = models.CharField(max_length=2, blank=True, verbose_name='Тип пл.')
    sent = models.DateField(null=True, verbose_name='Пер.в КБ')
    held = models.DateField(null=True, verbose_name='Проведена')
    priority = models.CharField(max_length=1, blank=True, verbose_name='Очер.пл.')
    maturity = models.DateField(null=True, verbose_name='Срок пл.')
    bill = models.ForeignKey(Bills, db_column='bill_id', verbose_name='Счет')
    check_num = models.CharField(max_length=50, blank=True, verbose_name='№ Чека')

    def __unicode__(self):
        return u'%s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s' %\
               (self.id, self.type, self.po_num, self.date, self.method,
                self.payer, self.payee, self.nomination, self.sum, self.VAT,
                self.total, self.f101, self.f104, self.f105, self.f106, self.f107, self.f108,
                self.f109, self.f110, self.sent, self.held, self.priority, self.maturity,
                self.bill, self.check_num)

    class Meta:
        db_table = 'payment_orders'
        verbose_name_plural = 'Платежные поручения'


class Payed_inwaybills(models.Model):
    p_order = models.ForeignKey(Payment_orders, db_column='po_id', verbose_name='ПП')
    inwaybill = models.ForeignKey(In_waybills, db_column='inwbl_id', verbose_name='Накладная')
    sum = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='Сумма')

    def __unicode__(self):
        return u'%s %s %s' % (self.p_order, self.inwaybill, self.sum)

    class Meta:
        db_table = 'payed_inwaybills'
        verbose_name_plural = 'Накладне к пп'
        unique_together = ('p_order', 'inwaybill')

class Payed_factures(models.Model):
    p_order = models.ForeignKey(Payment_orders, db_column='po_id', verbose_name='ПП')
    facture = models.ForeignKey(Factures, db_column='facture_id', verbose_name='С-Ф')
    sum = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='Сумма')

    def __unicode__(self):
        return u'%s %s %s' % (self.p_order, self.facture, self.sum)

    class Meta:
        db_table = 'payed_factures'
        verbose_name_plural = 'Сч.-Фактуры к пп'
        unique_together = ('p_order', 'facture')

class Parts(models.Model):
    id = models.AutoField(primary_key=True)
    part = models.CharField(max_length=10, verbose_name='Деталь')
    type = models.ForeignKey(Prod_types3, db_column='type_id', verbose_name='Тип')

    def __unicode__(self):
        return u'%s %s %s' % (self.id, self.part, self.type)

    class Meta:
        db_table = 'parts'
        verbose_name_plural = 'Детали'


class Parts_spec(models.Model):
    component = models.ForeignKey(Components, db_column='comp_id', verbose_name='Изделие')
    part = models.ForeignKey(Parts, db_column='part_id', verbose_name='Деталь')
    height = models.SmallIntegerField(verbose_name='Высота')
    width = models.SmallIntegerField(verbose_name='Ширина')
    material = models.ForeignKey(Products, verbose_name='Материал', db_column='material', related_name='material.parts_spec_set')
    edge1h = models.ForeignKey(Products, verbose_name='Кромка1', db_column='edge1h', related_name='edge1h.parts_spec_set')
    edge2h = models.ForeignKey(Products, verbose_name='Кромка2', db_column='edge2h', related_name='edge2h.parts_spec_set')
    edge1w = models.ForeignKey(Products, verbose_name='Кромка3', db_column='edge1w', related_name='edge1w.parts_spec_set')
    edge2w = models.ForeignKey(Products, verbose_name='Кромка4', db_column='edge2w', related_name='edge2w.parts_spec_set')
    qty = models.SmallIntegerField(verbose_name='Кол-во')
    hole = models.SmallIntegerField(verbose_name='Отверстия')
    note = models.CharField(max_length=20, blank=True, verbose_name='Примечания')

    def __unicode__(self):
        return u'%s %s %s %s %s %s %s %s %s %s %s %s' %\
               (self.component, self.part, self.height, self.width, self.material,
                self.edge1h, self.edge2h, self.edge1w, self.edge2w, self.qty, self.hole,
                self.note)

    class Meta:
        db_table = 'parts_spec'
        verbose_name_plural = 'Деталировка'

class Materials(models.Model):
    component = models.ForeignKey(Components, db_column='comp_id', verbose_name='Изделие')
    product = models.ForeignKey(Products, db_column='prod_id', verbose_name='Материал')
    parameters = models.CharField(max_length=20, blank=True, verbose_name='Параметры')
    qty = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Кол-во')
    price = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='Цена')
    sum = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='Сумма')
    material_no = models.SmallIntegerField(null=True, verbose_name='№ мат.')

    def __unicode__(self):
        return u'%s %s %s %s %s %s %s' % \
               (self.component, self.product, self.parameters, self.qty, self.price, self.sum,
                   self.material_no)

    class Meta:
        db_table = 'materials'
        verbose_name_plural = 'Материалы'
        unique_together = ('component', 'product')

class Parts_lib(models.Model):
    product = models.ForeignKey(Products, db_column='prod_id', verbose_name='Изделие')
    part = models.ForeignKey(Parts, db_column='part_id', verbose_name='Деталь')
    height = models.SmallIntegerField(verbose_name='Высота')
    width = models.SmallIntegerField(verbose_name='Ширина')
    material = models.ForeignKey(Products, verbose_name='Материал', db_column='material', related_name='material.parts_lib_set')
    edge1h = models.ForeignKey(Products, verbose_name='Кромка1', db_column='edge1h', related_name='edge1h.parts_lib_set')
    edge2h = models.ForeignKey(Products, verbose_name='Кромка2', db_column='edge2h', related_name='edge2h.parts_lib_set')
    edge1w = models.ForeignKey(Products, verbose_name='Кромка3', db_column='edge1w', related_name='edge1w.parts_lib_set')
    edge2w = models.ForeignKey(Products, verbose_name='Кромка4', db_column='edge2w', related_name='edge2w.parts_lib_set')
    qty = models.SmallIntegerField(verbose_name='Кол-во')
    hole = models.SmallIntegerField(verbose_name='Отверстия')
    note = models.CharField(max_length=20, blank=True, verbose_name='Примечания')

    def __unicode__(self):
        return u'%s %s %s %s %s %s %s %s %s %s %s %s' %\
               (self.product, self.part, self.height, self.width, self.material,
                self.edge1h, self.edge2h, self.edge1w, self.edge2w, self.qty, self.hole,
                self.note)

    class Meta:
        db_table = 'parts_lib'
        verbose_name_plural = 'Библиотека деталей'

class Materials_lib(models.Model):
    product = models.ForeignKey(Products, db_column='prod_id', related_name='prod_id.materials_lib_set',
                                verbose_name='Изделие')
    material = models.ForeignKey(Products, db_column='material', related_name='material.materials_lib_set',
                                 verbose_name='Материал')
    parameters = models.CharField(max_length=20, blank=True, verbose_name='Параметры')
    qty = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Кол-во')
    material_no = models.SmallIntegerField(null=True, verbose_name='№ мат.')

    def __unicode__(self):
        return u'%s %s %s %s %s' % \
               (self.product, self.material, self.parameters, self.qty,
                   self.material_no)

    class Meta:
        db_table = 'materials_lib'
        verbose_name_plural = 'Библиотека материалов'
        unique_together = ('product','material')
		

class Prod_lunch(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(verbose_name='Дата')
    invoice = models.ForeignKey(Invoices, db_column='inv_id', verbose_name='Заказ')
    note = models.CharField(max_length=20, blank=True, verbose_name='Примечания')

    def __unicode__(self):
        return u'%s %s %s %s' % (self.id, self.date, self.invoice, self.note)

    class Meta:
        db_table = 'prod_lunch'
        verbose_name_plural = 'Запуск'


class Prod_perf(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(verbose_name='Дата')
    invoice = models.ForeignKey(Invoices, db_column='inv_id', verbose_name='Заказ')
    note = models.CharField(max_length=20, blank=True, verbose_name='Примечания')

    def __unicode__(self):
        return u'%s %s %s %s' % (self.id, self.date, self.invoice, self.note)

    class Meta:
        db_table = 'prod_perf'
        verbose_name_plural = 'Изготовление'

class Prod_ship(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(verbose_name='Дата')
    invoice = models.ForeignKey(Invoices, db_column='inv_id', verbose_name='Заказ')
    note = models.CharField(max_length=20, blank=True, verbose_name='Примечания')

    def __unicode__(self):
        return u'%s %s %s %s' % (self.id, self.date, self.invoice, self.note)

    class Meta:
        db_table = 'prod_ship'
        verbose_name_plural = 'Отгрузка'

class Lunch_details(models.Model):
    lunch = models.ForeignKey(Prod_lunch, db_column='lunch_id', verbose_name='Запуск')
    article = models.ForeignKey(Articles, db_column='art_id', verbose_name='Позиция')
    qty = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Кол-во')

    def __unicode__(self):
        return u'%s %s %s' % (self.lunch, self.article, self.qty)

    class Meta:
        db_table = 'lunch_details'
        verbose_name_plural = 'Детали запуска'

class Perf_details(models.Model):
    perfection = models.ForeignKey(Prod_perf, db_column='perf_id', verbose_name='Изготовление')
    article = models.ForeignKey(Articles, db_column='art_id', verbose_name='Позиция')
    qty = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Кол-во')

    def __unicode__(self):
        return u'%s %s %s' % (self.perfection, self.article, self.qty)

    class Meta:
        db_table = 'perf_details'
        verbose_name_plural = 'Детали изготовления'

class Ship_details(models.Model):
    ship = models.ForeignKey(Prod_ship, db_column='ship_id', verbose_name='Отгрузка')
    article = models.ForeignKey(Articles, db_column='art_id', verbose_name='Позиция')
    qty = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Кол-во')

    def __unicode__(self):
        return u'%s %s %s' % (self.ship, self.article, self.qty)

    class Meta:
        db_table = 'ship_details'
        verbose_name_plural = 'Детали отгрузки'