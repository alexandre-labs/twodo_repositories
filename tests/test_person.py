import pytest

from twodo_domain.person import Person
from twodo_repositories.person import IPersonRepository, IPersonRepositoryException


def test_person_repo_missing_create_method():
    class TestPersonRepository(IPersonRepository):
        def retrieve(self, person_data):
            pass

        def update(self, person_data):
            pass

        def delete(self, person_data):
            pass

    with pytest.raises(TypeError):
        TestPersonRepository()


def test_person_repo_missing_update_method():
    class TestPersonRepository(IPersonRepository):
        def create(self, person):
            pass

        def retrieve(self, person_data):
            pass

        def delete(self, person_data):
            pass

    with pytest.raises(TypeError):
        TestPersonRepository()


def test_person_repo_missing_retrieve_method():
    class TestPersonRepository(IPersonRepository):
        def create(self, person):
            pass

        def update(self, person_data):
            pass

        def delete(self, person_data):
            pass

    with pytest.raises(TypeError):
        TestPersonRepository()


def test_person_repo_missing_delete_method():
    class TestPersonRepository(IPersonRepository):
        def create(self, person):
            pass

        def retrieve(self, person_data):
            pass

        def update(self, person_data):
            pass

    with pytest.raises(TypeError):
        TestPersonRepository()


def test_raising_subclass_of_person_repository_exception():
    class ConnectionTimeOut(IPersonRepositoryException):
        pass

    class TestPersonRepository(IPersonRepository):
        def create(self, person):
            raise ConnectionTimeOut

        def retrieve(self, person_data):
            pass

        def update(self, person_data):
            pass

        def delete(self, person_data):
            pass

    person_repo = TestPersonRepository()

    with pytest.raises(IPersonRepositoryException):
        person_repo.create(Person('Aleaxndre', 'alexandre@inter.net'))
