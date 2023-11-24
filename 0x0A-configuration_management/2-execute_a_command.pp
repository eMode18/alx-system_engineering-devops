exec { 'killmenow':
  command     => 'pkill -f killmenow',
  path        => '/bin:/usr/bin:/usr/local/bin',
  refreshonly => true,
}
