#!/bin/bash

if [ $# -eq 0 ]; then
  echo "No version provided"
  exit 1
fi

ansible-builder build --file builder/${1}/execution-environment.yml --context builder/${1}/context --tag ansible-execution-env:${1} -vvv
