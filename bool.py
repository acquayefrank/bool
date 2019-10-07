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
    # generate_cnf(p[1])
    # generate_dnf(p[1])


def p_var(p):
    """ var : VAR """
    p[0] = p[1]


def p_disjunctive_formular(p):
    """
    disjunctive_formular : '(' formular DISJUNCTION formular ')'
                         |  formular DISJUNCTION formular 
    """
    p[0] = p[1]


def p_conjunctive_formular(p):
    """
    conjunctive_formular : '(' formular CONJUNCTION formular ')'
                         |  formular CONJUNCTION formular 
    """
    p[0] = p[1]


def p_implicative_formular(p):
    """
    implicative_formular : '(' formular IMPLICATION formular ')'
                         |  formular IMPLICATION formular
    """
    p[0] = p[1]


def p_negative_formular(p):
    """
    negative_formular : '~' '(' formular ')'
                      | '~' formular 
    """
    p[0] = p[1]


def p_error(p):
    try:
        print("Syntax error at '%s'" % p.value)
    except Exception:
        print("Hmmm, you're doing something funky, call the guy who wrote the code")
        sys.exit()


yacc.yacc()

def generate_cnf(p):
    print(p)

def generate_dnf(p):
    print(p)

if __name__ == '__main__':
    while 1:
        try:
            s = input('bool > ')
            if s == 'exit':
                break
        except EOFError:
            break
        if not s: continue
        yacc.parse(s)
