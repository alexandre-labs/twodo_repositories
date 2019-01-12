import pytest

from twodo_repositories.todo import IToDoRepository, IToDoRepositoryException


def test_todo_repo_missing_create_method():
    class TestToDoRepository(IToDoRepository):
        def retrieve(self, todo_data):
            pass

        def update(self, todo_data):
            pass

        def delete(self, todo_data):
            pass

    with pytest.raises(TypeError):
        TestToDoRepository()


def test_todo_repo_missing_update_method():
    class TestToDoRepository(IToDoRepository):
        def create(self, todo):
            pass

        def retrieve(self, todo_data):
            pass

        def delete(self, todo_data):
            pass

    with pytest.raises(TypeError):
        TestToDoRepository()


def test_todo_repo_missing_retrieve_method():
    class TestToDoRepository(IToDoRepository):
        def create(self, todo):
            pass

        def update(self, todo_data):
            pass

        def delete(self, todo_data):
            pass

    with pytest.raises(TypeError):
        TestToDoRepository()


def test_todo_repo_missing_delete_method():
    class TestToDoRepository(IToDoRepository):
        def create(self, todo):
            pass

        def retrieve(self, todo_data):
            pass

        def update(self, todo_data):
            pass

    with pytest.raises(TypeError):
        TestToDoRepository()


def test_raising_subclass_of_todo_repository_exception():
    class ConnectionTimeOut(IToDoRepositoryException):
        pass

    class TestToDoRepository(IToDoRepository):
        def create(self, todo):
            raise ConnectionTimeOut

        def retrieve(self, todo_data):
            pass

        def update(self, todo_data):
            pass

        def delete(self, todo_data):
            pass

    todo_repo = TestToDoRepository()

    with pytest.raises(IToDoRepositoryException):
        todo_repo.create('Some Todo')
