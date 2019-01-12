"""Defines the base class to `twodo_domain.todo.ToDo` repositories.
"""
import abc
import typing as t
import uuid
from dataclasses import dataclass

from twodo_domain.todo import ToDo


@dataclass
class IToDoData:
    """Represents an ID to an instance of the domain entity `twodo_domain.todo.ToDo`.

    It can be used as the response after creating a representation
    to a `twodo_domain.todo.ToDo` in the data system or the request to update
    a representation.

    It remove from the domain entity the responsability to have an attribute ID, as
    it (the ID) is usually related to a repository
    """

    id: uuid.UUID
    # The todo is optional because in some context just the ID is enough (e.g. retrieve, delete)
    todo: t.Optional[ToDo]


class IToDoRepositoryException(Exception):
    """It is not an interface, but should be used like it was.
    If some exception occurred on your impl., such exception has a context, so
    you can extends this exception to your context.

    e.g.:
        - Error on creating a representation because some id collision:
            class IDCollision(IToDoRepositoryException):
                pass
            raise IDCollision

    This class is useful to catch all ToDo's repositories exceptions. So a sugestion:
        use it to catch all, but not to raise all.
    """

    pass


class IToDoRepository(abc.ABC):

    """A repository is an interface between a domain entity and a data system.
    A repository should implement (even with a pass) a CRUD (Create, Retrieve, Update and Delete)
    set of functions.
    """

    entity: ToDo

    @abc.abstractmethod
    def create(self, todo: ToDo) -> IToDoData:
        """Creates a representation of a ToDo in the data system.

        Parameters
        ----------

            todo:
                An instance of the domain entity `twodo_domain.todo.ToDo`

        Raises
        ------

            ToDoRepositoryException:
                Any error on creating the representation

        Returns
        -------

            todo_data: IToDoData
        """
        return NotImplemented  # type: ignore

    @abc.abstractmethod
    def retrieve(self, todo_data_id: uuid.UUID) -> IToDoData:
        """Retrieves the todo data by its unique ID.

        Parameters
        ----------

            todo:
                The identifier of todo representation

        Raises
        ------

            ToDoRepositoryException:
                Any error on retrieving the representation

        Returns
        -------

            todo_data: IToDoData
        """
        return NotImplemented  # type: ignore

    @abc.abstractmethod
    def update(self, todo_data: IToDoData) -> IToDoData:
        """Updates a todo data based on its ID.

        Parameters
        ----------

            todo_data:
                The ID and todo representing the data that should be updated.

        Raises
        ------

            ToDoRepositoryException:
                Any error on updating the representation

        Returns
        -------

            todo_data:
                The updated todo data
        """
        return NotImplemented  # type: ignore

    @abc.abstractmethod
    def delete(self, todo_data: IToDoData) -> None:
        """Deletes a preson data based on its ID.

        Parameters
        ----------

            todo_data:
                The todo data to access the ID.

        Raises
        ------

            ToDoRepositoryException:
                Any error on deleting the representation

        Returns
        -------

            None
        """
        return NotImplemented  # type: ignore
