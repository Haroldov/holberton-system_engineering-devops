# Requirements:
# Your SSH client configuration must be configured to use the private key ~/.ssh/holberton
# Your SSH client configuration must be configured to refuse to authenticate using a password
exec { '/etc/ssh/ssh_config':
  command => '/bin/echo -e "IdentityFile ~/.ssh/holberton\nPasswordAuthentication no" >> /etc/ssh/ssh_config',
  path    => '/etc/ssh/ssh_config',
}
