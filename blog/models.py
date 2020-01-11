from django.db import models
from django.urls import reverse
from django.utils import timezone

class Post(models.Model): 
	titulo = models.CharField(max_length=100)
	conteudo = models.TextField()
	data = models.DateTimeField(default=timezone.now)
	autor = models.CharField(max_length=100)

	def __str__(self):
		return self.titulo
