from django.urls import reverse
from django.test import Client

def test_index_purBeurre_view():
    client = Client()
    path = reverse('favorite-index')
    response = client.get(path)
    content = response.content.decode()
    expected_content = ""
    assert response.status_code == 200