# Bool

Given a Boolean formula in 2-CNF, use the resolution method to determine whether it is satisfiable. Clauses of the 2-CNF can be of one of the two forms: α \/ β or α -> β, where α and β are literals (p or ~p, where p is a variable). The CNF is presented in the usual notation, for example: (p -> q) /\ (~r \/ s) /\ (~q -> p)

## Bools Grammar

```
formular ::= var | disjunctive_formular | conjunctive_formular | implicative_formular | (formular)

disjunctive_formular ::= (formular \/ formular) | formular \/ formular

conjunctive_formular ::= (formular /\ formular) | formular /\ formular

implicative_formular ::=  (formular -> formular) | formular -> formular
```

## Needed Software

Python==3.7.4

ply==3.11

## Installation

Download and install [PLY](https://www.dabeaz.com/ply/)

## Running 

Navigate to the folder
Run the command below:
> python bool.py 

NB// Works as a terminal app

PS// Had a lot of help from some collegues :)

## Sample Tests

```

* (p -> q) /\ (~r \/ s) /\ (~q -> p)      sat
* x /\ (~x \/ y)                          sat
* (p -> q) /\ (~r \/ s) /\ (~q -> p)      sat
* (~p \/ q) /\ (~p \/ ~q)                 sat
* (p \/ ~q) /\ (p \/ q)                   sat
* (p \/ ~q) /\ (p \/ ~q)                  sat
* (~p \/ q) /\ (p \/ q)                   sat
* (p -> q) /\ (~q \/ p)                   unsat
* (p->q)/\(~r\/s)/\(~q->p)                sat
* (p ->q)/\(q->r)/\(r->s)/\(s->t)/\p/\~t  unsat
* (p ->q)/\(q->r)/\p/\~r                  unsat

```
