from unittest import TestCase

from auth_module.core.SaltFactory import SaltFactory


class TestSaltFactory(TestCase):
    def setUp(self) -> None:
        self.factory = SaltFactory()

    def test_generate_salt__should_return_correct_length(self):
        length = 10
        res = self.factory.generate_salt(length)
        self.assertEqual(length, len(res))

    def test_generate_salt__should_return_randomly(self):
        length = 15
        res1 = self.factory.generate_salt(length)
        res2 = self.factory.generate_salt(length)
        self.assertNotEqual(res1, res2)
