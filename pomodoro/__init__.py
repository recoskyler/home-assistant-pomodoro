"""
This module provides functions for calculating and printing hours, as well as outputting YAML data.

Functions:
- calculate_hours: Calculates the total hours based on input data.
- print_hours: Prints the calculated hours.
- output_yaml: Outputs the calculated hours in YAML format.
"""

from .calculator import calculate_hours
from .printer import print_hours
from .yaml import output_yaml

__all__ = ["calculate_hours", "print_hours", "output_yaml"]
