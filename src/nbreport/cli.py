"""Command-line interface for NBReport."""

from pathlib import Path
from typing import Optional
from typing import Tuple

import click

from .export import export_pdf

EXPORT_FUNCTIONS = {
    "pdf": export_pdf,
    # "html": export_html,
    # "markdown": export_markdown,
}


@click.command()
@click.argument(
    "notebooks",
    type=click.Path(exists=True, dir_okay=False, path_type=Path),
    nargs=-1,
    required=True,
)
@click.option(
    "--output",
    "-o",
    type=click.Path(file_okay=False, path_type=Path),
    default=Path.cwd(),
    show_default=True,
    help="Directory to save reports",
)
@click.option(
    "--template",
    "-t",
    default=None,
    help="nbconvert template name (defaults to Jupyter PDF template)",
)
@click.option(
    "--template-dir",
    "-d",
    type=click.Path(file_okay=False, path_type=Path),
    default=None,
    help="Directory containing nbconvert templates",
)
@click.option(
    "--export-type",
    "-f",
    type=click.Choice(EXPORT_FUNCTIONS.keys(), case_sensitive=False),
    default="pdf",
    show_default=True,
    help="Format to export notebook",
)
@click.option(
    "--debug",
    is_flag=True,
    help="Enable verbose output",
)
def cli(
    notebooks: Tuple[Path, ...],
    output: Path,
    template: Optional[str],
    template_dir: Optional[Path],
    export_type: str,
    debug: bool,
) -> None:
    """Convert one or more Jupyter notebooks to reports."""
    # guard against only template_dirs being passed
    if template_dir and not template:
        raise click.UsageError("--template-dir requires --template")

    # get exporter
    export_func = EXPORT_FUNCTIONS[export_type.lower()]

    # loop over each nb
    for nb_path in notebooks:
        # notify
        click.echo(f"Exporting {nb_path.name!r} as {export_type.upper()}...")

        # export
        export_func(
            nb_path=str(nb_path),
            output_dir=str(output),
            template_name=template,
            template_dir=str(template_dir) if template_dir else None,
            debug=debug,
        )

    # ... finished
    click.echo("Export complete.")


if __name__ == "__main__":
    cli()
