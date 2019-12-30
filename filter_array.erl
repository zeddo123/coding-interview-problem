% From Hackerrank.com
% Filter a given array of integers and output only those values that are less than a specified value .
% The output integers should be in the same sequence as they were in the input.
% You need to write a function with the recommended method signature for the languages mentioned below.
% For the rest of the languages, you have to write a complete code.

-module(filter_array).
-export([filter/2]).

filter([Head|Rest], Fil) when Fil > Head ->
	io:format("~w ~n", [Head]),
	filter(Rest, Fil);

filter([_|Rest], Fil) ->
	filter(Rest, Fil);

filter([], _) ->
	ok.