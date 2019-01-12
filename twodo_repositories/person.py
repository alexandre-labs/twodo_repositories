"""Defines the base class to `twodo_domain.person.Person` repositories.
"""
import abc
import typing as t
import uuid
from dataclasses import dataclass

from twodo_domain.person import Person


@dataclass
class IPersonData:
    """Represents an ID to an instance of the domain entity `twodo_domain.person.Person`.

    It can be used as the response after creating a representation
    to a `twodo_domain.person.Person` in the data system or the request to update
    a representation.

    It remove from the domain entity the responsability to have an attribute ID, as
    it (the ID) is usually related to a repository
    """

    id: uuid.UUID
    # The person is optional because in some context just the ID is enough (e.g. retrieve, delete)
    person: t.Optional[Person]


class IPersonRepositoryException(Exception):
    """It is not an interface, but should be used like it was.
    If some exception occurred on your impl., such exception has a context, so
    you can extends this exception to your context.

    e.g.:
        - Error on creating a representation because some id collision:
            class IDCollision(IPersonRepositoryException):
                pass
            raise IDCollision

    This class is useful to catch all person's repositories exceptions. So a sugestion:
        use it to catch all, but not to raise any.
    """

    pass


class IPersonRepository(abc.ABC):

    """A repository is an interface between a domain entity and a data system.
    A repository should implement (even with a pass) a CRUD (Create, Retrieve, Update and Delete)
    set of functions.
    """

    entity: Person

    @abc.abstractmethod
    def create(self, person: Person) -> IPersonData:
        """Creates a representation of a person in the data system.

        Parameters
        ----------

            person:
                An instance of the domain entity `twodo_domain.person.Person`

        Raises
        ------

            PersonRepositoryException:
                Any error on creating the representation

        Returns
        -------

            person_data: IPersonData
        """
        return NotImplemented  # type: ignore

    @abc.abstractmethod
    def retrieve(self, person_data: IPersonData) -> IPersonData:
        """Retrieves the person data by its unique ID.

        Parameters
        ----------

            person:
                The identifier of person representation

        Raises
        ------

            PersonRepositoryException:
                Any error on retrieving the representation

        Returns
        -------

            person_data: IPersonData
        """
        return NotImplemented  # type: ignore

    @abc.abstractmethod
    def update(self, person_data: IPersonData) -> IPersonData:
        """Updates a person data based on its ID.

        Parameters
        ----------

            person_data:
                The ID and person representing the data that should be updated.

        Raises
        ------

            PersonRepositoryException:
                Any error on updating the representation

        Returns
        -------

            person_data:
                The updated person data
        """
        return NotImplemented  # type: ignore

    @abc.abstractmethod
    def delete(self, person_data: IPersonData) -> None:
        """Deletes a preson data based on its ID.

        Parameters
        ----------

            person_data:
                The person data to access the ID.

        Raises
        ------

            PersonRepositoryException:
                Any error on deleting the representation

        Returns
        -------

            None
        """
        return NotImplemented  # type: ignore
