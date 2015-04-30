# -*- coding: utf-8 -*-
# Standard Library
import logging

# Third Party Stuff
from django.apps import apps
from django.conf import settings

from .utils import notify_devices

log = logging.getLogger(__name__)


def register_apple_device(user, token):
    PushDevice = apps.get_model("zeropush", "PushDevice")
    device = PushDevice.objects.filter(token=token).first()
    if device:
        device.user = user
        device.save()
        return device
    else:
        return PushDevice.objects.create(token=token, user=user)


def deregister_apple_device(user, token):
    PushDevice = apps.get_model("zeropush", "PushDevice")
    device = PushDevice.objects.filter(token=token, user=user).first()
    if device:
        device.delete()
        return device
    else:
        return False


def send_push_notification(user, alert=None, sound=None, badge=None, info=None, expiry=None,
                           content_available=None, category=None):
    if getattr(settings, 'DISABLE_PUSH_NOTIFICATION', False):
        log.info("Sent to %s: %s" % (user.get_full_name(), str(alert)))
        return True

    return notify_devices(user.pushdevices.all(), alert=alert, sound=sound,
                          badge=badge, info=info, expiry=expiry,
                          content_available=content_available, category=category)


def send_bulk_push_notification(users, alert=None, sound=None, badge=None, info=None, expiry=None,
                                content_available=None, category=None):

    devices = [user.pushdevices.all() for user in users]

    # Flaten list of list. i.e. merge devices of every users
    # http://stackoverflow.com/a/952952
    merged_devices = [item for sublist in devices for item in sublist]

    if getattr(settings, 'DISABLE_PUSH_NOTIFICATION', False):
        log.info("Sent to %s: %s" % (merged_devices, str(alert)))
        return True

    return notify_devices(merged_devices, alert=alert, sound=sound,
                          badge=badge, info=info, expiry=expiry,
                          content_available=content_available, category=category)
