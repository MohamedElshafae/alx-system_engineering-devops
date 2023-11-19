# increase the limt of Nginx


package { 'nginx':
  ensure => installed,
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

exec { 'increase-limt':
  command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/',
}
exec { 'nginx-restart':
  command     => 'etc/init.d/nginx restart',
  path        => 'etc/init.d/'
}
