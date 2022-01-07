from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^contact$', views.contact, name='contact'),
    re_path(r'^building-materials$', views.building_materials, name='materials'),
    re_path(r'^artificial-intelligence$', views.artificial_intelligence, name='ai'),
    re_path(r'^ui-ux-design-analysis$', views.ui_ux_design_analysis, name='design'),
    re_path(r'^website-development$', views.website_development, name='web-development'),
    re_path(r'^hosting$', views.hosting, name='hosting'),
    re_path(r'^app-development$', views.app_development, name='app-development'),
    re_path(r'^computer-hardware-networking$', views.computer_hardware_networking, name='hardware'),
    re_path(r'^terms&conditions$', views.terms, name='terms'),
    re_path(r'^send-mail$', views.send_email, name='send-mail'),
]
