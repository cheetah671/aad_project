#!/bin/bash
# Script to check progress of the test suite

cd /home/arnav-agnihotri/Downloads/AAD_CP

echo "=== Test Suite Progress ==="
echo ""

# Check if process is still running
if pgrep -f "run_all.py" > /dev/null; then
    echo "Status: RUNNING ✓"
else
    echo "Status: COMPLETED or NOT RUNNING"
fi

echo ""
echo "=== Last 20 lines of log ==="
tail -20 run_all.log

echo ""
echo "=== Test Results So Far ==="
if [ -f "outputs/results.csv" ]; then
    echo "Total tests completed: $(tail -n +2 outputs/results.csv 2>/dev/null | wc -l)"
    echo ""
    echo "Results by algorithm:"
    tail -n +2 outputs/results.csv 2>/dev/null | cut -d',' -f1 | sort | uniq -c
fi

echo ""
echo "To view full log: tail -f run_all.log"
echo "To stop tests: pkill -f run_all.py"
