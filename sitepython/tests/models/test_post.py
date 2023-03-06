import pytest

from blog import PostFactory


@pytest.fixture
def post_published():
    return PostFactory()


@pytest.mark.django_db
def test_create_published_post(post_published):
    assert post_published.title == 'pytest with factory'
