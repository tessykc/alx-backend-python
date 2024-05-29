#!/usr/bin/env python3
"""
unit test for utils.access_nested_map
TestAccessNestedMap class that inherits from unittest.TestCase
Implement the TestAccessNestedMap.test_access_nested_map method 
to test that the method returns 
"""


def access_nested_map(nested_map, path):
  """
  Accesses a value within a nested dictionary using a given path.

  Args:
      nested_map: A nested dictionary containing the data.
      path: A tuple representing the key sequence to reach the desired value.

  Returns:
      The value at the specified path within the nested map,
      or None if the path is invalid.

  Raises:
      TypeError: If the path is not a tuple.
  """

  if not isinstance(path, tuple):
    raise TypeError("Path must be a tuple of keys")

  current_level = nested_map
  for key in path:
    if key not in current_level:
      return None
    current_level = current_level[key]

  return current_level
