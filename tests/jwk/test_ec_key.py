from unittest import TestCase
from joserfc.jwk import ECKey
from tests.keys import read_key


class TestECKey(TestCase):
    def run_import_key(self, name):
        public_pem = read_key(f"ec-{name}-public.pem")
        key1 = ECKey.import_key(public_pem)
        self.assertEqual(key1.is_private, False)

        private_pem = read_key(f"ec-{name}-private.pem")
        key2 = ECKey.import_key(private_pem)
        self.assertEqual(key2.is_private, True)

        # public key match
        self.assertEqual(
            key2.as_bytes(private=False),
            key1.as_bytes(private=False),
        )

        self.assertNotIn("d", key1.dict_value)
        self.assertIn("d", key2.dict_value)

    def test_import_p256_key(self):
        self.run_import_key("p256")

    def test_import_p384_key(self):
        self.run_import_key("p384")

    def test_import_p512_key(self):
        self.run_import_key("p512")

    def test_import_secp256k1_key(self):
        self.run_import_key("secp256k1")

    def test_generate_key(self):
        self.assertRaises(ValueError, ECKey.generate_key, "Invalid")

        key: ECKey = ECKey.generate_key(private=False)
        self.assertFalse(key.is_private)
        self.assertIsNone(key.private_key)
