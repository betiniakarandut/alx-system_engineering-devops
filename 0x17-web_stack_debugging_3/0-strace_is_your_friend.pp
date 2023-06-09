# puppet code to fix 500 error from wordpress website
exec { 'fix-wordpress':
  provider => shell,
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
}
