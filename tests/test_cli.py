"""Tests for nbreport.cli module."""

from pathlib import Path
from typing import Any
from typing import Callable
from typing import Dict
from typing import Tuple

from click.testing import CliRunner
from pytest import MonkeyPatch

from nbreport import cli
from nbreport import export


def test_cli_exports_pdf(
    tmp_notebook: Path,
    monkeypatch: MonkeyPatch,
    fake_converter: Tuple[Callable[..., None], Dict[str, Any]],
) -> None:
    """Check that CLI command invokes the PDF exporter correctly."""
    export_func, called = fake_converter
    monkeypatch.setattr(export, "export_pdf", export_func)

    runner = CliRunner()
    result = runner.invoke(cli.cli, [str(tmp_notebook)])

    assert result.exit_code == 0
    assert called.get("called") is True
    assert Path(called["path"]) == tmp_notebook
