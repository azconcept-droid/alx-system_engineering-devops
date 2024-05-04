# 0x10. HTTPS SSL
``DevOps`` ``SysAdmin`` ``Security``

![https](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/276/FlhGPEK.png)

# Background Context
**What happens when you don’t secure your website traffic?**

![sneakin](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/276/xCmOCgw.gif)

# Setting up SSL Termination on your webserver
1. login as root user
   ```
   sudo su
   ```
2. Install cerbot
   ```
   snap install --classic certbot
   ```
3. Stop haproxy from running
   ```
   service haproxy stop
   ```
4. Generate SSL certificate
   ```
   cerbot certonly --standalone -d www.yalect.live
   ```
5. Create a directory at /etc/haproxy/certs
   ```
   mkdir -p /etc/haproxy/certs
   ```

6. Combine the certificate and the key generated from step 5 into a .pem file in your certs directory
   ```
   export DOMAIN='www.yalect.live'
   cat /etc/letsencrypt/live/www.yalect.live/fullchain.pem /etc/letsencrypt/live/www.yalect.live/privkey.pem > /etc/haproxy/certs/$DOMAIN.pem
   ```

7. Change the mode of the DIRECTORY
   ```
   chmod -R go-rwx /etc/haproxy/certs
   ```

8. Add the following lines to your front_end in your haproxy config file
   ```
   sudo vim /etc/haproxy/haproxy.cfg # open the file
   #lines to add
   bind *:443 ssl crt /etc/haproxy/certs/domain.pem
   redirect scheme https if !{ ssl_fc }
   ```

9. Check if the configuration file is valid
    ```
    haproxy -f /etc/haproxy/haproxy.cfg -c
    ```

10. Start your haproxy
    ```
    service haproxy start
    ```
