#!/bin/bash

cd $(dirname $0)

TESTCASES_DIR=test/integration

# Check environment.
echo "Environment information"
python --version
echo

for TESTCASE_NAME in `ls -1 ${TESTCASES_DIR}`; do
  TESTCASE_DIR=${TESTCASES_DIR}/${TESTCASE_NAME}
  SCHEMA_NAME=`ls -1 ${TESTCASE_DIR} | grep schema`
  DATA_NAME=`ls -1 ${TESTCASE_DIR} | grep data`
  SCHEMA_PATH=${TESTCASE_DIR}/${SCHEMA_NAME}
  DATA_PATH=${TESTCASE_DIR}/${DATA_NAME}

  echo "Testcase ${TESTCASE_NAME}:"
  python main.py -s $SCHEMA_PATH $DATA_PATH 
done
