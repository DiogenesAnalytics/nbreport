"""Pytest fixtures for NBReport tests."""

from pathlib import Path
from typing import Any
from typing import Callable
from typing import Dict
from typing import Tuple

import pytest


@pytest.fixture
def tmp_notebook(tmp_path: Path) -> Path:
    """Fixture that creates a temporary notebook file for testing."""
    nb_file = tmp_path / "test_notebook.ipynb"
    nb_file.write_bytes(b"{}")  # minimal empty notebook content
    return nb_file


@pytest.fixture
def fake_converter() -> Tuple[Callable[..., None], Dict[str, Any]]:
    """Fixture that provides a fake converter function and a call-tracking dict."""
    called: Dict[str, Any] = {}

    def converter(nb_path: Path, **kwargs: Any) -> None:
        """Fake converter that records its call arguments."""
        called["called"] = True
        called["path"] = nb_path
        called["kwargs"] = kwargs

    return converter, called
