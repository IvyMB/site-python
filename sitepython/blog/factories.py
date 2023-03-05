import factory
from faker import Factory as FakeFactory

from django.contrib.auth.models import User
from django.utils.timezone import now

from .models.post import Post

faker = FakeFactory.create()

class UserFactory (factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = factory.Faker("safe_email")
    username = factory.LazyAtrribute(lambda x : faker.name())

    @classmethod
    def _prepare(cls, create, **kwargs):
        password = kwargs.pop("password", None)
        user = super(UserFactory, cls)._prepare(create,**kwargs)
        if password:
            user.save()
        return user

class PostFactory (factory.django.DjangoModelFactory):
    title = factory.LazyAttribute(lambda x : faker.sentence())
    created_on = factory.LazyAttribute(lambda x : now ())
    author = factory.subFactory(UserFactory)
    status = 0

    class Meta:
        model = Post