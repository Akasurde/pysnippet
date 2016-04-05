class KdcProxyUser:
    def __init__(self):
        self.username = 'kdcproxy'

    @property
    def username(self):
        return self.username

    @username.setter
    def setusername(self, user):
        self.username = user

class TestKdcproxy:
    def test_positive_kdcproxy(self):
        user = 'kdcproxy'
        k = KdcProxyUser()
        assert user in k.username

    def test_negative_kdcproxy(self):
        user = 'kdcproxy'
        k = KdcProxyUser()
        assert user in k.username
    
    def test_negative_kdcproxy1(self):
        user = 'abhijeet'
        k = KdcProxyUser()
        assert user in k.username

class TestS:
    def test_somethig(self):
        pass
