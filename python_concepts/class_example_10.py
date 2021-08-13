class KdcProxyUser:
   def __init__(self, username):
       self._username = username

   @property
   def username(self):
       return self._username

   @username.setter
   def setusername(self, user):
       self._username = user


k = KdcProxyUser('a')
#k.username = 'abhijeet'
# k.username('abhijeet')
k.setattr('username', 'abhijeet')
