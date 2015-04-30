#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import os
# import shutil
import unittest

import responses

# from zeropush import models
from zeropush.utils import ZEROPUSH_NOTIFY_URL, notify_devices


def test_hello(settings):
    settings.ZEROPUSH_AUTH_TOKEN = "super-poweful-token"
