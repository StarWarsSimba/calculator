# Questions to check your understanding

Our HOWTO documents contain quite a bit of cut-and-paste code.  
You don't have to write that code, but you do need to understand it. 
The purpose of these questions is to check your understanding as you 
work through the HOWTO.  

### 1 

Consider the following code. 
```python
five = IntConst(5)
print(5 == five)   # Comparison 1
print(five == 5)   # Comparison 2
```

Does the `__eq__` method of `IntConst` get called only in Comparison 
1, only in Comparison 2, in both, or in neither?

Both.

### 2

I noted that `__str__` method of
`Plus` is recursive, but I don't see an explicit call to `__str__`. 
Where is it?

The f-string notation calls the `__str__` method on `self.left` and `self.right`.

### 3

How do we know that the `eval` method will not loop forever (i.e., 
it will eventually reach a base case)?

Because the base case is defined.

### 4

The constructor for a `Plus` node says that it takes two `Expr` nodes
as arguments, but we are passing it `IntConst` and `Plus` nodes.  Is 
this ok?  Why or why not? 

This is okay because `IntConst` and `Plus` are subclasses of the `Expr`
class.

### 5

Method `_apply` returns an `int` rather than an `IntConst`.
How does the result of a binary operation become an
`IntConst` object? 

In the `eval` method inside the `BinOp` class, an `IntConst` object is 
returned with the `_apply` method passed into the new object.

### 6

We noted earlier that an expression like `2+(5*3)` could
be expressed algebraically (this is also called "infix" notation),
in reverse Polish notation (also called "postfix") like `2 5 3 * +`, or
in "prefix" notation like `+ 2 * 5 3` or `(+ (2 (* 5 3))`.  Which of 
these notations
have we adopted for the `__str__` methods of our `Expr` classes?

We used the algebraic notation for the `__str__` methods of the `Expr`
classes.

### 7 

Our postfix notation uses "~" for negation and reserves
"-" for subtraction.  Why? Can you give an example 
postfix (reverse Polish notation) expression that
would be ambiguous if we used "-" as both a 
unary and binary operation?

`2 3 -` evaluates to `(2 - 3) => -1`, and `2 3 ~` evaluates to `2 => 2`
and `(~3) => -3`

### 8

Suppose we wanted to add exponentiation to our calculator, so
that the RPN expression `5 2 ^` would evaluate to 25 (5 squared)
and `5 3 ^` would evaluate to 125 (5 cubed).  Assume the lexer
returns a token `lex.TokenPat.POWER`.  What new class would I
need to add to `expr.py`, and what would it be a subclass of? 
What change would I need to make to `rpncalc.py`?

A class for exponents called `Pow` would need to be added, and would be
a subclass of `BinOp`. Because it would be a subclass of `BinOp`, there
is no need for another `elif` statement in `rpncalc.py`, but the dict
at the top of the file would need to have `lex.TokenCat.POWER` assigned
to `expr.Pow`.