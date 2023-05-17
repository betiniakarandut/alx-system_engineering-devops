# 0x14. MySQL

## Description
- What is the main role of a database
- What is a database replica
- What is the purpose of a database replica
- Why database backups need to be stored in different physical locations
- What operation should you regularly perform to make sure that your database backup strategy actually works

## Task
| task | Description |
|------|-------------|
| [Setup a Primary-Replica infrastructure using MySQL](./4-mysql_configuration_primary) | Having a replica member on for your MySQL database has 2 advantages:<br>Redundancy: If you lose one of the database servers, you will still have another working one and a copy of your data<br>Load distribution: You can split the read operations between the 2 servers, reducing the load on the primary member and improving query response speed |
| [MySQL backup](./5-mysql_backup) | Write a Bash script that generates a MySQL dump and creates a compressed archive out of it.<br>Requirements:<br>The MySQL dump must contain all your MySQL databases<br>The MySQL dump must be named backup.sql<br>The MySQL dump file has to be compressed to a tar.gz archive<br>This archive must have the following name format: day-month-year.tar.gz<br>The user to connect to the MySQL database must be root<br>The Bash script accepts one argument that is the password used to connect to the MySQL database |
