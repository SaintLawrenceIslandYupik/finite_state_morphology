#!/bin/bash

foma -f yupiktest.foma 2> /dev/null | grep -v "^defined" | grep -v "^Root" | grep -v " states," | sort
