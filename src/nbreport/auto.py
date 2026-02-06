"""Notebook automation for NBReport."""

from typing import Any
from typing import Callable
from typing import Dict

import ipynbname
from IPython.display import clear_output

from .checks import check_ipython
from .export import export_pdf
from .hashing import hash_notebook


def auto_convert(
    nb_globals: Dict[str, Any],
    auto: bool = True,
    force: bool = False,
    converter: Callable[..., None] = export_pdf,
    **kwargs: Any,
) -> None:
    """Auto export a notebook when it has changed since last conversion."""
    # check that function is called from inside notebook
    check_ipython("auto_convert is designed to run in a Jupyter notebook only.")

    # get path to notebook
    nb_path = ipynbname.path().as_posix()

    # check previous hash
    if "NB_HASH" in nb_globals and (auto or force):
        fresh_nb_hash = hash_notebook(nb_path)
        if fresh_nb_hash != nb_globals["NB_HASH"] or force:
            print(f"Notebook path to be converted: {nb_path}")
            converter(nb_path, **kwargs)
            if not kwargs.get("debug", False):
                clear_output()  # type: ignore

    # update notebook hash
    nb_globals["NB_HASH"] = hash_notebook(nb_path)
