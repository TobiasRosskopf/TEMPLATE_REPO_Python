#!/usr/bin/env bash

pipenv lock --requirements > requirements.txt
pipenv lock  --dev-only --requirements > requirements-dev.txt
