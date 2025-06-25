# License: MIT
# Copyright © 2025 Frequenz Energy-as-a-Service GmbH

"""Common fixtures and utilities for testing."""

from collections.abc import AsyncIterator, Iterator
from contextlib import AsyncExitStack, ExitStack

import pytest


@pytest.fixture
def stack() -> Iterator[ExitStack]:
    """Provide an ExitStack fixture for managing resources."""
    with ExitStack() as stack:
        yield stack


@pytest.fixture
async def astack() -> AsyncIterator[AsyncExitStack]:
    """Provide an AsyncExitStack fixture for managing resources."""
    async with AsyncExitStack() as stack:
        yield stack
