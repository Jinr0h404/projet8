from django.urls import reverse
from django.test import Client


def test_index_purBeurre_view():
    client = Client()
    path = reverse('index')
    response = client.get(path)
    assert response.status_code == 200

def test_legal_view():
    client = Client()
    path = reverse('home-legal')
    response = client.get(path)
    assert response.status_code == 200