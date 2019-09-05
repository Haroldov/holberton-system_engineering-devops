-- Script that prepares a MySQL server for the project
GRANT REPLICATION SAVE ON *.* TO 'replica_user'@'%' IDENTIFIED BY 'replicahbtn';
FLUSH PRIVILEGES;

