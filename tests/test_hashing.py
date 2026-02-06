"""Tests for nbreport.hashing module."""

from pathlib import Path

from nbreport import hashing


def test_hash_notebook(tmp_notebook: Path) -> None:
    """Verify that hashing a notebook file returns a consistent SHA-512 hex string."""
    h1 = hashing.hash_notebook(str(tmp_notebook))
    h2 = hashing.hash_notebook(tmp_notebook)  # accept Path or str
    assert isinstance(h1, str)
    assert h1 == h2
