#!usr/bin/pup
#install specified flask version
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}

