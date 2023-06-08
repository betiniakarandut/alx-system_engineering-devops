# puppet code to fix 500 error from wordpress website
exec { 'fix-wordpress':
  command =>'sed -i 's/phhp/php/g' var/www/html/wp-setting.php' sudo systemctl restart apache2
  path    => ['/bin', '/usr/bin', '/bin/sbin']
}
