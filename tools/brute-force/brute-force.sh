#!/bin/bash

# A simple brute force script

if [ -z "$1" ] || [ -z "$2" ]; then
    echo "Usage: $0 <target> <wordlist>"
    exit 1
fi

target=$1
wordlist=$2

echo "Brute-forcing target: $target with wordlist: $wordlist"
while read -r password; do
    echo "Trying password: $password"
    # Simulate brute force logic
    # Example: sshpass -p $password ssh user@$target
done < "$wordlist"
