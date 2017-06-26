# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify
# Create your models here.

class Entrada(models.Model):

       titulo = models.CharField(max_length=200)
       contenido = models.TextField()
       precio = models.CharField(max_length=10)
       slug = models.SlugField(editable=False)


       def __unicode__(self):
       	return self.titulo

       	def save(self, *args, **kwargs):
       		if not self.id:
       			self.slug = slugify(self.titulo)
       		super(Entrada, self).save(*args, **kwargs)


class Entrada2(models.Model):
       titulo = models.CharField(max_length=200)
       contenido = models.TextField()
       precio = models.CharField(max_length=200)
       categoria = models.CharField(max_length=200)
       slug = models.SlugField(editable=False)
       def save(self, *args, **kwargs):
                     if not self.id:
                            self.slug = slugify(self.titulo)
                     super(Entrada2, self).save(*args, **kwargs)

     
