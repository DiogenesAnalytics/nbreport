"""Tests for nbreport.checks module."""

import pytest
from pytest import MonkeyPatch

from nbreport import checks


def test_get_ipython_safe_returns_none_when_not_in_ipython(
    monkeypatch: MonkeyPatch,
) -> None:
    """Ensure get_ipython_safe returns None outside IPython."""
    monkeypatch.setattr("IPython.get_ipython", lambda: None)
    assert checks.get_ipython_safe() is None


def test_check_ipython_raises_assert(monkeypatch: MonkeyPatch) -> None:
    """Ensure check_ipython raises an AssertionError outside IPython."""
    monkeypatch.setattr("IPython.get_ipython", lambda: None)
    with pytest.raises(AssertionError):
        checks.check_ipython()
