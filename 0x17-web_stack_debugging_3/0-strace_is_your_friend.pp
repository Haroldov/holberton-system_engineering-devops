include stdlib
$fqdn = $facts['fqdn']
file_line { 'wp-settings':
  ensure => present,
  path   => '/var/www/html/wp-settings.php',
  line   => ".phpp",
  match  => '.php',
}
