from django.conf.urls import patterns, include, url
from django.contrib import admin
from medicament import views
from medicament import viewsAjax

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Medic.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.monitor_type_list),
    url(r'^contact/', views.contact_list, name='contact_list'),
    url(r'^FAQ/', views.FAQ, name='FAQ'),
    url(r'^documents/', views.documents, name='documents'),

# ПОпытка использовать тот же механизм списка мониторингов для другого типа мониторинга
#    url(r'^form/(?P<question_id>\d+)/$', views.monitoring_list),
    url(r'^form/(?P<question_id>.+)/$', views.monitoring_list),
    url(r'^load/(?P<question_id>.+)/$', views.load_from_excel),
    url(r'^monitor/$', views.monitoring_form),
    url(r'^monitor/add_comment/(?P<question_id>.+)/$', views.add_comment, name='add_comment'),
    url(r'^monitor/export/(?P<question_id>.+)/$', views.export, name='export'),
    url(r'^monitor/(?P<question_id>.+)/$', views.monitoring_form, name='monitoring_form'),
    url(r'^test/(?P<question_id>.+)/$', views.test, name='test'),
    url(r'^test1/(?P<question_id>.+)/$', views.testAjax, name='testAjax'),
    url(r'^testJQ/(?P<question_id>.+)/$', viewsAjax.testAjaxJQ, name='testAjaxJQ'),
    url(r'^testJS1/', viewsAjax.testAjaxJS1, name='testAjaxJS'),
    url(r'^server/check/', viewsAjax.serverCheck, name='serverCheck'),
    url(r'^server/longOperation/', viewsAjax.longOperation, name='longOperation'),
    url(r'^server/getStatusOperation/', viewsAjax.serverGetStatusOperation, name='serverStatus'),

    url(r'^testJS2/', viewsAjax.testAjaxJS2, name='testAjaxJS2'),
    url(r'^server/longOperation2/', viewsAjax.longOperation2, name='longOperation2'),
    url(r'^server/getStatusOperation2/', viewsAjax.serverGetStatusOperation2, name='serverStatus2'),

)