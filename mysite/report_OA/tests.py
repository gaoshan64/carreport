from django.test import TestCase

# Create your tests here.
import os
os.environ.setdefault("DJANGO_SETTING_MODULE","demo.settings")
import django
django.setup()