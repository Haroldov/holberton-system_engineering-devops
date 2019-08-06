# Requirements:
# Your SSH client configuration must be configured to use the private key ~/.ssh/holberton
# Your SSH client configuration must be configured to refuse to authenticate using a password

file { '/etc/ssh/ssh_config':
  ensure => present,
}->
file_line { 'Append a line to /etc/ssh/ssh_config':
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/holberton',
}
file { '/etc/ssh/ssh_config':
  ensure => present,
}->
file_line { 'Replace a line to /etc/ssh/ssh_config':
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no',
}
