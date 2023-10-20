from typing_extensions import Protocol, Self
from typing import TypeVar, Iterable, Optional as Op, Union as U


T = TypeVar("T", covariant=True)


class _GetItem(Protocol[T]):
    """typing class used for schema_iter"""

    def __getitem__(self: Self, i: int) -> T:
        raise NotImplementedError


def schema_iter(val: _GetItem[T]) -> Iterable[T]:
    """typing helper"""
    return val


class APIError(Exception):
    def __init__(self, message: str, status: int) -> None:
        super().__init__(self, message)
        self.status = status


class Exit(BaseException):
    """exit program without printing exception"""

    pass
