#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-

"""
**Created:**    ??.??.2022
**Modified:**   ??.??.2022

**Authors:**    [Tobias Rosskopf](mailto:tobirosskopf@gmail.com)

Unit tests for cli module
"""

import pytest
from click.testing import CliRunner

from package_name import cli


class TestCLI:
    """
    Unit tests for the command line interface
    """
    @pytest.fixture()
    def cli_runner_instance(self) -> CliRunner:
        """
        Fixture for CliRunner instance

        Returns:
            CliRunner: Instance of CliRunner
        """
        return CliRunner()

    def test_cli(self, cli_runner_instance: CliRunner) -> None:
        """
        Tests the command line interface.

        Args:
            cli_runner_instance (CliRunner): Instance of CliRunner
        """
        result = cli_runner_instance.invoke(cli.main, ["."])
        assert result.exit_code == 0
        assert "Erfolgreich ausgeführt!" in result.output

    def test_cli_no_input(self, cli_runner_instance: CliRunner) -> None:
        """
        Tests the command line interface with no input.

        Args:
            cli_runner_instance (CliRunner): Instance of CliRunner
        """
        result = cli_runner_instance.invoke(cli.main)
        assert result.exit_code == 2
        assert "Error: Missing argument 'INPUT_PATH'." in result.output

    def test_cli_help(self, cli_runner_instance: CliRunner):
        """
        Tests the help dialog of the command line interface.
        """
        result = cli_runner_instance.invoke(cli.main, ["--help"])
        assert result.exit_code == 0
        assert "--help  Show this message and exit." in result.output
