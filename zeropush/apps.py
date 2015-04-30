# -*- coding: utf-8 -*-

# Third Party Stuff
from django.apps import AppConfig


class ZeroPushAppConfig(AppConfig):
    name = "zeropush"
    verbose_name = "ZeroPush"

    def ready(self):
        pass
