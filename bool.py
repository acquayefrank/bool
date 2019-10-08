import sys

import ply.lex as lex
import ply.yacc as yacc


tokens = ['CONJUNCTION', 'DISJUNCTION', 'IMPLICATION', 'VAR']
literals = ['(', ')', '~']


t_CONJUNCTION = r'/\\'
t_DISJUNCTION = r'\\/'
t_IMPLICATION = r'->'
t_VAR = r'[a-z]'
t_ignore = " \t"


clauses = []


def _clean_clause(p):
    return [ x for x in p if x ]

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lex.lex()


def p_formular(p):
    """formular : var
               | disjunctive_formular
               | conjunctive_formular
               | implicative_formular
               | negative_formular
               | '(' formular ')'
               """


def p_var(p):
    """ var : VAR """
    clauses.append(_clean_clause(p))


def p_disjunctive_formular(p):
    """
    disjunctive_formular : paren_disjunctive_formular
                         | no_paren_disjunctive_formular
    """


def p_paren_disjunctive_formular(p):
    """
    paren_disjunctive_formular : '(' formular DISJUNCTION formular ')'
    """
    clauses.append(_clean_clause(p))


def p_no_paren_disjunctive_formular(p):
    """
    no_paren_disjunctive_formular : formular DISJUNCTION formular 
    """
    clauses.append(_clean_clause(p))


def p_conjunctive_formular(p):
    """
    conjunctive_formular :  paren_conjunctive_formular
                         |  no_paren_conjunctive_formular 
    """


def p_paren_conjunctive_formular(p):
    """
    paren_conjunctive_formular : '(' formular CONJUNCTION formular ')'
    """
    clauses.append(_clean_clause(p))


def p_no_paren_conjunctive_formular(p):
    """
    no_paren_conjunctive_formular : formular CONJUNCTION formular 
    """
    clauses.append(_clean_clause(p))


def p_implicative_formular(p):
    """
    implicative_formular : paren_implicative_formular
                         |  no_paren_implicative_formular
    """


def p_paren_implicative_formular(p):
    """
    paren_implicative_formular : '(' formular IMPLICATION formular ')'
    """
    clauses.append(_clean_clause(p))

def p_no_paren_implicative_formular(p):
    """
    no_paren_implicative_formular : formular IMPLICATION formular
    """
    clauses.append(_clean_clause(p))


def p_negative_formular(p):
    """
    negative_formular : no_paren_negative_formular
    """


# def p_paren_negative_formular(p):
#     """
#     paren_negative_formular : '~' '(' formular ')'
#     """
#     clauses.append(_clean_clause(p))


def p_no_paren_negative_formular(p):
    """
    no_paren_negative_formular : '~' formular 
    """
    clauses.append(_clean_clause(p))


def p_error(p):
    try:
        print("Syntax error at '%s'" % p.value)
    except Exception:
        print("Hmmm, you're doing something funky, call the guy who wrote the code")
        sys.exit()


yacc.yacc()


if __name__ == '__main__':
    while True:
        try:
            s = input('bool supports 2CNF only > ')
            if s == 'exit':
                break
        except EOFError:
            break
        if not s: continue
        clauses.clear() # a work around for side effects
        yacc.parse(s)
        print(clauses)
