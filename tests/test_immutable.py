"""Unit tests for Immutable."""

import unittest

from src.immutable import Immutable


class ImmutableTestCase(unittest.TestCase):  # noqa: D101
    def test_should_get_attr(self):  # noqa: D102
        obj = Immutable()

        obj.test = 'test'

        self.assertEquals('test', obj.test)

    def test_should_get_raise_attribute_error_when_attr_is_set_twice(self):  # noqa: D102
        obj = Immutable()

        obj.test = 'test'

        with self.assertRaises(AttributeError):
            obj.test = 'new'

    def test_should_get_none_when_attr_is_not_set(self):  # noqa: D102
        obj = Immutable()

        self.assertEquals(None, obj.test)

    def test_should_convert_to_dict(self):  # noqa: D102
        obj = Immutable()

        obj.a = 'a'
        obj.b = 'b'

        dict = obj.to_dict()

        self.assertIn('a', dict)
        self.assertIn('b', dict)
        self.assertEquals(obj.a, dict['a'])
        self.assertEquals(obj.b, dict['b'])