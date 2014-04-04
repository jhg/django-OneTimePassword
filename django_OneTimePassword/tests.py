from django.test import TestCase
from django_OneTimePassword.gen_password import sha512TS


#class gen_password_test(TestCase):
#    def test_sha512TS_gen_user_seed(self):
#        """
#        Tests seed generate by sha512TS.
#        """
#        instance = sha512TS()
#        seed = instance.get_user_seed(
#            "admin",
#            length=6,
#            interval=30,
#            dictionary="abcdefghijklmnopqrstuvwxyz0123456789"
#        )
#        self.assertEqual(
#            seed,
#            ADMIN_SEED
#        )
