from wagtail.contrib.modeladmin.options import (
    ModelAdmin, ModelAdminGroup, modeladmin_register)

from deportes.models import Deporte

'''
N.B. To see what icons are available for use in Wagtail menus and StreamField block types,
enable the styleguide in settings:

INSTALLED_APPS = (
   ...
   'wagtail.contrib.styleguide',
   ...
)

or see http://kave.github.io/general/2015/12/06/wagtail-streamfield-icons.html

This demo project includes the full font-awesome set via CDN in base.html, so the entire
font-awesome icon set is available to you. Options are at http://fontawesome.io/icons/.
'''


class DeportesAdmin(ModelAdmin):
    # These stub classes allow us to put various models into the custom "Wagtail Bakery" menu item
    # rather than under the default Snippets section.
    model = Deporte
    search_fields = ('entidad', 'domicilio', 'c_p')
    menu_icon = 'doc-full-inverse'  # change as required
    menu_order = 75  # will put in 3rd place (000 being 1st, 100 2nd)



class DeportesAdminGroup(ModelAdminGroup):
    # These stub classes allow us to put various models into the custom "Wagtail Bakery" menu item
    # rather than under the default Snippets section.
    menu_label = 'Federaciones'
    menu_icon = 'doc-full-inverse'  # change as required
    menu_order = 75  # will put in 3rd place (000 being 1st, 100 2nd)
    items = (DeportesAdmin, )


# When using a ModelAdminGroup class to group several ModelAdmin classes together,
# you only need to register the ModelAdminGroup class with Wagtail:
modeladmin_register(DeportesAdminGroup)
