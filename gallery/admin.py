# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Categorys,Location,Image

# Register your models here.


admin.site.register(Categorys)
admin.site.register(Location)
admin.site.register(Image)
