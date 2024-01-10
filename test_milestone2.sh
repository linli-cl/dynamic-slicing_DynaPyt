#!/bin/bash

TEST_DIR="tests/milestone2"

for ((i=1; i<=12; i++)); do
    TEST_PATH="$TEST_DIR/test_$i"

    INSTRUMENT_CMD="python -m dynapyt.instrument.instrument --analysis src.dynamicslicing.slice_dataflow.SliceDataflow:\"$TEST_PATH/program.py\" --files \"$TEST_PATH/program.py\""
    RUN_ANALYSIS_CMD="python -m dynapyt.run_analysis --analysis src.dynamicslicing.slice_dataflow.SliceDataflow:\"$TEST_PATH/program.py.orig\" --entry \"$TEST_PATH/program.py\""

    echo "Running test_$i..."
    echo "Instrument command: $INSTRUMENT_CMD"
    eval "$INSTRUMENT_CMD"

    echo "Run analysis command: $RUN_ANALYSIS_CMD"
    eval "$RUN_ANALYSIS_CMD"

    echo "--------------------"
done
