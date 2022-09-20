import pytest

from django.urls import reverse


@pytest.mark.django_db
def teste_post_views(client):
    url = reverse('home')
    response = client.get(url)
    assert response.status_code == 200
