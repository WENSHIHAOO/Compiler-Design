#Name: Shihao Wen
#Netid: shiwen
#Student ID: 113085521
import sys
import ply.lex as lex
import ply.yacc as yacc
import decaf_lexer
import decaf_parser
import decaf_typecheck
import decaf_codegen

def just_scan():
    fn = sys.argv[1] if len(sys.argv) > 1 else ""
    if fn == "":
        print("Missing file name for source program.")
        print("USAGE: python3 decaf_checker.py <decaf_source_file_name>")
        sys.exit()
    lexer = lex.lex(module = decaf_lexer, debug = 1)

    fh = open(fn, 'r')
    source = fh.read()
    lexer.input(source)
    next_token = lexer.token()
    while next_token != None:
        print(next_token)
        next_token = lexer.token()

def main():
    fn = sys.argv[1] if len(sys.argv) > 1 else ""
    if fn == "":
        print("Missing file name for source program.")
        print("USAGE: python3 decaf_checker.py <decaf_source_file_name>")
        sys.exit()
    lexer = lex.lex(module = decaf_lexer, debug = 1)
    parser = yacc.yacc(module = decaf_parser, debug = 1)

    fh = open(fn, 'r')
    source = fh.read()
    fh.close()
    decaf_parser.Initialization()
    parser.parse(source, lexer = lexer, debug = 1)
    print("Yes")
    print()
    decaf_typecheck.check_program()
    for Class in decaf_parser.class_table.values():
        print("--------------------------------------------------------------------------")
        print(Class)
    with open(fn[:-6]+'.ami', 'w') as file:
        file.write(decaf_codegen.codegen_program())

if __name__ == "__main__":
    #just_scan()
    main()
