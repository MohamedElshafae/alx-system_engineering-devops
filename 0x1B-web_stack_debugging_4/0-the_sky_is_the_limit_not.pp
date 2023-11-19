# increase the limt of Nginx

exec { 'increase-limt':
  provider    => 'shell',
  command     => 'sudo sed -i "s/15/4096/" /etc/default/nginx',
}
exec { 'nginx-restart':
  provider    => 'shell',
  command     => 'sudo service nginx restart',
}
