from unittest import TestCase
from joserfc.jws import serialize_compact, deserialize_compact
from joserfc.jwk import RSAKey
from ..util import read_key


class TestRS(TestCase):
    private_key = RSAKey.import_key(read_key("openssl-rsa-private.pem"))
    public_key = RSAKey.import_key(read_key("openssl-rsa-public.pem"))

    def run_compact(self, alg: str, expect: bytes):
        header = {'alg': alg}
        payload = b'hello'
        value = serialize_compact(header, payload, self.private_key, [alg])
        self.assertEqual(value, expect)

        obj = deserialize_compact(expect, self.public_key, [alg])
        self.assertEqual(obj.payload, payload)

    def test_compact_RS256(self):
        expect = (
            b'eyJhbGciOiJSUzI1NiJ9.aGVsbG8.'
            b'GVU8F9Ygp1fzFg8R1-cBj-o2x5cNVrbmuqGzw7haatCVBzVX4xojYkpxgr7Mpy59_XN9uJ2PAwmK6r3_7f1_wnT-lfgYXCuD-CdhNvkSCmaoAFivEGuU8i-5KdmfH0NFbNYFd2vyuFXPDAGzgydZsBOZt60FHMc06K_ddrTCPe2r7RMeJDksMInIIipI7wthqi6xug0E2WBow37-mu-dnvZ2a0W5w6MfhE5EM8oE8qVZ92jjNuEWpMrmD1in2x98LiZWvOIbkIUqh-rJZ_akMY8x4vIJ22TWNS9WjVW3TWvHpNWZWik-CfIYku1xPI1FZZN46RNVwCsGH3muBkG8Ok83p3ylu_Zz5H8UDZ9YhSV8_GjLBKE6lKujZ1NtbKDfm0sxPKMh2Mq1y4je6OD_VC87Ya7UelBUXGjK69_LxVXLBhPm9Rly6k9FemD0Di6zmNJZ4hnGHjIDkPqrGFBCe_s8Ve8Pltk5MFoPPN5zcDqB-D9n-w0WazOEYXP59WmTxA_nhKsqiunyWDXIYV6ThaJ12gUvOvnTndFCx84j4wbnglnbsVSwgOPojdgGflb7XgljV47lT-DW_BoBbBaC6lhSsnKBU28z89hXIfJfg1OqiGntAtt5duHWdRmFjaCX6udzOw7sIYnFXsS5LD2f8lo9TmgGO2JBG3mPiLA65JQ'
        )
        self.run_compact('RS256', expect)

    def test_compact_RS384(self):
        expect = (
            b'eyJhbGciOiJSUzM4NCJ9.aGVsbG8.'
            b'c647l2lFKP9gnmWQdBICAvmiTugZleIT8hAWVBhCcgiOBzyUS0HECbkmre2egUSbtl8PL2OlXqJER26641G2zVbCQqWvCG_9HxgbLmfB7980voN860yzyKYqSRMuxM9P_a6ZR4PBho6Ng63T4XStz8JB3v3vHnq2FjtJfhzmHSRUhtsbo4u9anqKyINfgfDh0BCfCGny6gXcXEyHOo0zaerhOpkq-qcp3sEmaPWzLvpF4IL6gv3tMgyfMBdDONGpb_UUYiJNnzEN1LDW39Sg3muewRekFv7DwuHJOCMYi_zipOlcMM4ONRXE-T9krvf2pIc4mVHei2hG2WYTV2yOnr-wx7J8WlbPmK0_GwImGoult9hov8ihPTBun9wp374WcYn8lcjkCYz7eNYoF5Vrl_HVc0EyTuM8Bf4qStEmnIWCSlgwMgzEOqwf1mi6Oyh_iZh_wxHuklacP7iLsNtAFpfoCEy0s8Z66rHALYBPWYg95rgKw1qS1r652AS_AhYCUc9HPew84JTdngeUX3uJv_sOEWscS9Cr9-RqeZkdTQvHW51zafKy-m53yZ2bhUlhBR6MgZ7J-uN6xiLlC82DlBlDq3P8Hz96q5EoabJFXwCtz2Q6VnHk7DmOEFC5lESCcGDaTYdPaLHuJno12zxjTzZ_kUkzQSwKEzSkWfPesKY'
        )
        self.run_compact('RS384', expect)

    def test_compact_RS512(self):
        expect = (
            b'eyJhbGciOiJSUzUxMiJ9.aGVsbG8.'
            b'jIms9o3_R0NzcDSLcC4-HBWnEgm35Wepq8Fu_2C1Sv-nwdkLg6j7dtFMKfoDjxar7fCAjf_JJ_9Z7JTAJzDiFitNnFXuRpGSBm5ZOIYgIMOWl1cjToTe-FJS8T3mXxa4c0wz7a-E9pa4PLAB_Isgx0Hg-7CeH0hpKqULuUIvxuwsAeiKQeZpqu-KjAdFXp7AiJLFnLr7NzcelFsyzwcIVqB7GcDXpkCdmxKHUfOF8iN67lngqghl6lqWAVxjwGXm28mDrRbWnCOxFAZrgiDGkvoyImXMPywOQ7fioffgUTYa54Gmd63JH3L2YIlp2bX-Z9KlstDf9J2igwHQjcidk486f2e9ip0FI0cUa9w9_RJag2-loxkJjvsG6ial6LiiAA8qQZCMoVGcYJsAXhJfVGiLtxVj5v6iSUu5cSEoxI23QeAwIpvXWMiyFvWwwvalv3p-7JKWtbqFRWvx2LjCJpKAEHcRpVEx-brxsNGMH4gL648RFPn8-yFVsvb6DHOLP4VKEOVQhGW5KoPSafp2myyhTzHC8SpmwEJP0y0ArXfXngKs_eHTKRgyvPR2PJEtsoBzOyvF3h6BbsXbvhAVTT-k8qf0jqU4TscoCDPIbiJ9yo6Y_IFCu14zYHBxVZsED4V_v_Cwd3s935F8vNyqwddSm74izC8maNSYu34f38s'
        )
        self.run_compact('RS512', expect)
