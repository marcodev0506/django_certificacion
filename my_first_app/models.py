from django.db import models

class Carro(models.Model):
    title = models.TextField(max_length=255)