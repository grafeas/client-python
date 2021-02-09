#!/usr/bin/env bash

set -euo pipefail

wget https://github.com/grafeas/grafeas/raw/master/proto/v1alpha1/swagger/grafeas.swagger.json -O grafeas.swagger.json

wget https://repo1.maven.org/maven2/io/swagger/swagger-codegen-cli/2.4.18/swagger-codegen-cli-2.4.18.jar -O swagger-codegen-cli.jar

java -jar ./swagger-codegen-cli.jar generate -i ./grafeas.swagger.json -l python -o ./ -c ./config.py.json
