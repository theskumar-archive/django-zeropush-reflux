django-zeropush-2
=================

[![Build Status](https://travis-ci.org/theskumar/django-zeropush-reflux.svg)](https://travis-ci.org/theskumar/django-zeropush-reflux) [![Coverage Status](https://coveralls.io/repos/theskumar/django-zeropush-reflux/badge.svg)](https://coveralls.io/r/theskumar/django-zeropush-reflux)

A django app that helps you use [ZeroPush](http://zeropush.com)'s push notification API simply in your django backend for an iOS app.

# django-zeropush features

- Easy to use methods for sending push notifications to a user's all devices 
- Easy to use methods to connect iOS devices to a user.

## Interfaces

### Register an iOS device

```
zeropush.register_apple_device(user, token)
```

### Unregister an iOS device

```
zeropush.deregister_apple_device(user, token)
```

### Send push notification

```
zeropush.send_push_notification(user, alert=None, sound=None, badge=None,
                                info=None, expiry=None, 
                                content_available=None, category=None) 
```

### Send bulk push notification

```
zeropush.send_bulk_push_notification(user, alert=None, sound=None, badge=None,
                                     info=None, expiry=None, 
                                     content_available=None, category=None) 
```

# Installation

1. Add `zeropush` to your `INSTALLED_APPS` in your project's `settings.py`
2. Add `ZEROPUSH_AUTH_TOKEN="YOUR API TOKEN HERE"` to your `settings.py`
3. Run `./manage.py migrate` to create the PushDevice model's table.
4. Use `zeropush.register_apple_device` method to register a device to a user.
5. Now you can send push notifications as above!


# LICENSE

```
Copyright (c) 2015, Saurabh Kumar
Copyright (c) 2013, Håkan Waara
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
Neither the name of the owner nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
```
