from django.db import models

class Carro(models.Model):
    title = models.TextField(max_length=255)
    years= models.CharField(max_length=8,null=True)
    colors=models.CharField(max_length=30, null=True)

    def __str__(self):
        return f" {self.title} -{self.years}"

class Conductores(models.Model):
    name = models.TextField(max_length=255)
    years= models.CharField(max_length=8,null=True)
    sex=models.CharField(max_length=30, null=True)

    def __str__(self):
        return f" {self.name} -{self.years}--{self.sex}"
    
class Licen(models.Model):
    title = models.TextField(max_length=200)
    asig = models.ForeignKey(Conductores, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.title}---{self.asig}"
    