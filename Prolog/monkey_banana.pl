in_room(monkey).
in_room(chair).
in_room(banana).
clever(monkey).
tall(chair).
can_get(monkey,chair,banana).
can_climb(monkey,chair).

get_on(X,Y):-
can_climb(X,Y).

under(Y,Z):- in_room(Y), in_room(Z), in_room(X), can_get(X,Y,Z).

close2(X,Z):-
get_on(X,Y),under(Y,Z), tall(Y).

can_reach(X,Y):-
clever(X),close2(X,Y).
