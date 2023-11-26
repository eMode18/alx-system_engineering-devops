#!/usr/bin/env bash
# puppet automation

file { 'etc/ssh/ssh_config':
	ensure => present,

content => "
  #ssh client config
  host*
  IdentityFile ~/.ssh/school
  PasswordAuthentication no
}
