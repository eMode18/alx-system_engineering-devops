# Modify OS configuration to enable login as the holberton user and eliminate error messages when opening files
exec { 'modify_limits_conf_for_holberton':
  command => '/usr/bin/env sed -i "s/holberton/foo/" /etc/security/limits.conf',
}
