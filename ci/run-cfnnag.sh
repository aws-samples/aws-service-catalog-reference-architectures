#!/bin/bash
shopt -s nullglob
for f in {ec2,iam}/*.{json,yml} ; do
    if cfn_nag_scan --input-path "$f"; then
        echo "$f PASSED"
    else
        echo "$f FAILED"
        touch FAILED
    fi
done

if [ -e FAILED ]; then
  echo cfn-nag FAILED at least once!
  exit 1
else
  echo cfn-nag Passed on all files!
  exit 0
fi