-module(max).
-export([max_list/1]).

max_list([Head|Rest]) ->
	max_list(Rest, Head).

max_list([Head|Rest], Current_result) when Current_result > Head ->
	max_list(Rest, Current_result);

max_list([Head|Rest], _) ->
	max_list(Rest, Head);

max_list([], Result) ->
	Result.