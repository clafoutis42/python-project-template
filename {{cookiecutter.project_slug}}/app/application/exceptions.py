"""Application-level exceptions."""


class ApplicationError(Exception):
    """Base exception for application errors."""
    pass


class ValidationError(ApplicationError):
    """Raised when validation fails."""
    pass


class NotFoundError(ApplicationError):
    """Raised when a resource is not found."""
    pass