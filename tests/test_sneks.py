"""
Tests for checking that sneks specific functions are working.
"""

from curriculum_sneks.sneks import *
from curriculum_sneks.files import *

class Test:
    def test_only_printing_variables(self):
        with Execution('a,b=0,1\nprint(a,b)') as e:
            self.assertTrue(only_printing_variables())
        with Execution('print(0,"True", True)') as e:
            self.assertFalse(only_printing_variables())
        with Execution('print(True)') as e:
            self.assertFalse(only_printing_variables())