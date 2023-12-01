import sys
from importlib import import_module
from os import sep, remove
from os.path import join, exists
from shutil import copyfile, move
from inspect import getmembers, isclass
from typing import Tuple
import libcst as cst
import pytest

from dynapyt.instrument.instrument import instrument_file
from dynapyt.utils.hooks import get_hooks_from_analysis
from dynapyt.analyses.BaseAnalysis import BaseAnalysis


def correct_output(expected: str, actual: str) -> bool:
    if actual == expected or actual == expected + "\n":
        return True
    expected_lines = expected.split("\n")
    actual_lines = actual.split("\n")
    expected_trimmed = "\n".join([l for l in expected_lines if l.strip() != ""])
    actual_trimmed = "\n".join([l for l in actual_lines if l.strip() != ""])
    expected_ast = cst.parse_module(expected_trimmed)
    actual_ast = cst.parse_module(actual_trimmed)
    return expected_ast.deep_equals(actual_ast)


def test_runner(directory_pair: Tuple[str, str], capsys):
    abs_dir, rel_dir = directory_pair
    import dynapyt.runtime as _rt

    # gather hooks used by the analysis
    module_prefix = rel_dir.replace(sep, ".")
    if module_prefix.startswith("milestone2"):
        module_name = "dynamicslicing.slice_dataflow"
    elif module_prefix.startswith("milestone3"):
        module_name = "dynamicslicing.slice"
    else:
        pytest.fail(f"Could not determine module name for {rel_dir}")
    module = import_module(module_name)
    analysis_classes = getmembers(
        module, lambda c: isclass(c) and issubclass(c, BaseAnalysis) and c is not BaseAnalysis
    )

    # instrument
    program_file = join(abs_dir, "program.py")
    orig_program_file = join(abs_dir, "program.py.orig")
    # make sure to instrument the uninstrumented version
    with open(program_file, "r") as file:
        src = file.read()
        if "DYNAPYT: DO NOT INSTRUMENT" in src:
            if not exists(orig_program_file):
                pytest.fail(f"Could find only the instrumented program in {rel_dir}")
            copyfile(orig_program_file, program_file)

    selected_hooks = get_hooks_from_analysis([f"{module_name}.{ac[0]}:{program_file}" for ac in analysis_classes])

    instrument_file(program_file, selected_hooks)

    analysis_instances = [class_[1](orig_program_file) for class_ in analysis_classes]

    # analyze
    _rt.analyses = None
    _rt.set_analysis(analysis_instances)
    captured = capsys.readouterr()  # clear stdout
    # print(f"Before analysis: {captured.out}")  # for debugging purposes
    for analysis_instance in analysis_instances:
        if hasattr(analysis_instance, "begin_execution"):
            analysis_instance.begin_execution()
    import_module(f"{module_prefix}.program")
    _rt.end_execution()
    del sys.modules["dynapyt.runtime"]
    del _rt

    # check output
    expected_file = join(abs_dir, "expected.py")
    with open(expected_file, "r") as file:
        expected = file.read()

    captured = (
        capsys.readouterr()
    )  # read stdout produced by running the analyzed program
    # print(f"After analysis: {captured.out}")  # for debugging purposes
    with open(join(abs_dir, "sliced.py"), "r") as file:
        actual = file.read()
    if not correct_output(expected, actual):
        pytest.fail(
            f"Output of {rel_dir} does not match expected output.\n--> Expected:\n{expected}\n--> Actual:\n{actual}"
        )

    # restore uninstrumented program and remove temporary files
    move(orig_program_file, program_file)
    remove(join(abs_dir, "program-dynapyt.json"))
    remove(join(abs_dir, "sliced.py"))
