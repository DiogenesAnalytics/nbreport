"""Tests for nbreport.auto module."""

from pathlib import Path
from typing import Any
from typing import Callable
from typing import Dict
from typing import Tuple

import nbreport.auto as auto


def test_auto_convert_calls_converter(
    tmp_path: Path, fake_converter: Tuple[Callable[..., None], Dict[str, Any]]
) -> None:
    """Test that auto_convert calls the converter when forced."""
    converter, called = fake_converter

    # create temporary notebook
    nb_file = tmp_path / "test_notebook.ipynb"
    nb_file.write_bytes(b"{}")

    # create globals dict
    nb_globals: Dict[str, Any] = {}

    # call auto_convert with force=True
    auto.auto_convert(
        nb_globals,
        converter=converter,
        force=True,
        debug=True,
    )

    # assert converter was called
    assert called.get("called") is True
    assert Path(called["path"]).name == nb_file.name
