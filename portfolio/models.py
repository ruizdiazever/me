from django.db import models

# Create your models here.# En el parametro de la clase Project hereda model.Model
# Esto arma como si fuera una tabla de BD
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name = "Titulo") #Cadena de caracteres
    state = models.CharField(max_length=200, verbose_name= "Estado")
    description = models.TextField(verbose_name = "Descripcion")
    image = models.ImageField(verbose_name = "Imagen", upload_to="projects")
    link = models.URLField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name = "Fecha de modificacion")

    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-created"] # "-created" invierte la muestra, metodo de lista

    # Metodo reservado lleva doble guionbajo en ambos lados..
    def __str__(self): # Esto es para que devuelva una cadena & no un objets
        return self.title # Cuando vos llamas traeme el titulo.. eso significa este choclo