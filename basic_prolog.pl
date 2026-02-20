male(alim).
male(belal).
male(camal).
male(dipto).

female(rita).
female(shila).
female(nila).
female(tania).

father(alim, camal).
mother(rita, camal).

father(alim, nila).
mother(rita, nila).

father(camal, dipto).
mother(nila, tania).

father(belal, tania).
mother(shila, tania).

parent(X, Y) :- father(X, Y).
parent(X, Y) :- mother(X, Y).

sibling(X, Y) :-
    parent(P, X),
    parent(P, Y),
    X \= Y.

grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).


% 2. Like-Dislike:

likes(alim, tea).
likes(alim, cricket).
likes(belal, coffee).

dislikes(alim, smoking).
dislikes(belal, tea).

friend(X, Y) :-
    likes(X, Z),
    likes(Y, Z),
    X \= Y.
