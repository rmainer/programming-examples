<?php

	//
	//  Redis PHP api
	//  Last update: 2019-02-28
	//  Installation:
	//    Debian: apt install php-redis
	//

	$redis = new Redis();
	$redis->connect('127.0.0.1', 6379);
	$redis->auth('testpw');
	$redis->select(0);
	$redis->set('key', 'php', 10);
	echo 'output: '.$redis->get('key')."\n";
	$redis->close();

?>
