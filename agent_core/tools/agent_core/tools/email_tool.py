"""
Email tool for Agentra.uk (v0.2)

This is a safe placeholder implementation that simulates sending an email.
In future versions this can be wired to a real email provider (SMTP or API).
"""

from dataclasses import dataclass
from typing import Dict, Any
import datetime


@dataclass
class EmailResult:
    to: str
    subject: str
    body_preview: str
    timestamp: str
    status: str


class EmailTool:
    """
    Simple email tool interface.

    The goal for v0.2 is not to actually send email, but to:
    - Define a clean interface
    - Log intent to send
    - Return a structured result that the agent can reason about
    """

    def __init__(self, default_sender: str = "agent@agentra.uk") -> None:
        self.default_sender = default_sender

    def send_email(self, to: str, subject: str, body: str) -> Dict[str, Any]:
        """
        Simulates sending an email (placeholder).
        """

        timestamp = datetime.datetime.utcnow().isoformat()

        return {
            "from": self.default_sender,
            "to": to,
            "subject": subject,
            "body_preview": body[:60] + ("..." if len(body) > 60 else ""),
            "timestamp": timestamp,
            "status": "simulated_sent"
        }
