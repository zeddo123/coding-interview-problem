-module(sum_odd).
-export([sum/1]).

sum([Head|Rest]) when Head rem 2 /= 0 ->
	Head + sum(Rest);
sum([_|Rest]) ->
	sum(Rest);
sum([]) ->
	0.