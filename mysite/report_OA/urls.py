"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('base', views.base_test,name='base'),
    path('hello', views.hello_world,name='hello'),
    path('report_list', views.report_list,name='report_list'),
    #客户
    path('customer_list', views.customer_list,name='customer_list'),
    path('customer_detial/<int:customer_id>', views.customer_detial,name='customer_detial'),
    path('customer_add/', views.customer_add, name='customer_add'),
    path('customer_del/', views.customer_del, name='customer_del'),
    path('customer_redit/<int:customer_id>', views.customer_redit, name='customer_redit'),
    #车辆
    path('car_list', views.car_list,name='car_list'),
    path('car_detial/<int:car_id>', views.car_detial,name='car_detial'),
    path('car_del/', views.car_del, name='car_del'),
    path('car_add/', views.car_add, name='car_add'),
    path('car_redit/<int:car_id>', views.car_redit, name='car_redit'),
    #报告
    path('report_list', views.report_list,name='report_list'),
    path('report_detial/<int:report_id>', views.report_detial,name='report_detial'),
    path('report_del/', views.report_del, name='report_del'),
    #path('report1_add/', views.report_add, name='report_add'),
    #path('report1_redit/<int:report_id>', views.report_redit, name='report_redit'),
    path('report2_add/', views.report_add, name='report_add'),
    path('report2_redit/<int:report_id>', views.report2_redit, name='report2_redit'),
    path('report1_redit/<int:report_id>', views.report1_redit, name='report1_redit'),
    path('report_print/<int:report_id>', views.report_print, name='report_print'),

]
