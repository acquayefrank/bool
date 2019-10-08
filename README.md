# Bool

Given a Boolean formula, constructed from variables using /\ (conjunction), \/ (disjunction), -> (implication), and ~ (negation), `bool` translate it into Conjunctive Normal Form and into Disjunctive Normal Form.

## Bools Grammar

formular ::= var | disjunctive_formular | conjunctive_formular | implicative_formular | (formular)

disjunctive_formular ::= (formular \/ formular) | formular \/ formular

conjunctive_formular ::= (formular /\ formular) | formular /\ formular

implicative_formular ::=  (formular -> formular) | formular -> formular

## Needed Software

Python==3.7.4
ply==3.11

## Installation
Download and install [PLY](https://www.dabeaz.com/ply/)

## Running 
Navigate to the folder
Run the command below:
> python bool.py 
