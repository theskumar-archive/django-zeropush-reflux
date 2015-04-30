# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf import settings
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class PushDevice(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, blank=False,
                             related_name="pushdevices",
                             verbose_name=_("Owner of this device"))
    token = models.CharField(_("Device token string"), null=False, blank=False,
                             max_length=255, db_index=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('push device')
        verbose_name_plural = _('push devices')
        ordering = ('-modified',)

    def __str__(self):
        return u"UserDevice %s" % self.token
