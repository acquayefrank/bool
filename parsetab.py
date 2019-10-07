
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "CONJUNCTION DISJUNCTION IMPLICATION VARformular : var\n               | disjunctive_formular\n               | conjunctive_formular\n               | implicative_formular\n                var : VAR \n    disjunctive_formular : '(' formular DISJUNCTION formular ')'\n                         |  formular DISJUNCTION formular \n    \n    conjunctive_formular : '(' formular CONJUNCTION formular ')'\n                         |  formular CONJUNCTION formular \n    \n    implicative_formular : '(' formular IMPLICATION formular ')'\n                         |  formular IMPLICATION formular\n    "
    
_lr_action_items = {'VAR':([0,7,8,9,10,15,16,17,],[6,6,6,6,6,6,6,6,]),'(':([0,7,8,9,10,15,16,17,],[7,7,7,7,7,7,7,7,]),'$end':([1,2,3,4,5,6,12,13,14,21,22,23,],[0,-1,-2,-3,-4,-5,-7,-9,-11,-6,-8,-10,]),'DISJUNCTION':([1,2,3,4,5,6,11,12,13,14,18,19,20,21,22,23,],[8,-1,-2,-3,-4,-5,15,8,8,8,8,8,8,-6,-8,-10,]),'CONJUNCTION':([1,2,3,4,5,6,11,12,13,14,18,19,20,21,22,23,],[9,-1,-2,-3,-4,-5,16,9,9,9,9,9,9,-6,-8,-10,]),'IMPLICATION':([1,2,3,4,5,6,11,12,13,14,18,19,20,21,22,23,],[10,-1,-2,-3,-4,-5,17,10,10,10,10,10,10,-6,-8,-10,]),')':([2,3,4,5,6,12,13,14,18,19,20,21,22,23,],[-1,-2,-3,-4,-5,-7,-9,-11,21,22,23,-6,-8,-10,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'formular':([0,7,8,9,10,15,16,17,],[1,11,12,13,14,18,19,20,]),'var':([0,7,8,9,10,15,16,17,],[2,2,2,2,2,2,2,2,]),'disjunctive_formular':([0,7,8,9,10,15,16,17,],[3,3,3,3,3,3,3,3,]),'conjunctive_formular':([0,7,8,9,10,15,16,17,],[4,4,4,4,4,4,4,4,]),'implicative_formular':([0,7,8,9,10,15,16,17,],[5,5,5,5,5,5,5,5,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> formular","S'",1,None,None,None),
  ('formular -> var','formular',1,'p_formular','bool.py',33),
  ('formular -> disjunctive_formular','formular',1,'p_formular','bool.py',34),
  ('formular -> conjunctive_formular','formular',1,'p_formular','bool.py',35),
  ('formular -> implicative_formular','formular',1,'p_formular','bool.py',36),
  ('var -> VAR','var',1,'p_var','bool.py',44),
  ('disjunctive_formular -> ( formular DISJUNCTION formular )','disjunctive_formular',5,'p_disjunctive_formular','bool.py',50),
  ('disjunctive_formular -> formular DISJUNCTION formular','disjunctive_formular',3,'p_disjunctive_formular','bool.py',51),
  ('conjunctive_formular -> ( formular CONJUNCTION formular )','conjunctive_formular',5,'p_conjunctive_formular','bool.py',58),
  ('conjunctive_formular -> formular CONJUNCTION formular','conjunctive_formular',3,'p_conjunctive_formular','bool.py',59),
  ('implicative_formular -> ( formular IMPLICATION formular )','implicative_formular',5,'p_implicative_formular','bool.py',66),
  ('implicative_formular -> formular IMPLICATION formular','implicative_formular',3,'p_implicative_formular','bool.py',67),
]