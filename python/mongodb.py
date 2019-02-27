#!/usr/bin/python3

#
#  MongoDB + Python example
#  Last update: 2019-02-27
#

from pymongo import MongoClient
from pprint import pprint


# connect to MongoDB
mngcl = MongoClient('mongodb://admin:VerrekteMongol@127.0.0.1/?authSource=admin&authMechanism=SCRAM-SHA-1')

# return databases
print('Databases: {}'.format(mngcl.database_names()))
db_lst = mngcl.database_names()
if 'db' in db_lst:
	print('people database already exists')

# create database
my_db = mngcl['db']
my_col = my_db['people']


# insert people
john = { \
	u'given_name': u'John', \
	u'family_name': u'Doe' \
}
jane = {
	u'given_name': 'Jane', \
	u'family_name': 'Doe', \
	u'age': 123 \
}
john_id = my_col.insert_one(john).inserted_id
jane_id = my_col.insert_one(jane).inserted_id
print('John ID: {}'.format(john_id))

# get collections
print('Collections: {}'.format(my_db.collection_names(include_system_collections=False)))

# insert many
#rst = my_col.insert_many([ john, jane ])
#print('Inserted IDs: {}'.format(rst.inserted_ids))


# get a single document
print('find_one():')
pprint(my_col.find_one())

# find a document
print('Find Jane:')
pprint(my_col.find_one({'_id': jane_id}))

# find all documents, return only some fields, limit output to 10
for person in my_col.find({},{'_id':0, 'given_name':1, 'age':1}).limit(10):
	pprint(person)

# count documents
#print('Number documents: {}'.format(my_col.count_documents({})))

# find regex
for person in my_col.find({"given_name": {'$regex': '^Ja'}}).sort('_id', -1): # 1 = ascending, -1 = descending
	print(person['_id'])


# update
my_col.update_many(
	{ 'given_name': { '$regex': '^Jo' } },
	{ '$set': { u'age': 456 } }
)


# remove John
my_col.delete_one({'_id': john_id})

# delete all Janes
print('Deleted: {}'.format(my_col.delete_many({'given_name': {'$regex': '^Ja'} }).deleted_count))

# delete all documents
my_col.delete_many({})

# delete collection
my_col.drop()

