"""Defines the base abstract class for a repository.
It uses the Python convention of put an underscore to indicate something
is private.
"""
import abc


class IRepository(abc.ABC):
    """A repository is an interface between a domain entity and a data system.
    A repository should implement (even with a pass) a CRUD (Create, Retrieve, Update and Delete)
    set of functions.

    ** The type hints should be defined by the entity base class. **
    """

    @abc.abstractmethod
    def create(self, entity):
        return NotImplemented

    @abc.abstractmethod
    def retrieve(self, entity_uuid):
        return NotImplemented

    @abc.abstractmethod
    def update(self, entity_uuid, entity):
        return NotImplemented

    @abc.abstractmethod
    def delete(self, entity_uuid):
        return NotImplemented
