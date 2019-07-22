# 0. Simple web stack

* A server is a physical device specifically created with the purpose of hosting a cloud application. Its hardware is specilized so that it can be turned on 24 hours in a row, it allows multiple connections with other devices and it has the availability to host services.

* The role of the domain name is to get the IP address from that server.

* The subdomain `www` is done with the DNS record `CNAME`.

* The role of the web server is to reply to `HTTP` requests by sending static content to the user.

* The role of the application server is to reply to `HTTP` requests by sending dynamic content to the user.

* The role of the database is to provide information to the application server in order to reply to the user.

### Issues with this infrastructure:

* The whole server is a single point of failure in this system (SPOF).

* Its downtime it's not good since there is only one server, it has to be down while the software is updated.

* Cannot scale if too much incoming traffic due to the implementation of just one server.
