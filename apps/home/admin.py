# -*- encoding: utf-8 -*-

from django.contrib import admin
from apps.home.models import Eveniment, Voluntari


# Register your models here.

admin.site.register(Voluntari)
admin.site.register(Eveniment)


