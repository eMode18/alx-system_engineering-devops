# puupet automation for webserver

package { 'nginx':
  ensure => installed,
}

file_line { 'install':
  ensure => 'present',
  path   => '/etc/nginx/sites-enabled/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.github.com/eMode18 permanent;',
}

file { '/var/www/html/index.html':
  content => 'Hello world!',
}

service { 'nginx':
  ensure => running,
  require => Package['nginx'],
}
