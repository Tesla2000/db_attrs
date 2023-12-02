from dataclasses import dataclass, field

from src.db_classes import uint8, uint16, uint32, uint64, DbClass
import unittest


@dataclass
class Foo(DbClass):
    a: uint8 | int
    b: uint16 | int = field(default=uint16(2))
    c: uint32 | int
    d: uint64 | int


class TestFooClass(unittest.TestCase):
    def setUp(self):
        self.foo_instance = Foo(a=uint8(10))
        self.foo_instance.c = 111

    # Negative tests - ValueErrors on out-of-range assignments
    def test_attribute_a_out_of_range(self):
        with self.assertRaises(ValueError):
            self.foo_instance.a = -1  # Below uint8 range
        with self.assertRaises(ValueError):
            self.foo_instance.a = 256  # Above uint8 range

    def test_attribute_b_out_of_range(self):
        with self.assertRaises(ValueError):
            self.foo_instance.b = -1  # Below uint16 range
        with self.assertRaises(ValueError):
            self.foo_instance.b = 65536  # Above uint16 range

    def test_attribute_c_out_of_range(self):
        with self.assertRaises(ValueError):
            self.foo_instance.c = -1  # Below uint32 range
        with self.assertRaises(ValueError):
            self.foo_instance.c = 4294967296  # Above uint32 range

    def test_attribute_d_out_of_range(self):
        with self.assertRaises(ValueError):
            self.foo_instance.d = -1  # Below uint64 range
        with self.assertRaises(ValueError):
            self.foo_instance.d = 18446744073709551616  # Above uint64 range

    # Positive tests - Valid assignments within range
    def test_attribute_a_positive(self):
        self.foo_instance.a = 50
        self.assertEqual(self.foo_instance.a, 50)

    def test_attribute_b_positive(self):
        self.foo_instance.b = 15000
        self.assertEqual(self.foo_instance.b, 15000)

    def test_attribute_c_positive(self):
        self.foo_instance.c = 2000000000
        self.assertEqual(self.foo_instance.c, 2000000000)

    def test_attribute_d_positive(self):
        self.foo_instance.d = 50000000000000000
        self.assertEqual(self.foo_instance.d, 50000000000000000)


if __name__ == '__main__':
    unittest.main()
