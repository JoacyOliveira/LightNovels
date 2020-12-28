from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class UsuariosConfig(AppConfig):
    name = 'usuarios'
    verbose_name = _('profiles')

