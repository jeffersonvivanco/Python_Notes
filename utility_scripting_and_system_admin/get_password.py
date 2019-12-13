import getpass

def svc_login(user, passwd):
  print('user {}, password {}'.format(user, passwd))
  pass

user = getpass.getuser()
passwd = getpass.getpass()

if svc_login(user, passwd):
  print('Yay')
else:
  print('Boo')