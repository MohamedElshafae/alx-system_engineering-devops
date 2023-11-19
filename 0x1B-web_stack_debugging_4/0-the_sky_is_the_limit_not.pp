# increase the limt of Nginx

exec { 'increase-limt':
  provider    => 'shell',
  command     => "sed -i 's/^ULIMIT=.*/ULIMIT=\"-n 15000\"/' /etc/default/nginx",
}

exec { 'nginx-restart':
  provider    => 'shell',
  command     => 'service nginx restart',
}
