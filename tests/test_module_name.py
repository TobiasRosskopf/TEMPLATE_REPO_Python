#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-

"""
**Created:**    ??.??.2022
**Modified:**   ??.??.2022

**Authors:**    [Tobias Rosskopf](mailto:tobirosskopf@gmail.com)

Unit tests for <module_name>
"""

import pytest

from package_name.module_name import ClassName


class TestClassName:
    """
    Unit tests for <ClassName>
    """

    @pytest.fixture()
    def class_name_instance(self):
        """
        Fixture for <ClassName> instance

        Returns:
            <ClassName>: Instance of Classname
        """
        return ClassName()

    def test_init(self, class_name_instance: ClassName):
        """
        Tests <ClassName>'s instroctor

        Args:
            class_name_instance (<ClassName>): Instance of Classname
        """
        assert class_name_instance.name == ""

    def test_repr(self, class_name_instance: ClassName):
        """
        Tests REPL representation

        Args:
            class_name_instance (<ClassName>): Instance of Classname
        """
        assert repr(class_name_instance) == "ClassName()"

    def test_str(self, class_name_instance: ClassName):
        """
        Tests string representation

        Args:
            class_name_instance (<ClassName>): Instance of Classname
        """
        assert str(class_name_instance) == ""

    def test_eq(self, class_name_instance: ClassName):
        """
        Tests equality check

        Args:
            class_name_instance (<ClassName>): Instance of Classname
        """
        assert class_name_instance == ClassName()

    def test_not_eq(self, class_name_instance: ClassName):
        """
        Tests not equality check

        Args:
            class_name_instance (<ClassName>): Instance of Classname
        """
        assert class_name_instance != ClassName("test")

    def test_not_instance(self, class_name_instance: ClassName):
        """
        Tests not equality check

        Args:
            class_name_instance (<ClassName>): Instance of Classname
        """
        assert class_name_instance != "test"
