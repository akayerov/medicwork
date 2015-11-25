# -*- coding: utf-8 -*-
'''
@author: a_kayerov
'''
from django.db.models import Sum
from random import random
import openpyxl
from openpyxl.styles import Font
from openpyxl.styles import Border
from openpyxl import load_workbook
from openpyxl.workbook import Workbook

from medicament.oper_with_base import create_new_report, save_doc, get_name, get_period_namef, get_region_name, get_name_input
from medicament.models import Document, Doc_type, Hosp, Period, Role, Region, Comment, Doc_Hosp, Doc1, Doc2, Rows

from medicament.modelsDoc3 import Doc3, Doc3Tab1000, Doc3Tab2000, Doc3Tab3000, Doc3Tab4000, Doc3Tab5000, Doc3Tab5001, Doc3Tab6000, Doc3Tab7000

from _datetime import datetime
from openpyxl.styles.borders import Side, BORDER_MEDIUM


def create_report_form3(periodInt, datef):
    ''' Создание новых документов (в новом периоде)
        Возвращает True, если добавление записей прошло успешно
        В противном случае возвращает False
        copy_fields_formX - функция начального заполнения '''
    
    # Более сложная функция создания новых отчетов - дополнительно создаются записи в подчиненных таблицах
    type = 3
    period = Period.objects.get(pk=periodInt)
    period_prev = period.prev
    num_rec = Doc3.objects.filter(period = period).count()     
    if num_rec > 0:
        return False
    for dh in Doc_Hosp.objects.filter(doc_type = type):
        odoc = Doc3.objects.create(hosp=dh.hosp, period=period, datef=datef)
        # если предыдущий период есть, попробуем заполнить документ из предыдущего
        if period_prev:       
            doc_prevList = Doc3.objects.filter(period = period_prev, hosp = dh.hosp, status='F')
            if doc_prevList:
                doc_prev = doc_prevList[0]
                copy_fields_form3(doc_prev, odoc)
                odoc.save()
                create_tab(type,odoc, doc_prev)     # создаем табличные части для нового отчета 4 - код мониторинга
            else:     
                create_tab(type,odoc)     # создаем табличные части для нового отчета 4 - код мониторинга
        else:     
            create_tab(type,odoc)     # создаем табличные части для нового отчета 4 - код мониторинга

                
#    return create_new_report(3,Doc3,periodInt,datef, copy_fields_form3)
    return True

def create_tab(type, odoc, pdoc = None):
    ''' создатим табличные записи для нового отчета '''
    
    row = Rows.objects.filter(type  = type, table = 'таб1000')
    for r in row:
        otab1000 = Doc3Tab1000.objects.create(doc=odoc, row=r )
        if pdoc:
            ptab1000 = Doc3Tab1000.objects.get(doc=pdoc, row=r )
            if ptab1000:
                otab1000.c1 = ptab1000.c1
                otab1000.c2 = ptab1000.c2
                otab1000.c3 = ptab1000.c3
                otab1000.c4 = ptab1000.c4
                otab1000.c5 = ptab1000.c5
                otab1000.c6 = ptab1000.c6
                otab1000.c7 = ptab1000.c7
                otab1000.c8 = ptab1000.c8
                otab1000.c9 = ptab1000.c9
                otab1000.c10 = ptab1000.c10
                otab1000.c11 = ptab1000.c11
                otab1000.c12 = ptab1000.c12
        otab1000.save()
    row = Rows.objects.filter(type  = type, table = 'таб2000')
    for r in row:
        otab2000 = Doc3Tab2000.objects.create(doc=odoc, row=r )
        if pdoc:
            ptab2000 = Doc3Tab2000.objects.get(doc=pdoc, row=r )
            if ptab2000:
                otab2000.c1 = ptab2000.c1
                otab2000.c2 = ptab2000.c2
                otab2000.c3 = ptab2000.c3
                otab2000.c4 = ptab2000.c4
        otab2000.save()
    row = Rows.objects.filter(type  = type, table = 'таб3000')
    for r in row:
        otab3000 = Doc3Tab3000.objects.create(doc=odoc, row=r )
        if pdoc:
            ptab3000 = Doc3Tab3000.objects.get(doc=pdoc, row=r )
            if ptab3000:
                otab3000.c1 = ptab3000.c1
                otab3000.c2 = ptab3000.c2
                otab3000.c3 = ptab3000.c3
                otab3000.c4 = ptab3000.c4
                otab3000.c5 = ptab3000.c5
        otab3000.save()
    row = Rows.objects.filter(type  = type, table = 'таб4000')
    for r in row:
        otab4000 = Doc3Tab4000.objects.create(doc=odoc, row=r )
        if pdoc:
            ptab4000 = Doc3Tab4000.objects.get(doc=pdoc, row=r )
            if ptab4000:
                otab4000.c1 = ptab4000.c1
                otab4000.c2 = ptab4000.c2
                otab4000.c3 = ptab4000.c3
                otab4000.c5 = ptab4000.c5
                otab4000.c6 = ptab4000.c6
                otab4000.c7 = ptab4000.c7
        otab4000.save()
    row = Rows.objects.filter(type  = type, table = 'таб5000')
    for r in row:
        otab5000 = Doc3Tab5000.objects.create(doc=odoc, row=r )
        if pdoc:
            ptab5000 = Doc3Tab5000.objects.get(doc=pdoc, row=r )
            if ptab5000:
                otab5000.c1 = ptab5000.c1
                otab5000.c2 = ptab5000.c2
                otab5000.c3 = ptab5000.c3
                otab5000.c5 = ptab5000.c5
                otab5000.c6 = ptab5000.c6
                otab5000.c7 = ptab5000.c7
                otab5000.c13 = ptab5000.c13
        otab5000.save()
    row = Rows.objects.filter(type  = type, table = 'таб5001')
    for r in row:
        otab5001 = Doc3Tab5001.objects.create(doc=odoc, row=r )
        if pdoc:
            ptab5001 = Doc3Tab5001.objects.get(doc=pdoc, row=r )
            if ptab5001:
                otab5001.c1 = ptab5001.c1
                otab5001.c2 = ptab5001.c2
                otab5001.c3 = ptab5001.c3
                otab5001.c5 = ptab5001.c5
                otab5001.c6 = ptab5001.c6
                otab5001.c7 = ptab5001.c7
                otab5001.c13 = ptab5001.c13
        otab5001.save()
    row = Rows.objects.filter(type  = type, table = 'таб6000')
    for r in row:
        otab6000 = Doc3Tab6000.objects.create(doc=odoc, row=r )
        if pdoc:
            ptab6000 = Doc3Tab6000.objects.get(doc=pdoc, row=r )
            if ptab6000:
                otab6000.c1 = ptab6000.c1
                otab6000.c2 = ptab6000.c2
                otab6000.c3 = ptab6000.c3
                otab6000.c5 = ptab6000.c5
                otab6000.c6 = ptab6000.c6
                otab6000.c7 = ptab6000.c7
                otab6000.c13 = ptab6000.c13
        otab6000.save()
    row = Rows.objects.filter(type  = type, table = 'таб7000')
    for r in row:
        otab7000 = Doc3Tab7000.objects.create(doc=odoc, row=r )
        if pdoc:
            ptab7000 = Doc3Tab7000.objects.get(doc=pdoc, row=r )
            if ptab7000:
                otab7000.c1 = ptab7000.c1
                otab7000.c2 = ptab7000.c2
                otab7000.c3 = ptab7000.c3
                otab7000.c4 = ptab7000.c4
                otab7000.c5 = ptab7000.c5
                otab7000.c6 = ptab7000.c6
        otab7000.save()

def save_doc_form3(request, type, id_doc, mode_comment):
    ''' Сохранить запись Document + комментарий с новой записью в комментрии с действием пользователя
        Установить собственый параментрв DOCx,set_fields_formx, is_valid_formx
    ''' 
    return save_doc(Doc3,set_fields_form3, is_valid_form3, request, type, id_doc, mode_comment)

def copy_fields_form3(ds, dd):
    dd.t3001 = ds.t3001
    dd.t4001_r1 = ds.t4001_r1
    dd.t4001_r2 = ds.t4001_r2
    dd.t4002_r1 = ds.t4002_r1
    dd.t4002_r2 = ds.t4002_r2
    dd.t7001 = ds.t7001
    dd.t7002 = ds.t7002
    dd.t7003 = ds.t7003
    dd.t7004 = ds.t7004
    dd.t7004_r1 = ds.t7004_r1
    dd.t7004_r2 = ds.t7004_r2
    dd.t7004_r3 = ds.t7004_r3
    dd.t7004_r4 = ds.t7004_r4
    dd.t7004_r5 = ds.t7004_r5
    dd.t7004_r6 = ds.t7004_r6
    dd.t7004_r7 = ds.t7004_r7
    dd.t7004_r8 = ds.t7004_r8
    dd.t7005 = ds.t7005
    dd.t7006 = ds.t7006
    dd.t7006_r1 = ds.t7006_r1
    dd.t7007 = ds.t7007
    dd.t7008 = ds.t7008
    dd.t7009 = ds.t7009
    dd.t7010 = ds.t7010
    dd.t7011 = ds.t7011
    dd.t7012 = ds.t7012
  

def set_fields_form3(request, doc):
    ''' Заполнение полей модели данными формы . 
        Для каждой формы
    '''
    if 'button_save' or 'button_send_control'  in request.POST:
        type = 3
    # поля формы (вне табличных частей) 
        doc.t3001 = request.POST['t3001']
        
        doc.t4001_r1 = request.POST['t4001_r1']
        doc.t4001_r2 = request.POST['t4001_r2']
        
        doc.t4002_r1 = request.POST['t4002_r1']
        doc.t4002_r2 = request.POST['t4002_r2']
        
        doc.t7001 = request.POST['t7001']
        doc.t7002 = request.POST['t7002']
        doc.t7003 = request.POST['t7003']
        doc.t7004 = request.POST['t7004']
        doc.t7004_r1 = request.POST['t7004_r1']
        doc.t7004_r2 = request.POST['t7004_r2']
        doc.t7004_r3 = request.POST['t7004_r3']
        doc.t7004_r4 = request.POST['t7004_r4']
        doc.t7004_r5 = request.POST['t7004_r5']
        doc.t7004_r6 = request.POST['t7004_r6']
        doc.t7004_r7 = request.POST['t7004_r7']
        doc.t7004_r8 = request.POST['t7004_r8'] 
        doc.t7005 = request.POST['t7005']
        doc.t7006 = request.POST['t7006']
        doc.t7006_r1 = request.POST['t7006_r1']
        doc.t7007 = request.POST['t7007']
        doc.t7008 = request.POST['t7008']
        doc.t7009 = request.POST['t7009']
        doc.t7010 = request.POST['t7010']
        doc.t7011 = request.POST['t7011']
        doc.t7012 = request.POST['t7012']
    
    # Табличные части
    # Таблица 1000
        table = 't1000'    
        tabrs = Doc3Tab1000.objects.filter(doc=doc)
        for tab in tabrs: 
            tab.c1 = request.POST[get_name_input(table,tab.row.id,"c5")] + request.POST[get_name_input(table,tab.row.id,"c9")]
            tab.c2 = request.POST[get_name_input(table,tab.row.id,"c6")] + request.POST[get_name_input(table,tab.row.id,"c10")]
            tab.c3 = request.POST[get_name_input(table,tab.row.id,"c7")] + request.POST[get_name_input(table,tab.row.id,"c11")]
            tab.c4 = request.POST[get_name_input(table,tab.row.id,"c8")] + request.POST[get_name_input(table,tab.row.id,"c12")]
			
            tab.c5 = request.POST[get_name_input(table,tab.row.id,"c5")]
            tab.c6 = request.POST[get_name_input(table,tab.row.id,"c6")]
            tab.c7 = request.POST[get_name_input(table,tab.row.id,"c7")]
            tab.c8 = request.POST[get_name_input(table,tab.row.id,"c8")]
			
            tab.c9 = request.POST[get_name_input(table,tab.row.id,"c9")]
            tab.c10 = request.POST[get_name_input(table,tab.row.id,"c10")]
            tab.c11 = request.POST[get_name_input(table,tab.row.id,"c11")]
            tab.c12 = request.POST[get_name_input(table,tab.row.id,"c12")]
            tab.save()
    # Таблица 2000
        table = 't2000'    
        tabrs = Doc3Tab2000.objects.filter(doc=doc)
        for tab in tabrs: 
            tab.c1 = request.POST[get_name_input(table,tab.row.id,"c1")]
            if tab.row.id != 4 and tab.row.id != 23:
                tab.c2 = request.POST[get_name_input(table,tab.row.id,"c2")]
                tab.c3 = request.POST[get_name_input(table,tab.row.id,"c3")]
            tab.c4 = request.POST[get_name_input(table,tab.row.id,"c4")]
            tab.save()
    # Таблица 3000
        table = 't3000'    
        tabrs = Doc3Tab3000.objects.filter(doc=doc)
        for tab in tabrs: 
            tab.c1 = request.POST[get_name_input(table,tab.row.id,"c1")]
            tab.c2 = request.POST[get_name_input(table,tab.row.id,"c2")]
            tab.c3 = request.POST[get_name_input(table,tab.row.id,"c3")]
            tab.c4 = request.POST[get_name_input(table,tab.row.id,"c4")]
            if tab.row.id != 37 and tab.row.id != 38:
                tab.c5 = request.POST[get_name_input(table,tab.row.id,"c5")]
            tab.save()
    # Таблица 4000
        table = 't4000'    
        tabrs = Doc3Tab4000.objects.filter(doc=doc)
        for tab in tabrs: 
            tab.c1 = request.POST[get_name_input(table,tab.row.id,"c1")]
            tab.c2 = request.POST[get_name_input(table,tab.row.id,"c2")]
            tab.c3 = request.POST[get_name_input(table,tab.row.id,"c3")]
            tab.c5 = request.POST[get_name_input(table,tab.row.id,"c5")]
            tab.c6 = request.POST[get_name_input(table,tab.row.id,"c6")]
            tab.c7 = request.POST[get_name_input(table,tab.row.id,"c7")]
            tab.save()
    # Таблица 5000
        table = 't5000'    
        tabrs = Doc3Tab5000.objects.filter(doc=doc)
        for tab in tabrs: 
            tab.c1 = request.POST[get_name_input(table,tab.row.id,"c1")]
            tab.c2 = request.POST[get_name_input(table,tab.row.id,"c2")]
            tab.c3 = request.POST[get_name_input(table,tab.row.id,"c3")]
            tab.c5 = request.POST[get_name_input(table,tab.row.id,"c5")]
            tab.c6 = request.POST[get_name_input(table,tab.row.id,"c6")]
            tab.c7 = request.POST[get_name_input(table,tab.row.id,"c7")]
            tab.c13 = request.POST[get_name_input(table,tab.row.id,"c13")]
            tab.save()
    # Таблица 5001
        table = 't5001'    
        tabrs = Doc3Tab5001.objects.filter(doc=doc)
        for tab in tabrs: 
            tab.c1 = request.POST[get_name_input(table,tab.row.id,"c1")]
            tab.c2 = request.POST[get_name_input(table,tab.row.id,"c2")]
            tab.c3 = request.POST[get_name_input(table,tab.row.id,"c3")]
            tab.c5 = request.POST[get_name_input(table,tab.row.id,"c5")]
            tab.c6 = request.POST[get_name_input(table,tab.row.id,"c6")]
            tab.c7 = request.POST[get_name_input(table,tab.row.id,"c7")]
            tab.c13 = request.POST[get_name_input(table,tab.row.id,"c13")]
            tab.save()
    # Таблица 6000
        table = 't6000'    
        tabrs = Doc3Tab6000.objects.filter(doc=doc)
        for tab in tabrs: 
            tab.c1 = request.POST[get_name_input(table,tab.row.id,"c1")]
            tab.c2 = request.POST[get_name_input(table,tab.row.id,"c2")]
            tab.c3 = request.POST[get_name_input(table,tab.row.id,"c3")]
            tab.c5 = request.POST[get_name_input(table,tab.row.id,"c5")]
            tab.c6 = request.POST[get_name_input(table,tab.row.id,"c6")]
            tab.c7 = request.POST[get_name_input(table,tab.row.id,"c7")]
            tab.c13 = request.POST[get_name_input(table,tab.row.id,"c13")]
            tab.save()
    # Таблица 7000
        table = 't7000'    
        tabrs = Doc3Tab7000.objects.filter(doc=doc)
        for tab in tabrs: 
            tab.c1 = request.POST[get_name_input(table,tab.row.id,"c1")]
            tab.c2 = request.POST[get_name_input(table,tab.row.id,"c2")]
            tab.c3 = request.POST[get_name_input(table,tab.row.id,"c3")]
            tab.c4 = request.POST[get_name_input(table,tab.row.id,"c4")]
            tab.c5 = request.POST[get_name_input(table,tab.row.id,"c5")]
            tab.c6 = request.POST[get_name_input(table,tab.row.id,"c6")]
            tab.save()

def is_valid_form3(dd, ds):
    ''' Проверка заполнения формы на корректность 
        dd - текущий документ
        ds - документ предыдущего периода
        Все поля кроме 7011 должны быть >= соответствующего значения предыдущего периода
    print(dd)
    print(ds)
    if int(dd.t3001) < int(ds.t3001):
        ret = [False,'Ошибка 3001.']
        return ret
    '''
    ret = [True,'OK']
    return ret

def calc_sum_form3(doc):
    ''' Возвращает Суммы данных отчетов
        В отличие от предыдущих отчетов кроме основной DOC используются дополнительные таблицы 
    '''
#   Суммирование по основной части документа
    period = doc[0].period
    aq1= doc.aggregate(Sum('t3001'),Sum('t4001_r1'),Sum('t4001_r2'),Sum('t4002_r1'),Sum('t4002_r2'),Sum('t7001'),\
                       Sum('t7002'),Sum('t7003'),Sum('t7004'),Sum('t7004_r1'),Sum('t7004_r2'),\
                       Sum('t7004_r3'),Sum('t7004_r4'),Sum('t7004_r5'),Sum('t7004_r6'),Sum('t7004_r7'),\
                       Sum('t7004_r8'),Sum('t7005'),Sum('t7006'),Sum('t7006_r1'),Sum('t7007'),\
                       Sum('t7008'),Sum('t7009'),Sum('t7010'),Sum('t7011'),Sum('t7012')
         )
    s1 = [aq1['t3001__sum'],aq1['t4001_r1__sum'],aq1['t4001_r2__sum'],aq1['t4002_r1__sum'],aq1['t4002_r2__sum'],aq1['t7001__sum'],\
          aq1['t7002__sum'],aq1['t7003__sum'],aq1['t7004__sum'],aq1['t7004_r1__sum'],aq1['t7004_r2__sum'],\
          aq1['t7004_r3__sum'],aq1['t7004_r4__sum'],aq1['t7004_r5__sum'],aq1['t7004_r6__sum'],aq1['t7004_r7__sum'],\
          aq1['t7004_r8__sum'],aq1['t7005__sum'],aq1['t7006__sum'],aq1['t7006_r1__sum'],aq1['t7007__sum'],\
          aq1['t7008__sum'],aq1['t7009__sum'],aq1['t7010__sum'],aq1['t7011__sum'],aq1['t7012__sum']
        ]

#   суммирование табличных частей документа
#   ТАБЛИЦА 1000
    row = Rows.objects.filter(type  = 3, table = 'таб1000')
    s1000 = []
    for r in row:
        tab1000 = Doc3Tab1000.objects.filter(doc = doc, doc__period=period, row=r )
        aq1000 = tab1000.aggregate(Sum('c1'),Sum('c2'),Sum('c3'),Sum('c4'),Sum('c5'),\
                                   Sum('c6'),Sum('c7'),Sum('c8'),Sum('c9'),Sum('c10'),\
                                   Sum('c11'),Sum('c12'))
        obj = [tab1000[0].row,aq1000['c1__sum'],aq1000['c2__sum'],aq1000['c3__sum'],aq1000['c4__sum'],\
               aq1000['c5__sum'],aq1000['c6__sum'],aq1000['c7__sum'],aq1000['c8__sum'],aq1000['c9__sum'],\
               aq1000['c10__sum'],aq1000['c11__sum'],aq1000['c12__sum']]
        s1000.append(obj) 
    
#   ТАБЛИЦА 2000
    row = Rows.objects.filter(type  = 3, table = 'таб2000')
    s2000 = []
    for r in row:
        tab2000 = Doc3Tab2000.objects.filter(doc = doc, doc__period=period, row=r )
        aq2000 = tab2000.aggregate(Sum('c1'),Sum('c2'),Sum('c3'),Sum('c4'))
        obj = [tab2000[0].row,aq2000['c1__sum'],aq2000['c2__sum'],aq2000['c3__sum'],aq2000['c4__sum']]
        s2000.append(obj)
#   ТАБЛИЦА 3000
    row = Rows.objects.filter(type  = 3, table = 'таб3000')
    s3000 = []
    for r in row:
        tab3000 = Doc3Tab3000.objects.filter(doc = doc, doc__period=period, row=r )
        aq3000 = tab3000.aggregate(Sum('c1'),Sum('c2'),Sum('c3'),Sum('c4'),Sum('c5'))
        obj = [tab3000[0].row,aq3000['c1__sum'],aq3000['c2__sum'],aq3000['c3__sum'],aq3000['c4__sum'],aq3000['c5__sum']]
        s3000.append(obj)
#   ТАБЛИЦА 4000
    row = Rows.objects.filter(type  = 3, table = 'таб4000')
    s4000 = []
    for r in row:
        tab4000 = Doc3Tab4000.objects.filter(doc = doc, doc__period=period, row=r )
        aq4000 = tab4000.aggregate(Sum('c1'),Sum('c2'),Sum('c3'),Sum('c5'),Sum('c6'),Sum('c7'))
        obj = [tab4000[0].row,aq4000['c1__sum'],aq4000['c2__sum'],aq4000['c3__sum'],aq4000['c5__sum'],aq4000['c6__sum'],aq4000['c7__sum']]
        s4000.append(obj)
#   ТАБЛИЦА 5000
    row = Rows.objects.filter(type  = 3, table = 'таб5000')
    s5000 = []
    for r in row:
        tab5000 = Doc3Tab5000.objects.filter(doc = doc, doc__period=period, row=r )
        aq5000 = tab5000.aggregate(Sum('c1'),Sum('c2'),Sum('c3'),Sum('c5'),Sum('c6'),Sum('c7'),Sum('c13'))
        obj = [tab5000[0].row,aq5000['c1__sum'],aq5000['c2__sum'],aq5000['c3__sum'],aq5000['c5__sum'],aq5000['c6__sum'],aq5000['c7__sum'],aq5000['c13__sum']]
        s5000.append(obj)
#   ТАБЛИЦА 5001
    row = Rows.objects.filter(type  = 3, table = 'таб5001')
    s5001 = []
    for r in row:
        tab5001 = Doc3Tab5001.objects.filter(doc = doc, doc__period=period, row=r )
        aq5001 = tab5001.aggregate(Sum('c1'),Sum('c2'),Sum('c3'),Sum('c5'),Sum('c6'),Sum('c7'),Sum('c13'))
        obj = [tab5001[0].row,aq5001['c1__sum'],aq5001['c2__sum'],aq5001['c3__sum'],aq5001['c5__sum'],aq5001['c6__sum'],aq5001['c7__sum'],aq5001['c13__sum']]
        s5001.append(obj)
#   ТАБЛИЦА 6000
    row = Rows.objects.filter(type  = 3, table = 'таб6000')
    s6000 = []
    for r in row:
        tab6000 = Doc3Tab6000.objects.filter(doc = doc, doc__period=period, row=r )
        aq6000 = tab6000.aggregate(Sum('c1'),Sum('c2'),Sum('c3'),Sum('c5'),Sum('c6'),Sum('c7'),Sum('c13'))
        obj = [tab6000[0].row,aq6000['c1__sum'],aq6000['c2__sum'],aq6000['c3__sum'],aq6000['c5__sum'],aq6000['c6__sum'],aq6000['c7__sum'],aq6000['c13__sum']]
        s6000.append(obj)
#   ТАБЛИЦА 7000
    row = Rows.objects.filter(type  = 3, table = 'таб7000')
    s7000 = []
    for r in row:
        tab7000 = Doc3Tab7000.objects.filter(doc = doc, doc__period=period, row=r )
        aq7000 = tab7000.aggregate(Sum('c1'),Sum('c2'),Sum('c3'),Sum('c4'),Sum('c5'),Sum('c6'))
        obj = [tab7000[0].row,aq7000['c1__sum'],aq7000['c2__sum'],aq7000['c3__sum'],aq7000['c4__sum'],aq7000['c5__sum'],aq7000['c6__sum']]
        s7000.append(obj)
    
#   в сл строке довавить остальные табличные части
    res = {'doc':s1,'tab1000':s1000,'tab2000':s2000,'tab3000':s3000,'tab4000':s4000,'tab5000':s5000,'tab5001':s5001,'tab6000':s6000,'tab7000':s7000}
    return res

def exp_to_excel_form3(doc, iperiod, iregion, mode, stat = None):    # mode = 0 по региону или группе больниц  mode = 1 - по конкретной больнице
    res =  calc_sum_form3(doc)
    speriod = get_period_namef(iperiod)
    sregion = get_region_name(mode,doc,iregion)
    name_file = get_name("/static/Form/Form3.xlsx")

    wb = openpyxl.load_workbook(name_file)
    
#    print(wb.get_sheet_names())
    
    sheet = wb['stat']
    sheet1 = wb['1000']
    sheet2 = wb['2000']
    sheet3 = wb['3000']
    sheet4 = wb['4000']
    sheet5 = wb['5000']
    sheet6 = wb['5001']
    sheet7 = wb['6000']
    sheet8 = wb['7000']
#    sheet = wb.active
    
    sheet['B1'] = "Период:"
    sheet['C1'] = speriod
    sheet['B2'] = "Учереждение"
    sheet['C2'] = sregion
    if mode==0:
        sheet['B3'] = "Статистика по отчету"  
        sheet['B4'] = "Организаций предоставляющих, Всего"
        sheet['C4'] = stat.rec_all
        sheet['B5'] = "Отобрано в отчет, Всего"
        sheet['C5'] = stat.rec_fltr
        sheet['B6'] = "Завершено"
        sheet['C6'] = stat.rec_complete
        sheet['B7'] = "Согласование"
        sheet['C7'] = stat.rec_soglas
        sheet['B8'] = "Корректировка"
        sheet['C8'] = stat.rec_correct
        sheet['B9'] = "Редактирование"
        sheet['C9'] = stat.rec_edit
       
# Вне табличные данные
    d = res['doc']
    
# ТаблицыS
#   1000
    startrow = 7
    i = 0
    t = res['tab1000']
    for line in t:
        sheet1["C" + str(startrow + i)] = line[5] + line[9]
        sheet1["D" + str(startrow + i)] = line[6] + line[10]
        sheet1["E" + str(startrow + i)] = line[7] + line[11]
        sheet1["F" + str(startrow + i)] = line[8] + line[12]
        sheet1["G" + str(startrow + i)] = line[5]
        sheet1["H" + str(startrow + i)] = line[6]
        sheet1["I" + str(startrow + i)] = line[7]
        sheet1["J" + str(startrow + i)] = line[8]
        sheet1["K" + str(startrow + i)] = line[9]
        sheet1["L" + str(startrow + i)] = line[10]
        sheet1["M" + str(startrow + i)] = line[11]
        sheet1["N" + str(startrow + i)] = line[12]
        i += 1

#   2000
    startrow = 6
    i = 0
    t = res['tab2000']
    for line in t:
        sheet2["C" + str(startrow + i)] = line[1]
        if i != 0 and i != 19:
            sheet2["D" + str(startrow + i)] = line[2]
            sheet2["E" + str(startrow + i)] = line[3]
        sheet2["F" + str(startrow + i)] = line[4]
        i += 1

#   3000
    startrow = 6
    i = 0
    t = res['tab3000']
    for line in t:
        sheet3["C" + str(startrow + i)] = line[1]
        sheet3["D" + str(startrow + i)] = line[2]
        sheet3["E" + str(startrow + i)] = line[3]
        sheet3["F" + str(startrow + i)] = line[4]
        if i != 13 and i != 14:
            sheet3["G" + str(startrow + i)] = line[5]
        i += 1
    sheet3['F25'] = d[0]

#   4000
    startrow = 6
    i = 0
    t = res['tab4000']
    for line in t:
        sheet4["D" + str(startrow + i)] = line[1]
        sheet4["E" + str(startrow + i)] = line[2]
        sheet4["F" + str(startrow + i)] = line[3]
        sheet4["H" + str(startrow + i)] = line[4]
        sheet4["I" + str(startrow + i)] = line[5]
        sheet4["J" + str(startrow + i)] = line[6]
        i += 1
    sheet4['H19'] = d[1]
    sheet4['H20'] = d[2]
    sheet4['K21'] = d[3]
    sheet4['K22'] = d[4]

#   5000
    startrow = 6
    i = 0
    t = res['tab5000']
    for line in t:
        sheet5["D" + str(startrow + i)] = line[1]
        sheet5["E" + str(startrow + i)] = line[2]
        sheet5["F" + str(startrow + i)] = line[3]
        sheet5["H" + str(startrow + i)] = line[4]
        sheet5["I" + str(startrow + i)] = line[5]
        sheet5["J" + str(startrow + i)] = line[6]
        sheet5["P" + str(startrow + i)] = line[7]
        i += 1   

#   5001
    startrow = 6
    i = 0
    t = res['tab5001']
    for line in t:
        sheet6["D" + str(startrow + i)] = line[1]
        sheet6["E" + str(startrow + i)] = line[2]
        sheet6["F" + str(startrow + i)] = line[3]
        sheet6["H" + str(startrow + i)] = line[4]
        sheet6["I" + str(startrow + i)] = line[5]
        sheet6["J" + str(startrow + i)] = line[6]
        sheet6["P" + str(startrow + i)] = line[7]
        i += 1   

#   6000
    startrow = 6
    i = 0
    t = res['tab6000']
    for line in t:
        sheet7["D" + str(startrow + i)] = line[1]
        sheet7["E" + str(startrow + i)] = line[2]
        sheet7["F" + str(startrow + i)] = line[3]
        sheet7["H" + str(startrow + i)] = line[4]
        sheet7["I" + str(startrow + i)] = line[5]
        sheet7["J" + str(startrow + i)] = line[6]
        sheet7["P" + str(startrow + i)] = line[7]
        i += 1    
    
#   7000
    startrow = 6
    i = 0
    t = res['tab7000']
    for line in t:
        sheet8["C" + str(startrow + i)] = line[1]
        sheet8["D" + str(startrow + i)] = line[2]
        sheet8["E" + str(startrow + i)] = line[3]
        sheet8["F" + str(startrow + i)] = line[4]
        sheet8["G" + str(startrow + i)] = line[5]
        sheet8["H" + str(startrow + i)] = line[6]
        i += 1
    startrow = 15
    i = 0
    for i in range(21):
        sheet8["G" + str(startrow + i)] = d[i + 5]

    sheet['B12'] = "Выведено в системе ЯрВебМед " + str(datetime.now()) 
    sheet['B12'].font = Font(size=5)
 
#   name_file =  get_name("\\medicament\\Form\\rep" + str(int(random()*100000000)) + ".xlsx") 
    name_file =  get_name("/medicament/Form/rep" + str(int(random()*100000000)) + ".xlsx") 
    wb.save(name_file)
    
    return name_file

 
