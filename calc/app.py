from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def do_add():
    """Add a and b"""
    
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a, b)
    
    return str(result)
    
@app.route('/sub')
def do_sub():
    """Subtract b from a"""
    
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = sub(b, a)
    
    return str(result)
    
    
@app.route('/mult')
def do_mult():        
    """Multiply a and b"""
    
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = mult(a, b)
    
    return str(result)
    
@app.route('/div')
def do_div():
    """Divide a and b""" 
    
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = div(a, b)
    
    return str(result)   

##PART TWO
OPERATORS = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}

@app.route('/math/<oper>')
def do_math(oper):
    """Do all math a and b"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = OPERATORS[oper](a, b)
    
    return str(result)