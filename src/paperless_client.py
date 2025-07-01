"""Skeleton client for interacting with Paperless-ngx."""

from typing import Any

class PaperlessClient:
    """Simple placeholder client."""

    def __init__(self, base_url: str, token: str | None = None):
        self.base_url = base_url
        self.token = token

    def list_documents(self) -> Any:
        """Return a list of documents from Paperless-ngx."""
        # This is just a placeholder and does not perform real requests.
        return []
