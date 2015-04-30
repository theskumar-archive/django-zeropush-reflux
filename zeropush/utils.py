# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

# Standard Library
import json
import logging
from datetime import timedelta

# Third Party Stuff
import requests
from django.conf import settings

logger = logging.getLogger(__name__)

ZEROPUSH_NOTIFY_URL = "https://api.zeropush.com/notify"


def notify_devices(devices, alert=None, sound=None, badge='+1', info=None, expiry=None,
                   content_available=None, category=None):
    '''
    https://zeropush.com/documentation/api_reference#notify
    '''
    assert settings.ZEROPUSH_AUTH_TOKEN

    if len(devices) > 0:
        params = {
            "device_tokens": [device.token for device in devices]
        }
        # add alert payload
        params.update({"alert": alert})

        if sound is not None:
            params.update({"sound": sound})
        if badge is not None:
            params.update({"badge": badge})
        if info is not None:
            params.update({"info": json.dumps(info)})
        if content_available is not None:
            params.update({"content_available": bool(content_available)})
        if category is not None:
            params.update({"category": category})

        # add default expiry if not available
        expiry_time = expiry if expiry else int(timedelta(days=30).total_seconds())
        params.update({"expiry": expiry_time})

        # add authorization
        headers = {'Authorization': 'Token token="%s"' % settings.ZEROPUSH_AUTH_TOKEN,
                   'content-type': 'application/json'}

        response = requests.post(ZEROPUSH_NOTIFY_URL, json.dumps(params), headers=headers)

        if response.ok:
            logger.info("Push successfully sent to zeropush")
            return True
        else:
            msg = "Error! Push failed to be sent to zeropush! Error response: %s" % response.text
            logger.error(msg)
            return False

    return False
