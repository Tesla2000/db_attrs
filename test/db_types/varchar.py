import unittest
from dataclasses import dataclass

from src.db_classes import DbClass, varchar, text


@dataclass
class Foo(DbClass):
    a: varchar(5)
    b: varchar(6)
    c: varchar(7)
    d: varchar(8)
    e: text



class TestFooClass(unittest.TestCase):
    def setUp(self):
        self.foo_instance = Foo()

    # Negative tests - ValueErrors on out-of-range assignments
    def test_attribute_a_out_of_range(self):
        with self.assertRaises(ValueError):
            self.foo_instance.a = "Too long string"  # Exceeds varchar(5) length

    def test_attribute_b_out_of_range(self):
        with self.assertRaises(ValueError):
            self.foo_instance.b = "Too long"  # Exceeds varchar(6) length

    def test_attribute_c_out_of_range(self):
        with self.assertRaises(ValueError):
            self.foo_instance.c = "Too biggg"  # Exceeds varchar(7) length

    def test_attribute_d_out_of_range(self):
        with self.assertRaises(ValueError):
            self.foo_instance.d = "Exceeded limit"  # Exceeds varchar(8) length

    def test_attribute_e_wrong_type(self):
        with self.assertRaises(ValueError):
            self.foo_instance.e = 1

    # Positive tests - Valid assignments within range
    def test_attribute_a_positive(self):
        self.foo_instance.a = "Hello"
        self.assertEqual(self.foo_instance.a, "Hello")

    def test_attribute_b_positive(self):
        self.foo_instance.b = "Greet1"
        self.assertEqual(self.foo_instance.b, "Greet1")

    def test_attribute_c_positive(self):
        self.foo_instance.c = "World23"
        self.assertEqual(self.foo_instance.c, "World23")

    def test_attribute_d_positive(self):
        self.foo_instance.d = "Testing4"
        self.assertEqual(self.foo_instance.d, "Testing4")

    def test_attribute_e_positive(self):
        passed_text = """I'm the Scatman
Ski-bi dibby dib yo da dub dub
Yo da dub dub
Ski-bi dibby dib yo da dub dub
Yo da dub dub
(I'm the Scatman)
Ski-bi dibby dib yo da dub dub
Yo da dub dub
Ski-bi dibby dib yo da dub dub
Yo da dub dub
Ba-da-ba-da-ba-be bop bop bodda bope
Bop ba bodda bope
Be bop ba bodda bope
Bop ba bodda
Ba-da-ba-da-ba-be bop ba bodda bope
Bop ba bodda bope
Be bop ba bodda bope
Bop ba bodda bope"""
        self.foo_instance.e = passed_text
        self.assertEqual(self.foo_instance.e, passed_text)

if __name__ == '__main__':
    unittest.main()

