import ast

def to_tree(expr):
  if(isinstance(expr, ast.Call)):
    return [expr.func.id] + list(map(to_tree, expr.args))
  if(isinstance(expr, ast.Num)):
    return expr.n
  if(isinstance(expr, ast.Name)):
    return expr.id
  if(isinstance(expr, ast.BinOp)):
    return [type(expr.op).__name__, to_tree(expr.left), to_tree(expr.right)]

def from_str(str):
  return to_tree(ast.parse(str).body[0].value)
