# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from .models import Entrada2

# Create your views here.

class IndexView (ListView):

	template_name = 'index.html'
	model = Entrada2

class EntradaDetailView (DetailView):

	template_name = 'detalle.html'
	model = Entrada2