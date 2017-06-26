# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Entrada
from django.views.generic import ListView
# Create your views here.

class IndexView (ListView):

	template_name = 'index.html'
	model = Entrada