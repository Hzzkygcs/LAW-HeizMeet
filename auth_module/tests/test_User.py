from django.test import TestCase

from auth_module.models.User import User


class TestUser(TestCase):

    def setUp(self) -> None:
        self.email = "b"
        self.password = "passw"
        user = User.objects.create(email=self.email)
        user.password = self.password
        self.user = user

    def test_object_saved_successfully(self):
        User.objects.create(email="a", _password=b'b')
        user = User.objects.get(email="a")
        self.assertIsNotNone(user)
        self.assertEqual(user.email, 'a')
        self.assertEqual(user.password, b'b')

    def test_password_should_not_be_stored_as_plaintext(self):
        self.assertNotEqual(self.user.password, self.password)
        self.assertNotEqual(self.user._password, self.password)

    def test__is_password_valid__should_return_false_if_password_not_equal(self):
        wrong_password = self.password + "a"
        self.assertFalse(self.user.is_password_valid(wrong_password))

    def test__is_password_valid__should_return_true_if_password_is_equal(self):
        self.assertTrue(self.user.is_password_valid(self.password))