"""
Project Orion
=============

Version information for Project Orion.

This module provides a single source of truth for application metadata.
Other modules should import these constants rather than defining their own
version or project information.

Author:
    Project Orion Development Team

License:
    MIT
"""

from __future__ import annotations

from dataclasses import dataclass

# -----------------------------------------------------------------------------
# Application Metadata
# -----------------------------------------------------------------------------

APP_NAME: str = "Project Orion"

APP_DESCRIPTION: str = (
    "Automated Infrastructure Deployment Platform"
)

COMPANY_NAME: str = "Project Orion"

VERSION_MAJOR: int = 0
VERSION_MINOR: int = 1
VERSION_PATCH: int = 0

VERSION: str = (
    f"{VERSION_MAJOR}."
    f"{VERSION_MINOR}."
    f"{VERSION_PATCH}"
)

COPYRIGHT_YEAR: int = 2026

COPYRIGHT: str = (
    f"© {COPYRIGHT_YEAR} {COMPANY_NAME}"
)


# -----------------------------------------------------------------------------
# Version Information
# -----------------------------------------------------------------------------

@dataclass(frozen=True, slots=True)
class VersionInfo:
    """
    Immutable representation of the Orion application version.
    """

    major: int
    minor: int
    patch: int

    @property
    def short(self) -> str:
        """
        Returns:
            Version string without additional metadata.
        """
        return f"{self.major}.{self.minor}.{self.patch}"

    @property
    def full(self) -> str:
        """
        Returns:
            Full application name including version.
        """
        return f"{APP_NAME} v{self.short}"


VERSION_INFO = VersionInfo(
    major=VERSION_MAJOR,
    minor=VERSION_MINOR,
    patch=VERSION_PATCH,
)