import cas
import parse

def op_to_class(op):
  table = {
    "Add": cas.Sum,
    "Mult": cas.Product,
    "Pow": cas.Expt,
    "BitXor": cas.Expt,
    "Sub": cas.Diff
  }
  return table[op]

def convert_ast(expr):
  if(isinstance(expr, list)):
    return op_to_class(expr[0])(convert_ast(expr[1]), convert_ast(expr[2]))
  elif(isinstance(expr, int)):
    return cas.Num(expr)
  elif(isinstance(expr, str)):
    return cas.Var(None, expr)
  else:
    raise RuntimeError("Something went wrong converting atom: %s" % expr)

#print(convert_ast(parse.from_str("(e^2)*(e^3)")).eval())

while True:
  line = input('> ')
  
  if len(line) == 0:
    break
  
  print(convert_ast(parse.from_str(line)).eval())
