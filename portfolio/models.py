from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Company(models.Model):
    name = models.CharField(max_length=250, verbose_name="Nombre de la empresa")
    description = models.TextField(verbose_name="Descripción")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"
        ordering = ["-created"]


    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=250, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(verbose_name="Imagen", upload_to="projects")
    link = models.URLField(null=True, blank=True, verbose_name="Dirección Web")
    companies = models.ManyToManyField(Company, verbose_name="Empresas")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-created"]


    def __str__(self):
        return self.title