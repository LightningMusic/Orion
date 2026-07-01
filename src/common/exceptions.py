"""
Project Orion
=============

Application exception hierarchy.

All custom exceptions within Project Orion should inherit from
OrionError. This provides a consistent exception hierarchy for
logging, error handling, and user-facing error reporting.

Author:
    Project Orion Development Team

License:
    MIT
"""

from __future__ import annotations


class OrionError(Exception):
    """
    Base exception for all Project Orion errors.

    Catch this exception to handle any application-specific error.
    """


# =============================================================================
# Application
# =============================================================================


class InitializationError(OrionError):
    """
    Raised when Orion fails during application startup.
    """


class ShutdownError(OrionError):
    """
    Raised when Orion encounters an error during shutdown.
    """


class ServiceRegistrationError(OrionError):
    """
    Raised when a service cannot be registered with the service container.
    """


class ServiceResolutionError(OrionError):
    """
    Raised when a requested service cannot be resolved.
    """


class EventBusError(OrionError):
    """
    Raised for Event Bus failures.
    """


# =============================================================================
# Configuration
# =============================================================================


class ConfigurationError(OrionError):
    """
    Base class for configuration-related errors.
    """


class ConfigurationFileNotFoundError(ConfigurationError):
    """
    Raised when a required configuration file cannot be found.
    """


class ConfigurationValidationError(ConfigurationError):
    """
    Raised when configuration validation fails.
    """


class ConfigurationVersionError(ConfigurationError):
    """
    Raised when an unsupported configuration version is encountered.
    """


# =============================================================================
# Logging
# =============================================================================


class LoggingError(OrionError):
    """
    Raised when the logging subsystem fails.
    """


# =============================================================================
# Hardware Inspection
# =============================================================================


class InspectionError(OrionError):
    """
    Base class for hardware inspection failures.
    """


class HardwareDetectionError(InspectionError):
    """
    Raised when hardware cannot be identified.
    """


class UnsupportedHardwareError(InspectionError):
    """
    Raised when unsupported hardware is encountered.
    """


class SMARTError(InspectionError):
    """
    Raised when SMART information cannot be retrieved.
    """


# =============================================================================
# Recovery
# =============================================================================


class RecoveryError(OrionError):
    """
    Base class for recovery subsystem failures.
    """


class RecoveryVerificationError(RecoveryError):
    """
    Raised when recovered data cannot be verified.
    """


# =============================================================================
# Preparation
# =============================================================================


class PreparationError(OrionError):
    """
    Base class for storage preparation failures.
    """


class ConfirmationError(PreparationError):
    """
    Raised when destructive action confirmation fails.
    """


class SanitizationError(PreparationError):
    """
    Raised when storage sanitization fails.
    """


# =============================================================================
# Provisioning
# =============================================================================


class ProvisioningError(OrionError):
    """
    Base class for provisioning failures.
    """


class InstallationError(ProvisioningError):
    """
    Raised when Proxmox installation fails.
    """


class BootstrapError(ProvisioningError):
    """
    Raised when bootstrap configuration fails.
    """


# =============================================================================
# Networking
# =============================================================================


class NetworkError(OrionError):
    """
    Base class for networking failures.
    """


class EthernetDisconnectedError(NetworkError):
    """
    Raised when no Ethernet connection is detected.
    """


class DHCPError(NetworkError):
    """
    Raised when DHCP configuration fails.
    """


class DNSResolutionError(NetworkError):
    """
    Raised when DNS resolution fails.
    """


class GatewayUnreachableError(NetworkError):
    """
    Raised when the configured gateway cannot be reached.
    """


class DeploymentControllerConnectionError(NetworkError):
    """
    Raised when the Deployment Controller cannot be contacted.
    """


# =============================================================================
# Deployment Controller
# =============================================================================


class DeploymentControllerError(OrionError):
    """
    Base class for Deployment Controller failures.
    """


class AuthenticationError(DeploymentControllerError):
    """
    Raised when authentication fails.
    """


class AuthorizationError(DeploymentControllerError):
    """
    Raised when authorization fails.
    """


class NodeRegistrationError(DeploymentControllerError):
    """
    Raised when a node cannot be registered.
    """


# =============================================================================
# Inventory
# =============================================================================


class InventoryError(OrionError):
    """
    Base class for inventory failures.
    """


# =============================================================================
# Benchmark
# =============================================================================


class BenchmarkError(OrionError):
    """
    Base class for benchmark failures.
    """


class BenchmarkTimeoutError(BenchmarkError):
    """
    Raised when a benchmark exceeds its allowed execution time.
    """


# =============================================================================
# Filesystem
# =============================================================================


class FileSystemError(OrionError):
    """
    Base class for filesystem failures.
    """


class DirectoryCreationError(FileSystemError):
    """
    Raised when a required directory cannot be created.
    """


class FileOperationError(FileSystemError):
    """
    Raised when a filesystem operation fails.
    """