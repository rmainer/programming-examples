#!/bin/bash

#
#  Initializes MongoDB, adds admin and a test user
#  Last update: 2019-02-27
#

if [ `id -u` != 0 ]; then
	echo "Become root!"
	exit 0
fi

output() {
	TIME=`date '+%H:%M:%S'`
	echo -e "\e[33m[$TIME] $1\e[39m" 
}

output "Be careful, this script will delete your old MongoDB data!"
read -p "Proceed (y/n) " proceed

if [ $proceed != "y" ]; then
	exit
fi

output "mongodb stop"
systemctl stop mongodb

output "cleanup"
rm -rf /var/lib/mongodb/*

output "mongodb start"
systemctl start mongodb

output "sleep"
sleep 2

output "checking connection"
mongo --eval 'db.runCommand({ connectionStatus: 1})'

output "create 'admin' user"
mongo << EOF
use admin
db.createUser(
	{user: "admin",
	pwd: "VerrekteMongol",
	roles: [ { role: "root", db: "admin" } ]})
EOF

output "creating user 'mongotest'"
mongo << EOF
use admin
db.auth("admin", "VerrekteMongol")
use users
db.createUser({ user: "mongotest", pwd: "mongotest123", roles: [{ role: "readWrite", db: "mongotest" }] })
EOF

output "drop 'test' database"
mongo << EOF
use admin
db.auth("admin", "VerrekteMongol")
use test
db.dropDatabase()
EOF
