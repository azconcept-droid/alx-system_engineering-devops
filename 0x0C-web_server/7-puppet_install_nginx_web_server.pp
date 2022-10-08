# Install puppet and nginx with custom body and redirect 

exec { 'nginx':
  command =>    'sudo apt-get install nginx -y',
  path     =>    ['/usr/bin', '/usr/sbin'],
}

exec { 'custom_body':
  command =>      'sudo echo "Hello World!" > /var/www/html/index.nginx-debian.html'
  path    =>       ['/usr/bin/', '/usr/sbin'],
}

exec { 'redirect' :
  command =>     "sudo sed -i 's+_;+_;\n\tlocation /redirect_me {\n\t\treturn 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;\n\t}+g' /etc/nginx/sites-available/default",
  path    =>      ['/usr/bin/', '/usr/sbin'],
}

exec { 'restart_nginx':
  command =>      'sudo service nginx restart',
  path    =>       ['/usr/bin/', '/usr/sbin'],
}
