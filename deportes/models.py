from django.db import models
from wagtail.core.models import Page 
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your models here.
class Deporte(models.Model):
    entidad = models.CharField('entidad', max_length=250)
    domicilio = models.CharField(max_length=250)
    c_p = models.DecimalField(max_digits=6, decimal_places=1)
    localidad = models.CharField(max_length=250)
    horario = models.CharField(max_length=250)
    web = models.URLField(blank=True)
    email = models.URLField(blank=True)
    telefono = models.CharField(max_length=250)
    fax = models.CharField(max_length = 250)

    panels = [
        FieldPanel('entidad'),
        FieldPanel('domicilio'),
        FieldPanel('c_p'),
        FieldPanel('localidad'),
        FieldPanel('horario'),
        FieldPanel('web'),
        FieldPanel('email'),
        FieldPanel('telefono'),
        FieldPanel('fax')

    ]


    def __str__(self):
        return f'{self.entidad} ({self.domicilio}, {self.localidad}, {self.web}) '
    
    class Meta:
        verbose_name = 'Federación deportiva'
        verbose_name_plural = 'Federaciones deportivas'

class DeportesIndexPage(Page):
    introduccion = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('introduccion', classname="full")
    ]

    def paginate(self, request, deportes, *args):
        page = request.GET.get('page')
        
        paginator = Paginator(deportes, 5)
        try:
            pages = paginator.page(page)
        except PageNotAnInteger:
            pages = paginator.page(1)
        except EmptyPage:
            pages = paginator.page(paginator.num_pages)
        return pages

    def get_context(self, request):
        context = super().get_context(request)
        # context['peliculas'] = self.paginate(request)
        context['deportes'] = Deporte.objects.all()
        return context