import unittest
import proc_address_clip
import proc_address_sysarg


class TestClass(unittest.TestCase):
    def adrress_cannot_be_empty_from_clip(self):
        address = proc_address_clip.get_address()
        unittest.assertFalse(len(address) == 0)

    def address_cannot_be_empty_from_sysarg(self):
        address = proc_address_sysarg.get_address()
        unittest.assertFalse(len(address) == 0)
