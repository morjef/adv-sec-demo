# Example 4: Path traversal
import os
def read_file(filename):
  with open(filename, "r") as f: # Vulnerable line
    return f.read()
