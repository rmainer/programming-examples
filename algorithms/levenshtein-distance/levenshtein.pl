#!/usr/bin/perl

use strict;
use warnings;
use List::Util qw[min];

sub levenshtein {
	my (@d, $n1, $n2, $w1, $w2);
	$w1 = lc $_[0];
	$w2 = lc $_[1];
	$n1 = length($w1) + 1;
	$n2 = length($w2) + 1;

	for(my $y=0; $y<$n1; $y++) {
		for(my $x=0; $x<$n2; $x++) {
			$d[$y][$x] = 0;
		}
	}
	for(my $y=1; $y<$n1; $y++) {
		$d[$y][0] = $y;
	}
	for(my $x=0; $x<$n2; $x++) {
		$d[0][$x] = $x;
	}

	for(my $y=1; $y<$n1; $y++) {
		for(my $x=1; $x<$n2; $x++) {
			if( substr($w1, $y-1, 1) eq substr($w2, $x-1, 1) ) {
				$d[$y][$x] = $d[$y-1][$x-1];
			}
			else {
				$d[$y][$x] = min($d[$y-1][$x-1], $d[$y-1][$x], $d[$y][$x-1]) + 1;
			}
		}
	}

	return $d[$n1-1][$n2-1];
}

print levenshtein("Roman", "Ramon")."\n";
