-module(add_subtract).
-export([sumup/2]).

sumup([First | TheRest], add) ->
	First + sumup(TheRest,sub);

sumup([First | TheRest], sub) ->
	(- First) + sumup(TheRest,add);

sumup([First | TheRest], start) ->
	First + sumup(TheRest,add);
	
sumup([], _) ->
	0.
