"""Notebook hashing utilities for NBReport."""

import hashlib
from pathlib import Path
from typing import Union

from ._constants import BUFF_SIZE


def hash_notebook(nb_path: Union[Path, str], chunked: bool = False) -> str:
    """Generate a SHA-512 hash of a Jupyter notebook file."""
    path = Path(nb_path)

    if not chunked:
        return hashlib.sha512(path.read_bytes()).hexdigest()

    sha512 = hashlib.sha512()
    with path.open("rb") as f:
        while chunk := f.read(BUFF_SIZE):
            sha512.update(chunk)
    return sha512.hexdigest()
