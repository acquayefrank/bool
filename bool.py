import ply.lex as lex
import ply.yacc as yacc


tokens = [
    'VAR',
    'IMPLICATION',
    'CONJUNCTION',
    'DISJUNCTION',
    'LPAREN',
    'RPAREN',
]


states = (
    ('negation', 'exclusive'),
)


t_IMPLICATION = r'->'
t_CONJUNCTION = r'/\\'
t_DISJUNCTION = r'\\/'
t_LPAREN = r'\('
t_RPAREN = r'\)'


def t_NEGATION(t):
    r'~'
    t.lexer.begin('negation')


def t_negation_VAR(t):
    r'[a-z]'
    val = t.value
    if val in t.lexer.values_of_variables:
        t.value = t.lexer.values_of_variables.index(val) + 1
    else:
        t.lexer.values_of_variables.append(val)
        t.value = len(t.lexer.values_of_variables)
    t.value *= (-1)
    t.lexer.begin('INITIAL')
    return t


def t_VAR(t):
    r'[a-z]'
    val = t.value
    if val in t.lexer.values_of_variables:
        t.value = t.lexer.values_of_variables.index(val)+1
    else:
        t.lexer.values_of_variables.append(val)
        t.value = len(t.lexer.values_of_variables)
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


t_negation_ignore = " \t\n"


t_ignore = ' \t'


def t_negation_error(t):
    print('Lexical error: "' + str(t.value[0]) + '" in line ' + str(t.lineno))
    t.lexer.skip(1)


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()
lexer.values_of_variables = []

clauses = []


def p_Fm_conj(p):
    'Fm : Fm CONJUNCTION Clause'
    clauses.append(p[3])


def p_Fm_term(p):
    'Fm : Clause'
    clauses.append(p[1])


def p_Clause_impl(p):
    'Clause : LPAREN Var IMPLICATION Var RPAREN'
    p[0] = ((-1) * p[2], p[4])


def p_term_disj(p):
    'Clause : LPAREN Var DISJUNCTION Var RPAREN'
    p[0] = (p[2] , p[4])


def p_term_literal(p):
    'Clause : Var'
    p[0] = (p[1],0)


def p_literal_simple(p):
    'Var : VAR'
    p[0] = p[1]


def p_error(p):
    message = """
                Syntax error!
                Ensure you follow this grammar: 
                Fm      ::= Fm /\ Clause | Clause")
                Clause  ::= ( Var -> Var ) |")
                            ( Var \/ Var ) |")
                            Var"
                Var     ::= literal | ~ literal
            """
    print(message)
    raise SyntaxError("error in input!")


def find_resolution(el1, el2):
    for i in range(2):
        for j in range(2):
            if el1[i]!=0 and el2[j]!=0 and el1[i]+el2[j]==0:
                new_pair=(el1[(i+1)%2],el2[(j+1)%2])
                if new_pair[0] != 0 and new_pair[1] != 0 and new_pair[0] + new_pair[1] == 0:
                    return (0,0)
                return new_pair
    return 0


def resolution(left_bound, arr):
    init_size=len(arr)
    for i in range(left_bound, init_size):
        elem=arr[i]
        for j in range(0,left_bound):
            new_elem=find_resolution(elem, arr[j])
            if new_elem==0:
                continue
            if new_elem == (0,0):
                return -1,arr
            else:
                arr.append(new_elem)
    return init_size, arr


def main(clauses):
    left_bound=1
    while left_bound!=len(clauses):
        left_bound,clauses=resolution(left_bound,clauses)
        if left_bound== -1:
            return False
    return True


if __name__ == '__main__':
    parser = yacc.yacc()
    print("(Works with 2CNF)")
    print("type exit in order to close bool")
    while True:
        try:
            s = input('\nbool > ')
            if s == 'exit':
                break
        except EOFError:
            break
        if not s: continue

        try:
            parser.parse(s)
            is_satisfiable = main(clauses)
            if is_satisfiable:
                print('\033[1;32;40m' + '\n\t{}\tis satisfiable'.format(s) + '\x1b[0m')
            else:
                print('\033[1;31;40m' + '\n\t{}\tis unsatisfiable'.format(s) + '\x1b[0m')
        except SyntaxError:
            continue
        clauses.clear() # Used to fix sideeffects

