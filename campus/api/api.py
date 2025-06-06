"""campus/api/api

Encapsulates operations on Campus resources.

The API for operations follows the Campus API specification.
Campus resources are represented through the CampusClient class, with
each resource represented as an attribute.
"""

from campus.api.base import CampusAPI
from campus.api.clients import Clients
from campus.api.users import Users


class CampusClient(CampusAPI):
    """The Campus API client.
    
    This class is the root of API calls.
    """
    clients: Clients
    users: Users

    def __init__(self, base_url: str, version = "v1"):
        super().__init__(base_url, version)
        # TODO: Add authentication parameters
        self.clients = Clients(self)
        self.users = Users(self)

    @classmethod
    def from_config(cls, config: dict):
        """Create a CampusClient from a configuration dictionary."""
        base_url = config.get("base_url", "https://api.campus.nyjc.dev")
        version = config.get("version", "v1")
        return cls(base_url, version)
