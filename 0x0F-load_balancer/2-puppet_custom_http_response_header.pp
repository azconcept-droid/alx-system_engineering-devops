# Install nginx and add custom header

package { 'nginx':
  ensure     =>      '1.18.0',
  provider   =>      'apt-get',
}

exec { 'custom_header' :
  command =>     'sed -i \'s/http {/&\n\tadd_header X-Served-By $hostname;\n/g\' /etc/nginx/nginx.conf',
  path    =>      ['/usr/bin/', '/usr/sbin'],
}

exec { 'restart_nginx':
  command =>      'service nginx restart',
  path    =>       ['/usr/bin/', '/usr/sbin'],
}
