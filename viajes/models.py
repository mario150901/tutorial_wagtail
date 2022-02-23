from pydoc import classname
from django.db import models
from wagtail.core.models import Page 
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your models here.
class Viaje(models.Model):
    nombre = models.CharField('título', max_length=250)
    #slug = models.SlugField(blank=True)
    link = models.URLField()
    imagen = models.URLField()
    coordenadas = models.CharField("coordenadas", max_length = 250, blank=True)

    panels = [
        FieldPanel('nombre'),
        FieldPanel('link'),
        FieldPanel('imagen'),
        FieldPanel('coordenadas')

    ]

    def __str__(self):
        return f'{self.nombre}'
    
    class Meta:
        verbose_name = 'Viaje'
        verbose_name_plural = 'Viajes'

class ViajesPage(Page):
    texto = RichTextField(blank=True)
    coordenadas = RichTextField(blank = True, max_length = 200)
    content_panels = Page.content_panels + [
        FieldPanel('texto', classname="full"),
        FieldPanel('coordenadas', classname="full")
    ]

    def paginate(self, request, viajes, *args):
        page = request.GET.get('page')
        
        paginator = Paginator(viajes, 10)
        try:
            pages = paginator.page(page)
        except PageNotAnInteger:
            pages = paginator.page(1)
        except EmptyPage:
            pages = paginator.page(paginator.num_pages)
        return pages