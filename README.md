# Log Analysis Project
A reporting tool that prints out reports (in plain text) 
based on the data in the database. 

# Questions It Answer:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## How to Install and Run Program.

1. Install [Vagrant](https://www.vagrantup.com/)
2. Install [VirtualBox](https://www.virtualbox.org/)
3. Download the vagrant setup files from [Udacity's Github](https://github.com/udacity/fullstack-nanodegree-vm)
4. Download the database newsdata.sql (https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
5. Put the newsdata.sql file into the vagrant directory
6. Download this project and unzip all file to the vagrant directory

# How to Run the Virtual Machine:
1. Open Terminal.
2. cd into the vagrant directory
3. Run ``` vagrant up ``` to build the VM for the first time.
4. Once it is built, run ``` vagrant ssh ``` to connect.
5. cd into the correct project directory: ``` cd /vagrant/log_analysis ```
6. Load the data using the following command: ``` psql -d news -f newsdata.sql ```

# Running the Project
1. You should already have vagrant up and be connected to it. 
1. If you aren't already, cd into the correct project directory: ``` cd /vagrant/log_project ```
1. Run ``` python log.py ```

