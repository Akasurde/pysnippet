#!/usr/bin/python

import hmac
import hashlib
class hotp:
        def __init__(self,key,digits=6):
                self.key=key
                self.digits=digits

        def dynamictruncate(self,s):
                """dynamically truncate the string"""
                offset=int(s,16)&0xf
                return "%016x" % (int(s[offset*2:offset*2+8],16) 
                &0x7fffffff)

        def intto16string(self,c):
                """convert an int to a 16 byte string"""
                c="%016x" %count
                return "".join([chr(int(c[i*2:i*2+2],16)) for i in range 
                (0,8)])

        def get(self,count):
                """ calculates the HOTP for key and count """
                count=self.intto16string(count)
                hc=hmac.new(self.key,count,hashlib.sha1)
                s=hc.hexdigest()
                ts=self.dynamictruncate(s)
                snum=int(ts,16)
                return snum % (10 ** self.digits)

                return hotp.get(self,count)

if __name__=="__main__":
        h=hotp("DFHUZHTYEAYUE2C7MGJICJEAU5VCQSCQIVKQ6XG7AGYZLHVY4YDA")
        for count in range (0,11):
                print h.get(count)
