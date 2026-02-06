"""Environment validation utilities for NBReport."""

from typing import Any
from typing import Optional

import IPython


def get_ipython_safe() -> Optional[Any]:
    """Return the currently active IPython interactive shell instance."""
    return IPython.get_ipython()  # type: ignore


def check_ipython(err_msg: str = "Not running in a Jupyter notebook.") -> None:
    """Check code is running inside an IPython (Jupyter) environment."""
    assert get_ipython_safe() is not None, err_msg
