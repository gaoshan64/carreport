# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : forms.py
# Time       ：2022/2/24 17:44
# Author     ：Gao Shan
# Description：
"""
from django import forms
from django.contrib.auth.models import User
from .models import Customer,CarAbout,ReportsContent2,ReportsContent1
from ajaximage.widgets import AjaxImageWidget


class AjaxImageField(forms.FileField):
    widget = AjaxImageWidget()




class CustomerAddForm(forms.ModelForm):

    class Meta:
        model =Customer
        exclude=()

class CarAboutForm(forms.ModelForm):
    #licence_first=forms.DateField(label='初次等登记日期',widget=forms.DateInput(attrs={'type':'date'}))
    #licence_issued=forms.DateField(label='上牌日期',widget=forms.DateInput(attrs={'type':'date'}))

    class Meta:
        model = CarAbout
        exclude=()
        widgets ={
            'licence_first':forms.TextInput(attrs={'type':'date'}),
            'licence_issued': forms.TextInput(attrs={'type': 'date'})
        }


class Report2ContentForm(forms.ModelForm):



    class Meta:
        model = ReportsContent2
        exclude=('report_m',)
        plus_attr='id_car_score.value' \
                  '=parseInt(id_car_body_score.value)' \
                  '+parseInt(id_car_chassis_score.value)' \
                  '+parseInt(id_car_power_score.value)' \
                  '+parseInt(id_car_com_score.value);'
        max_value_200='if(value>200)value=200'
        max_value_300='if(value>300)value=300'

        widgets = {
            'car_body_score':forms.NumberInput(attrs={'onChange':plus_attr,'min':'0','max':'200',
                                                      'oninput':max_value_200}),
            'car_chassis_score':forms.NumberInput(attrs={'onChange':plus_attr,'min':'0','max':'200',
                                                         'oninput':max_value_200}),
            'car_power_score':forms.NumberInput(attrs={'onChange':plus_attr,'min':'0','max':'300',
                                                       'oninput':max_value_300}),
            'car_com_score':forms.NumberInput(attrs={'onChange':plus_attr,'min':'0','max':'300',
                                                     'oninput':max_value_300}),
        }

class Report1ContentForm(forms.ModelForm):
    class Meta:
        model =ReportsContent1
        exclude=('report_m',)