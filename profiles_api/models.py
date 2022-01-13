from django.db import models

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

class UserProfile (AbstractBaseUser, PermissionsMixin):
    ''' Modelo Base de datos para Usuarios en el sistema '''
    