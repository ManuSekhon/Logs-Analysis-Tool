# Logs Analysis Tool
Source code for Logs Analysis tool designed in python.

*By Manuinder Sekhon*
#
It is a reporting tool that prints out reports (in plain text) based on the questions below.
1. **What are the most popular three articles of all time?**
1. **Who are the most popular article authors of all time?**
1. **On which days did more than 1% of requests lead to errors?**


## Prerequisites
This project runs in a virtual machine provided by Udacity. Download required dependencies from links below.
* [Vagrant](https://www.vagrant.com/)
* [Virtualbox](https://www.virtualbox.org/)
* [SQL news data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
* [Virtual Machine Configuration](https://d17h27t6h515a5.cloudfront.net/topher/2017/August/59822701_fsnd-virtual-machine/fsnd-virtual-machine.zip)

## Project Design
1. `application.py` defines the `main` function that gets database name and formats the data for display. It depends on `helpers` module to get data from the database.
1. `helpers.py` defines a class `Log` that establishes the connection to the database. `Log` defines required methods to fetch desired data. It automatically closes the connection to database upon program termination.
1. `output.txt` contains the expected output of the program.

## Installation

* Install virtualbox.
* Install vagrant.
* Install python 3.x
```bash
$ sudo apt-get update
$ sudo apt-get install python3
```
* Setup and start the virtual machine

*NOTE: This operation may take several minutes to complete.*
```bash
$ unzip FSND-Virtual-Machine.zip
$ cd FSND-Virtual-Machine/vagrant
$ vagrant up
$ vagrant ssh
```
* Put this project and the extracted `newsdata.zip` in `/vagrant` directory.
* Load news data into your database.
```
psql -d news -f newsdata.sql
```
* Verify that database is correctly loaded by executing `psql -d news` and running `\dt`. If you see three tables `authors`, `articles` and `log`, then you are good to go!

## Usage
```bash
cd /vagrant/Logs-Analysis-Tool
python3 application.py
```
Open `output.txt` for sample output.