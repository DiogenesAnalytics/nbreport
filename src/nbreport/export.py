"""Notebook export utilities for NBReport."""

import datetime
from pathlib import Path
from typing import Optional
from typing import Union

import traitlets.config
from nbconvert.exporters import PDFExporter


def export_pdf(
    nb_path: Union[str, Path],
    debug: bool = False,
    output_dir: Optional[Union[str, Path]] = None,
    template_name: Optional[str] = None,
    template_dir: Optional[Union[str, Path]] = None,
) -> None:
    """Generate a PDF report from a Jupyter notebook using nbconvert."""
    # guarantee nb path is not str
    nb_path = Path(nb_path)

    # default output directory
    output_dir = Path(output_dir) if output_dir is not None else Path.cwd()
    output_dir.mkdir(parents=True, exist_ok=True)

    # configure nbconvert
    config = traitlets.config.Config()
    config.PDFExporter.update(
        {
            "exclude_input_prompt": True,
            "exclude_output_prompt": True,
            "verbose": debug,
        }
    )

    # enable tag-based cell removal
    config.TagRemovePreprocessor.enabled = True
    config.TagRemovePreprocessor.remove_cell_tags = ("remove_cell",)
    config.TagRemovePreprocessor.remove_input_tags = ("remove_input",)

    config.PDFExporter.preprocessors = ["nbconvert.preprocessors.TagRemovePreprocessor"]

    # override templates if requested
    if template_name is not None:
        config.TemplateExporter.template_name = template_name
        if template_dir is not None:
            config.TemplateExporter.extra_template_basedirs = [str(template_dir)]

    # create exporter
    exporter = PDFExporter(config=config)  # type: ignore

    # run conversion
    pdf_data, _metadata = exporter.from_filename(str(nb_path))

    # generate timestamped output filename
    dt_stamp = datetime.datetime.now().strftime("%y%m%d%H%M%S")
    pdf_name = f"{nb_path.name}.{dt_stamp}.pdf"
    pdf_full_path = output_dir / pdf_name

    # write pdf data
    pdf_full_path.write_bytes(pdf_data)  # type: ignore
