from os import makedirs
from os.path import join

import nbformat
from nbconvert.preprocessors import ExecutePreprocessor, CellExecutionError


def get_default_dir_name():
    return "executed"


def get_output_filename(notebook_filename):
    return join(".", get_default_dir_name(), notebook_filename)


def get_error_filename(output_filename):
    from datetime import datetime
    from os.path import dirname, basename
    return join(dirname(output_filename), f"Error_{datetime.now()}_{basename(output_filename)}")


def execute_notebook(notebook_filename, kernel_name="python3", path=".", timeout=None):
    makedirs(get_default_dir_name(), exist_ok=True)

    with open(notebook_filename) as file:
        nb = nbformat.read(file, as_version=4)

    ep = ExecutePreprocessor(timeout=timeout, kernel_name=kernel_name)
    
    output_filename = get_output_filename(notebook_filename)
    
    try:
        ep.preprocess(nb, {"metadata": {"path": path}})
    except CellExecutionError:
        output_filename = get_error_filename(output_filename)
        raise
    finally:
        with open(output_filename, "w", encoding="utf-8") as file:
            nbformat.write(nb, file)
