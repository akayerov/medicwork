# -*- coding: utf-8 -*-
from django.db import models
from medicament.models import Document, Rows
# Doc3 Изменения в хранении информации - как товар в накладной
class Doc3(Document):
# тест 
# порядок именования полей tX_rY_N_cZ,   X-таблица номер, Y-номер строки, N-подстрока, Z-номер столбца
    t3001 = models.IntegerField('Таб3001', default=0)
 
    t4001_r1 = models.IntegerField('Таб4001_1', default=0)
    t4001_r2 = models.IntegerField('Таб4001_2', default=0)

    t4002_r1 = models.IntegerField('Таб4002_1', default=0)
    t4002_r2 = models.IntegerField('Таб4002_2', default=0)

    t7001 = models.IntegerField('Таб7001', default=0)
    t7002 = models.IntegerField('Таб7002', default=0)
    t7003 = models.IntegerField('Таб7003', default=0)
    t7004 = models.IntegerField('Таб7004', default=0)
    t7004_r1 = models.IntegerField('Таб7004_1', default=0)
    t7004_r2 = models.IntegerField('Таб7004_2', default=0)
    t7004_r3 = models.IntegerField('Таб7004_3', default=0)
    t7004_r4 = models.IntegerField('Таб7004_4', default=0)
    t7004_r5 = models.IntegerField('Таб7004_5', default=0)
    t7004_r6 = models.IntegerField('Таб7004_6', default=0)
    t7004_r7 = models.IntegerField('Таб7004_7', default=0)
    t7004_r8 = models.IntegerField('Таб7004_8', default=0)
    t7005 = models.IntegerField('Таб7005', default=0)
    t7006 = models.IntegerField('Таб7006', default=0)
    t7006_r1 = models.IntegerField('Таб7006_1', default=0)
    t7007 = models.IntegerField('Таб7007', default=0)
    t7008 = models.IntegerField('Таб7008', default=0)
    t7009 = models.IntegerField('Таб7009', default=0)
    t7010 = models.IntegerField('Таб7010', default=0)
    t7011 = models.IntegerField('Таб7011', default=0)
    t7012 = models.IntegerField('Таб7012', default=0)
    def __str__(self):              # __unicode__ on Python 2
        return str(self.period) + ':' + str(self.hosp)

class Doc3Tab1000(models.Model): # таблица 1000
    doc = models.ForeignKey(Doc3)  
    row = models.ForeignKey(Rows)
    c1 = models.IntegerField('Таб1000_Кол1', default=0)
    c2 = models.IntegerField('Таб1000_Кол2', default=0)
    c3 = models.IntegerField('Таб1000_Кол3', default=0)
    c4 = models.IntegerField('Таб1000_Кол4', default=0)
    c5 = models.IntegerField('Таб1000_Кол5', default=0)
    c6 = models.IntegerField('Таб1000_Кол6', default=0)
    c7 = models.IntegerField('Таб1000_Кол7', default=0)
    c8 = models.IntegerField('Таб1000_Кол8', default=0)
    c9 = models.IntegerField('Таб1000_Кол9', default=0)
    c10 = models.IntegerField('Таб1000_Кол10', default=0)
    c11 = models.IntegerField('Таб1000_Кол11', default=0)
    c12 = models.IntegerField('Таб1000_Кол12', default=0)
    def __str__(self):              # __unicode__ on Python 2
        return str(self.doc) + ':' + str(self.row)

class Doc3Tab2000(models.Model): # таблица 2000
    doc = models.ForeignKey(Doc3)  
    row = models.ForeignKey(Rows)
    c1 = models.IntegerField('Таб2000_Кол1', default=0)
    c2 = models.IntegerField('Таб2000_Кол2', default=0)
    c3 = models.IntegerField('Таб2000_Кол3', default=0)
    c4 = models.IntegerField('Таб2000_Кол4', default=0)
    def __str__(self):              # __unicode__ on Python 2
        return str(self.doc) + ':' + str(self.row)

class Doc3Tab3000(models.Model): # таблица 3000
    doc = models.ForeignKey(Doc3)  
    row = models.ForeignKey(Rows)
    c1 = models.IntegerField('Таб3000_Кол1', default=0)
    c2 = models.IntegerField('Таб3000_Кол2', default=0)
    c3 = models.IntegerField('Таб3000_Кол3', default=0)
    c4 = models.IntegerField('Таб3000_Кол4', default=0)
    c5 = models.IntegerField('Таб3000_Кол5', default=0)
    def __str__(self):              # __unicode__ on Python 2
        return str(self.doc) + ':' + str(self.row)

class Doc3Tab4000(models.Model): # таблица 4000
    doc = models.ForeignKey(Doc3)  
    row = models.ForeignKey(Rows)
    c1 = models.IntegerField('Таб4000_Кол1', default=0)
    c2 = models.IntegerField('Таб4000_Кол2', default=0)
    c3 = models.IntegerField('Таб4000_Кол3', default=0)
    c5 = models.IntegerField('Таб4000_Кол5', default=0)
    c6 = models.IntegerField('Таб4000_Кол6', default=0)
    c7 = models.IntegerField('Таб4000_Кол7', default=0)
    def __str__(self):              # __unicode__ on Python 2
        return str(self.doc) + ':' + str(self.row)

class Doc3Tab5000(models.Model): # таблица 5000
    doc = models.ForeignKey(Doc3)  
    row = models.ForeignKey(Rows)
    c1 = models.IntegerField('Таб5000_Кол1', default=0)
    c2 = models.IntegerField('Таб5000_Кол2', default=0)
    c3 = models.IntegerField('Таб5000_Кол3', default=0)
    c5 = models.IntegerField('Таб5000_Кол5', default=0)
    c6 = models.IntegerField('Таб5000_Кол6', default=0)
    c7 = models.IntegerField('Таб5000_Кол7', default=0)
    c13 = models.IntegerField('Таб5000_Кол13', default=0)
    def __str__(self):              # __unicode__ on Python 2
        return str(self.doc) + ':' + str(self.row)

class Doc3Tab5001(models.Model): # таблица 5001
    doc = models.ForeignKey(Doc3)  
    row = models.ForeignKey(Rows)
    c1 = models.IntegerField('Таб5001_Кол1', default=0)
    c2 = models.IntegerField('Таб5001_Кол2', default=0)
    c3 = models.IntegerField('Таб5001_Кол3', default=0)
    c5 = models.IntegerField('Таб5001_Кол5', default=0)
    c6 = models.IntegerField('Таб5001_Кол6', default=0)
    c7 = models.IntegerField('Таб5001_Кол7', default=0)
    c13 = models.IntegerField('Таб5001_Кол13', default=0)
    def __str__(self):              # __unicode__ on Python 2
        return str(self.doc) + ':' + str(self.row)

class Doc3Tab6000(models.Model): # таблица 6000
    doc = models.ForeignKey(Doc3)  
    row = models.ForeignKey(Rows)
    c1 = models.IntegerField('Таб6000_Кол1', default=0)
    c2 = models.IntegerField('Таб6000_Кол2', default=0)
    c3 = models.IntegerField('Таб6000_Кол3', default=0)
    c5 = models.IntegerField('Таб6000_Кол5', default=0)
    c6 = models.IntegerField('Таб6000_Кол6', default=0)
    c7 = models.IntegerField('Таб6000_Кол7', default=0)
    c13 = models.IntegerField('Таб6000_Кол13', default=0)
    def __str__(self):              # __unicode__ on Python 2
        return str(self.doc) + ':' + str(self.row)

class Doc3Tab7000(models.Model): # таблица 7000
    doc = models.ForeignKey(Doc3)  
    row = models.ForeignKey(Rows)
    c1 = models.IntegerField('Таб7000_Кол1', default=0)
    c2 = models.IntegerField('Таб7000_Кол2', default=0)
    c3 = models.IntegerField('Таб7000_Кол3', default=0)
    c4 = models.IntegerField('Таб7000_Кол4', default=0)
    c5 = models.IntegerField('Таб7000_Кол5', default=0)
    c6 = models.IntegerField('Таб7000_Кол6', default=0)
    def __str__(self):              # __unicode__ on Python 2
        return str(self.doc) + ':' + str(self.row)