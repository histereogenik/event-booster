import pytest
from .subscribers_repository import SubscribersRepository

@pytest.mark.skip("Insert in DB")
def test_insert():
    subscriber_info = {
        "nome": "meuNome22",
        "email": "email22@email.com",
        "evento_id": 2
    }
    subs_repo = SubscribersRepository()
    subs_repo.insert(subscriber_info)

@pytest.mark.skip("Select in DB")
def test_select():
    email = "email22@email.com"
    evento_id = 2
    subs_repo = SubscribersRepository()
    selected = subs_repo.select_subscriber(email=email, evento_id=evento_id)

    print(selected.nome)