class DomainError(Exception):
    """Base class for all domain-specific errors."""
    pass


class AuthenticationError(DomainError):
    """Raised when user credentials are invalid."""
    def __init__(self, message: str = "Invalid credentials"):
        super().__init__(message)


class PermissionDenied(DomainError):
    """Raised when a user attempts an unauthorized action."""
    def __init__(self, message: str = "Permission denied"):
        super().__init__(message)


class ResourceNotFound(DomainError):
    """Raised when an entity is not found in the system."""
    def __init__(self, resource: str = "Resource"):
        message = f"{resource} not found"
        super().__init__(message)