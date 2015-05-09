# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

# Third Party Stuff
from django.contrib import admin

from . import models


@admin.register(models.PushDevice)
class PushDeviceAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "token", "created", "modified"]
    list_display_links = list_display
    list_filter = ["created", "modified", ]
    readonly_fields = ["created", "modified", ]
