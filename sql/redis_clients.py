#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#wby 2018
#https://redis.io/clients#python 官方推荐使用redis-py
# pip install redis
# 连接使用 redis-py

import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)
r.set('foo', 'bar')
print(r.get('foo'))

#集群
# pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
# r = redis.Redis(connection_pool=pool)
#
