.TL
Nginx Configuration
.AU
Max
.NH
global
.PP 
.B "user"
www www
.PP 
.B "worker_processes"
5
.PP 
.B "error_log"
logs/error.log
.PP 
.B "pid"
logs/nginx.pid
.PP 
.B "worker_rlimit_nofile"
8192
.NH
events
.PP 
.B "worker_connections"
4096
.NH
http
.PP 
.B "include"
conf/mime.types
.PP 
.B "include"
/etc/nginx/proxy.conf
.PP 
.B "include"
/etc/nginx/fastcgi.conf
.PP 
.B "index"
index.html index.htm index.php
.PP 
.B "default_type"
application/octet-stream
.PP 
.B "log_format"
main '$remote_addr - $remote_user [$time_local] $status''"$request" $body_bytes_sent'
.PP 
.B "access_log"
logs/access.log  main
.PP 
.B "sendfile"
on
.PP 
.B "tcp_nopush"
on
.PP 
.B "server_names_hash_bucket_size"
128
.SH 
 server
.PP 
.B "listen"
80
.PP 
.B "server_name"
domain1.com www.domain1.com
.PP 
.B "access_log"
logs/domain1.access.log  main
.PP 
.B "root"
html
.SH 
 location ~ \.php$
.PP 
.B "fastcgi_pass"
127.0.0.1:1025
.SH 
 server
.PP 
.B "listen"
80
.PP 
.B "server_name"
domain2.com www.domain2.com
.PP 
.B "access_log"
logs/domain2.access.log  main
.SH 
 location ~ ^/(images|javascript|js|css|flash|media|static)/
.PP 
.B "root"
/var/www/virtual/big.server.com/htdocs
.PP 
.B "expires"
30d
.SH 
 location / 
.PP 
.B "proxy_pass"
http://127.0.0.1:8080
.SH 
 upstream
.PP 
.B "server"
127.0.0.3:8000 weight=5
.PP 
.B "server"
127.0.0.3:8001 weight=5
.PP 
.B "server"
192.168.0.1:8000
.PP 
.B "server"
192.168.0.1:8001
.SH 
 server
.PP 
.B "listen"
80
.PP 
.B "server_name"
big.server.com
.PP 
.B "access_log"
logs/big.server.access.log main
.SH 
 location / 
.PP 
.B "proxy_pass"
http://big_server_com
