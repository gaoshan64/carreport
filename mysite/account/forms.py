# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : forms.py
# Time       ：2022/2/23 4:02
# Author     ：Gao Shan
# Description：
"""
from django import forms

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control",'placeholder':"用户名"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control",'placeholder':"密码"}),)