import pytest

from django.urls import reverse, resolve

def test_index_url():
    assert resolve("/").view_name == "index"