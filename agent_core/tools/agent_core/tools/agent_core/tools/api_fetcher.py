"""
API fetcher tool for Agentra.uk (v0.2)

Lightweight wrapper around HTTP GET requests so the agent can
retrieve data from external APIs in a controlled way.
"""

from typing import Dict, Any, Optional
import json

try:
    import requests
except ImportError:
    requests = None  # In case the runtime has no requests installed


class ApiFetcher:
    """
    Simple HTTP GET client for external APIs.

    For v0.2 this is intentionally minimal and will later be extended
    with authentication, rate limiting and retries.
    """

    def fetch(self, url: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Fetch JSON data from a given URL.

        Returns a dict with:
        - status: "ok" / "error"
        - http_status: HTTP status code (if available)
        - data: parsed JSON or raw text
        - error: error message if any
        """

        if requests is None:
            return {
                "status": "error",
                "http_status": None,
                "data": None,
                "error": "requests library not available in this environment",
            }

        try:
            response = requests.get(url, params=params, timeout=10)
            content_type = response.headers.get("Content-Type", "")

            if "application/json" in content_type:
                data = response.json()
            else:
                # Fallback for non-JSON responses
                data = {"raw": response.text[:500]}

            return {
                "status": "ok",
                "http_status": response.status_code,
                "data": data,
                "error": None,
            }

        except Exception as exc:
            return {
                "status": "error",
                "http_status": None,
                "data": None,
                "error": str(exc),
            }
