from uuid import UUID

import pytest

from app.models import Category


@pytest.mark.django_db
def test_create_model_category():
    category = Category.objects.create(name='Telefon')
    count = Category.objects.count()
    assert isinstance(category.pk, UUID)
    assert category.name == 'Telefon'
    assert count == 1
