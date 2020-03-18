-module(merge_sort).
-export([sort/1, sublist/3]).

sort(List) ->
	sort(sublist(List, 1, length(List) div 2), sublist(List, length(List) div 2, length(List) - length(List) div 2)).

sort([One], [Two]) when One > Two ->
	[Two,One];

sort([One], [Two]) ->
	[One,Two];

sort(List1, List2) ->
	sort(sublist(List1, 1, length(List1) div 2), sublist(List1, length(List1) div 2, length(List1)- length(List1) div 2)) + sort(sublist(List2, 1, length(List2) div 2), sublist(List2, length(List2) div 2, length(List2)- length(List2) div 2)).

sublist([], _, _) ->
	[];
sublist([Head|Rest], B, E) ->
	sublist([Head|Rest], B, E, 0).

sublist([], _, _, _) ->
	[];

sublist([_|Rest], B, E, C) when B > C ->
	sublist(Rest, B, E, C + 1);

sublist([Head|Rest], B, E, C) when E >= C ->
	[Head] ++ sublist(Rest, B, E, C + 1);

sublist(_, _, E, C) when E < C->
	[].