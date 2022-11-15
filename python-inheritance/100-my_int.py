#!/usr/bin/python3
"""Defines a class MyInt that inherits from int."""


class MyInt(int):
    """Invert int operators == and !=."""

    def __eq__(self, value):
        """overrides == operator with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Overrides != with == behavior"""
        return self.real == value
