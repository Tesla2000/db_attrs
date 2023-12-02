import unittest
from dataclasses import dataclass

from src.db_classes import int8, int16, int32, int64, DbClass


@dataclass
class Foo(DbClass):
    a: int8 | int
    b: int16 | int
    c: int32 | int
    d: int64 | int


class TestFooClass(unittest.TestCase):
    def setUp(self):
        self.foo_instance = Foo(0, 0, 0, 0)

    def test_attribute_a(self):
        with self.assertRaises(ValueError):
            self.foo_instance.a = -129  # Below int8 range
        with self.assertRaises(ValueError):
            self.foo_instance.a = 128  # Above int8 range

    def test_attribute_b(self):
        with self.assertRaises(ValueError):
            self.foo_instance.b = -32769  # Below int16 range
        with self.assertRaises(ValueError):
            self.foo_instance.b = 32768  # Above int16 range

    def test_attribute_c(self):
        with self.assertRaises(ValueError):
            self.foo_instance.c = -2147483649  # Below int32 range
        with self.assertRaises(ValueError):
            self.foo_instance.c = 2147483648  # Above int32 range

    def test_attribute_d(self):
        with self.assertRaises(ValueError):
            self.foo_instance.d = -9223372036854775809  # Below int64 range
        with self.assertRaises(ValueError):
            self.foo_instance.d = 9223372036854775808  # Above int64 range

    def test_attribute_a_positive(self):
        self.foo_instance.a = 50
        self.assertEqual(self.foo_instance.a, 50)

    def test_attribute_b_positive(self):
        self.foo_instance.b = -15000
        self.assertEqual(self.foo_instance.b, -15000)

    def test_attribute_c_positive(self):
        self.foo_instance.c = 2000000000
        self.assertEqual(self.foo_instance.c, 2000000000)

    def test_attribute_d_positive(self):
        self.foo_instance.d = -50000000000000000
        self.assertEqual(self.foo_instance.d, -50000000000000000)


if __name__ == '__main__':
    unittest.main()
