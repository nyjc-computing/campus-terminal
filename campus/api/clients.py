"""campus/api/clients

Represents operations on the clients resource in Campus.
"""

from campus.schema.datatypes import ClientID, Validatable
from campus.schema.modeltypes import Client as ClientModel
from campus.api.base import SingleResource, ResourceCollection

from . import http


class Client(SingleResource):
    """Represents operations on a single client resource in Campus."""

    def __init__(self, parent, id: ClientID):
        super().__init__(parent)
        self.id = id


class Clients(ResourceCollection):
    """Represents operations on clients in Campus."""

