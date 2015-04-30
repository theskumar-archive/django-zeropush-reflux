# -*- coding: utf-8 -*-

# Third Party Stuff
import factory
from django.conf import settings
from factory import fuzzy


class PushDeviceFactory(factory.DjangoModelFactory):

    class Meta:
        model = 'zeropush.PushDevice'
        strategy = factory.CREATE_STRATEGY

    user = factory.SubFactory("tests.factories.UserFactory")
    token = fuzzy.FuzzyText(chars='01234567890abcdef-', length=64)


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = settings.AUTH_USER_MODEL
        strategy = factory.CREATE_STRATEGY

    # modify this to USERNAME_FIELD for custom user model
    username = factory.Sequence(lambda n: "user{}".format(n))
    email = factory.Sequence(lambda n: 'user%04d@email.com' % n)
    password = factory.PostGeneration(lambda obj, *args, **kwargs: obj.set_password(obj.username))
