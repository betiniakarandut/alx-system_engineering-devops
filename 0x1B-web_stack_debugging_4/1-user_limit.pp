# Change the OS configuration so that it is possible to login with the holberton user
exec {'file-1':
  provider => shell,
  command  => 'sudo sed -i "s/nofile 5/nofile 50000/" /etc/security/limits.conf',
  before   => Exec['replace-2'],
}

exec {'file-2':
  provider => shell,
  command  => 'sudo sed -i "s/nofile 4/nofile 40000/" /etc/security/limits.conf',
}
