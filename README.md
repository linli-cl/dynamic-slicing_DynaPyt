# dynamicslicing

## Installation

```console
pip install -r requirements.txt
pip install -e .
```

## Project Goals

The project aims to extract a subset of code from a given Python program that is relevant to specific
slicing criteria through dynamic analysis techniques. The scope of the analysis is within the execution
of a Python function.

The analysis of this project is mainly divided into two milestones, data flow slicing and data flow plus
control flow slicing. 

## Tools used
*DynaPyt*: This library provides a set of hooks for capturing different runtime events during program execution, such as variable reading and writing, Boolean expressions, and conditional judgments. The capture of these events provides the basis for dynamic slicing analysis. When using DynaPyt, the code needs to be instrumented first and then analyzed.

*LibCST*: This library provides operations on Python AST(Abstract Syntax Tree), making code parsing, manipulating and reprinting easier.

## Results
Multiple test cases are stored in the tests folder. The original folder of each test case contains program.py and expected.py, which store the original program code and the expected program code after slicing respectively.

After execution: The original code is transferred to program.py.orig. Automatically generate program-dynapyt.json and program.py instrumented files required for slicing. And get the sliced results in sliced.py.

The results show that All test examples were successfully sliced.

Please see "report_Application_of_dynamic_slicing_analysis_in_Python.pdf" for a more detailed project description.
