grammar Iona;

Lparen : '(' ;
Rparen : ')' ;
Lambda : '\\' ;
Dot : '.' ;
Semicolon : ';' ;
Equal : '=' ;
Bar : '|' ;

IntLiteral : '-'? [0-9]+;

LowerIdentifier : [a-z][a-zA-Z0-9]*;
UpperIdentifier : [A-Z][a-zA-Z0-9]*;

WS : 
    [ \t\r\n] -> skip
    ;

program : dataDecl* expr EOF ;

dataDecl : 'data' UpperIdentifier '=' dataDeclPart ('|' dataDeclPart)* ';' ;
dataDeclPart : UpperIdentifier+;

expr
    : lambdaExpr # expr1
    | matchExpr  # expr2
    | letExpr    # expr3
    ;

lambdaExpr
    : '\\' LowerIdentifier '->' lambdaExpr   # lambda1
    | addExpr                                # lambda2
    ;

addExpr
    : addExpr ('+' | '-') mulExpr            # add1
    | mulExpr                                # add2
    ;

mulExpr
    : mulExpr ('*' | '/') appExpr            # mul1
    | appExpr                                # mul2
    ;

appExpr
    : appExpr primaryExpr                    # app1
    | primaryExpr                            # app2
    ;

primaryExpr
    : IntLiteral                             # primary1
    | LowerIdentifier                        # primary2
    | '(' expr ')'                           # primary3
    | UpperIdentifier                        # primary4
    ;

matchExpr : 'match' expr 'with' matchCase+ ;
matchCase : '|' UpperIdentifier LowerIdentifier* '->' expr ;

letExpr : 'let' LowerIdentifier '=' expr 'in' expr;