#!/bin/bash

echo "testpassword" > test_wordlist.txt
./tools/brute-force/brute-force.sh test_target test_wordlist.txt > test_output.txt

if grep -q "Trying password: testpassword" test_output.txt; then
    echo "Brute force test passed!"
else
    echo "Brute force test failed!"
fi
