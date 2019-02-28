#!/usr/bin/python3

#
#  Redis python api example
#  Last update: 2019-02-28
#  Installation: 
#    Debian: apt install redis-server python3-redis
#
from redis import Redis

r = Redis(host='127.0.0.1', port=6379, db=0, encoding=u'utf-8', password='testpw')

# key: foo, value: bar, time until automaticly removed: 10 seconds
if r.set('foo', 'bar', ex=10) == True:
	print('success')

r.set('foo1', 'bar1')
r.set('foo2', 'bar2')
r.expire('foo1', 10)
r.delete('foo1', 'foo2')

print('output: {}'.format(r.get('foo')))

