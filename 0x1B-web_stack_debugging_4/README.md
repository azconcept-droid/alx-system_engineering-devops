#  0x1B. Web stack debugging #4
``DevOps`` ``SysAdmin`` ``Scripting`` ``Debugging``

## Install puppet-lint

$ apt-get install -y ruby
$ gem install puppet-lint -v 2.1.1


For the benchmarking, we are using ApacheBench which is a quite popular tool in the industry. It allows you to simulate HTTP requests to a web server. In this case, I will make 2000 requests to my server with 100 requests at a time. We can see that 943 requests failed, let’s fix our stack so that we get to 0, and remember that when something is going wrong, logs are your best friends!

```
ab -c 100 -n 2000 localhost/
```
