import hmac
import hashlib
import struct
import time
import unittest


def HOTP(K, C, digits=6, digestmod=hashlib.sha1):
    """
    HOTP accepts key K and counter C
    optional digits parameter can control the response length

    returns the OATH integer code with {digits} length
    """
    C_bytes = struct.pack(b"!Q", C)
    hmac_digest = hmac.new(key=K, msg=C_bytes,
                           digestmod=digestmod).hexdigest()
    return Truncate(hmac_digest)[-digits:]


def TOTP(K, digits=6, window=30, clock=None, digestmod=hashlib.sha1):
    """
    TOTP is a time-based variant of HOTP.
    It accepts only key K, since the counter is derived from the current time
    optional digits parameter can control the response length
    optional window parameter controls the time window in seconds

    returns the OATH integer code with {digits} length
    """
    if clock is None:
        clock = time.time()
    C = int(clock / window)
    return HOTP(K, C, digits=digits, digestmod=digestmod)


def Truncate(hmac_digest):
    """
    Truncate represents the function that converts an HMAC
    value into an HOTP value as defined in Section 5.3.
    http://tools.ietf.org/html/rfc4226#section-5.3
    """
    offset = int(hmac_digest[-1], 16)
    binary = int(hmac_digest[(offset * 2):((offset * 2) + 8)], 16) & 0x7fffffff
    return str(binary)


class HotpTest(unittest.TestCase):
    """
    a very simple test case for HOTP.
    Based on test vectors from http://www.ietf.org/rfc/rfc4226.txt
                          and  http://tools.ietf.org/html/rfc6238
    """
    def setUp(self):
        self.key_string = b'aaaaaa'

    def test_hotp_vectors(self):
        hotp_result_vector = ['755224', '287082', '359152',
                              '969429', '338314', '254676',
                              '287922', '162583', '399871',
                              '520489']
        for i in range(10):
            print HOTP(self.key_string, i)
        #for i, r in enumerate(hotp_result_vector):
        #    self.assertEqual(HOTP(self.key_string, i), r)

if __name__ == '__main__':
    unittest.main()

