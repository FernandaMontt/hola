# -*- coding: utf-8 -*-

from django.shortcuts import render
#from models import Post
from django.db import models
from django.utils import timezone

# Aqui se crea el modelo	
class Post(models.Model):
		author=models.ForeignKey('auth.User')
		titulo=models.CharField(max_length=200)
		text=models.TextField()
		created_date=models.DateTimeField(
					default=timezone.now)
		published_date=models.DateTimeField(
					blank=True, null=True)
			   
		def metodo(self):
					self.published_date = timezone.now()
					self.save()
		  
		def __str__(self):
					return self.titulo
	  

		  


