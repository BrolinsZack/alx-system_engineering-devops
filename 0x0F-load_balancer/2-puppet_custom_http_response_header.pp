# Installs a Nginx server with custom HTTP header

exec { 'update':
  command  => '/usr/bin/apt-get -y update',
  provider => shell,
  before   => Exec['install Nginx'],
}

exec { 'install Nginx':
  command  => '/usr/bin/apt-get -y install nginx',
  provider => shell,
  before   => Exec['add_header'],
}

$hostname = $::hostname

exec { 'add_header':
  command     => '/usr/bin/sed -i "s/include \/etc\/nginx\/sites-enabled\/\*;/include \/etc\/nginx\/sites-enabled\/\*;\n\tadd_header X-Served-By \"$HOST\";/" /etc/nginx/nginx.conf',
  provider    => shell,
  environment => ["HOST=${hostname}"],
  before      => Exec['restart Nginx'],
}

exec { 'restart Nginx':
  command  => '/usr/sbin/service nginx restart',
  provider => shell,
}
