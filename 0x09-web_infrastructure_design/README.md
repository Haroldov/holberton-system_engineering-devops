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

# 1. Distributed web infrastructure

* We are adding another server in orther to increase redundancy in the system and with this decrease SPOF and Downtime.

* `Round Robin`: It assigns connection to a server going through each one until there are no more connections to assign.

* This `LB` enables Active-Active setup because of both servers are running. On the other hand, in a Active-Passive setup only one server is running and the other one is waiting for a failure.

* A database Primary-Replica cluster works in the way that the replicas are only allowed to read and if they want to write the have to communicate with the primary node.

* The difference between a primary node and a replica node is that the replica can't write, only read. On the other hand, the primary node can do both.

### Issues with this infrastructure:

* The `Load Balancer` is the `SPOF` here. Because in case of `LB` failure the whole system will be down.

* This system has security issues. This means as there is no `firewall` anyone can have access directly to the servers. Moreover, it is not used the `HTTPS` protocol so the information is not encrypted.

* This system has not monitoring. Hence, it cannot be applied for example a dynamic round robin, or there is no record of the QPS, the time taken to access the site, etc.


This one has a special meaning because it assigns one or more connections immediately depending on real time monitoring. This depends on the current number of connections per node or the fastes node response time.

# 2. Secured and monitored web infrastructure

* We added a complete new server to increase redundancy. Moreover, firewall was added to each server in order to increase security, in this way servers only can be accessed from the LB. We added 1 SSL certificate in order to use the HTTPS protocol and encrypt all the information. Finally, we added a cloud monitoring system in order to keep track of the system.

* The firewalls are for not allowing incoming HTTP requests directly to the servers besides the LB and the monitoring system.

* The traffic is served over HTTPS in order to encrypt information and have more security.

* Monitoring is used for keep track of the system like: SSL not expired, Query Per Seconds, RAM, CPU, Disk, Network.

* The monitoring tool fakes a user request and measure all the variables.

* The QPS can be measure by sending a lot of changing in the password of a user and measuring the response of all of them.

### Issues with this infrastructure:

* Because the communication between the LB and the servers (as well as the servers and the monitoring system) is not encrypted.

* It can interfere with other requests if several users need to change their password and only one server can do it.

* I don't know this one.
