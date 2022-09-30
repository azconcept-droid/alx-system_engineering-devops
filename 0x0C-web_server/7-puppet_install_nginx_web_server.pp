# Install puppet and nginx with custom body and redirect 

exec { 'update_ubuntu':
  command =>     'apt-get update',
  path    =>      ['/usr/bin/', '/usr/sbin'],
}

package { 'puppet':
  ensure   =>    '5.5.10',
  provider =>    'gem',
}

package { 'nginx':
  ensure   =>    '1.18.0',
  provider =>    'apt-get',
}

exec { 'custom_body':
  command =>      'echo "Hello World!" > /var/www/html/index.nginx-debian.html'
  path    =>       ['/usr/bin/', '/usr/sbin'],
}

exec { 'redirect' :
  command =>     "sed -i 's+_;+_;\n\tlocation /redirect_me {\n\t\treturn 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;\n\t}+g' /etc/nginx/sites-available/default",
  path    =>      ['/usr/bin/', '/usr/sbin'],
}

exec { 'restart_nginx':
  command =>      'service nginx restart',
  path    =>       ['/usr/bin/', '/usr/sbin'],
}
