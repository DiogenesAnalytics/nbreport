"""Tests for nbreport.export module."""

from pathlib import Path

from nbreport import export


def test_export_pdf_creates_file(tmp_notebook: Path, tmp_path: Path) -> None:
    """Check that export_pdf generates a PDF file in the specified directory."""
    # Use a subdirectory for output
    output_dir = tmp_path / "reports"

    export.export_pdf(tmp_notebook, output_dir=output_dir, debug=True)

    # There should be exactly one PDF file in the output_dir
    pdf_files = list(output_dir.glob("*.pdf"))
    assert len(pdf_files) == 1
    assert pdf_files[0].suffix == ".pdf"
    assert tmp_notebook.stem in pdf_files[0].name
