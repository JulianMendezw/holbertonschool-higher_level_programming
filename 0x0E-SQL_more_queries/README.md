# 0x0E. SQL - More queries

-   Foundations - Higher-level programming ― Databases
-   By Guillaume, CTO at Holberton School

## Resources

**Read or watch**:

-   [How To Create a New User and Grant Permissions in MySQL](https://intranet.hbtn.io/rltoken/u4h2MXcCQfadszlRMQy-gw "How To Create a New User and Grant Permissions in MySQL")
-   [How To Use MySQL GRANT Statement To Grant Privileges To a User](https://intranet.hbtn.io/rltoken/ztrEKQexfEDtZ-8EUsG70Q "How To Use MySQL GRANT Statement To Grant Privileges To a User")
-   [MySQL constraints](https://intranet.hbtn.io/rltoken/LBrFqCMm9N9woTX7sS7e0g "MySQL constraints")
-   [SQL technique: subqueries](https://intranet.hbtn.io/rltoken/YYpPtkqFeKSCsAU4Y_y3Og "SQL technique: subqueries")
-   [Basic query operation: the join](https://intranet.hbtn.io/rltoken/npLCp3WasK0SUSUQqCF25A "Basic query operation: the join")
-   [SQL technique: multiple joins and the distinct keyword](https://intranet.hbtn.io/rltoken/GmRLMhkY-pPvjcpzyDvmRg "SQL technique: multiple joins and the distinct keyword")
-   [SQL technique: join types](https://intranet.hbtn.io/rltoken/ryjyRRN7696rJV0maP03Xw "SQL technique: join types")
-   [SQL technique: union and minus](https://intranet.hbtn.io/rltoken/L7Fi5w8GZG5MSdQZ19e88g "SQL technique: union and minus")
-   [MySQL Cheat Sheet](https://intranet.hbtn.io/rltoken/V9vpLbtkFwV4EZYoiz2NBA "MySQL Cheat Sheet")
-   [The Seven Types of SQL Joins](https://intranet.hbtn.io/rltoken/ySKSdhFeMDddea07XrDzeQ "The Seven Types of SQL Joins")
-   [MySQL Tutorial](https://intranet.hbtn.io/rltoken/-uqP0a89xUl3SsmV_ZtxRA "MySQL Tutorial")
-   [SQL Style Guide](https://intranet.hbtn.io/rltoken/jn4SHgwVtOJF0LQYPEIs-g "SQL Style Guide")
-   [MySQL 5.7 SQL Statement Syntax](https://intranet.hbtn.io/rltoken/YjNAE7DcadDbT_a7iI0sYw "MySQL 5.7 SQL Statement Syntax")

Extra resources around relational database model design:

-   [Design](https://intranet.hbtn.io/rltoken/9ppVdXqFMn-v1eKuxsOvaQ "Design")
-   [Normalization](https://intranet.hbtn.io/rltoken/zo6dqYxsXby3S3uON5JfOg "Normalization")
-   [ER Modeling](https://intranet.hbtn.io/rltoken/ZaMMezT-GdpgHB9pmM78iw "ER Modeling")

### General

-   How to create a new MySQL user
-   How to manage privileges for a user to a database or table
-   What’s a  `PRIMARY KEY`
-   What’s a  `FOREIGN KEY`
-   How to use  `NOT NULL`  and  `UNIQUE`  constraints
-   How to retrieve datas from multiple tables in one request
-   What are subqueries
-   What are  `JOIN`  and  `UNION`

## More Info

### Comments for your SQL file:

```
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$

```

### Install MySQL 5.7 on Ubuntu 14.04 LTS

```
$ echo 'deb http://repo.mysql.com/apt/ubuntu/ trusty mysql-5.7-dmr' | sudo tee -a /etc/apt/sources.list
$ sudo apt-get update
$ sudo apt-get install mysql-server-5.7
...
$ mysql --version
mysql  Ver 14.14 Distrib 5.7.8-rc, for Linux (x86_64) using  EditLine wrapper
$

```

**Don’t forget your  `root`  password**

If you had before MySQL 5.5 installed, please run these 2 commands after the installation of the version 5.7:

```
$ mysql_upgrade -u root -p
Password: 
$ sudo service mysql restart

```

If you have some issues to upgrade to 5.7, don’t hesitate to cleanup your server of any MySQL packages:  `sudo apt-get remove --purge mysql-server mysql-client mysql-common`

### Use “container-on-demand” to run MySQL

-   Ask for container  `Ubuntu 14.04 - Python 3.4`
-   Connect via SSH
-   Or via the WebTerminal
-   In the container, you should start MySQL before playing with it:

```
$ service mysql start
 * MySQL Community Server 5.7.8-rc is started
$
$ cat 0-list_databases.sql | mysql -uroot -p my_database
Enter password: 
Database
information_schema
mysql
performance_schema
sys
$

```

**In the container, credentials are  `root/root`**

### How to import a SQL dump

```
$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password: 
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller
$

```

![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/3/bc2575fee3303b731031.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210302%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210302T170646Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=81419dcd861996dc040939fb7d9884c28c49a5d63c545a2138a9e18871ab6972)
