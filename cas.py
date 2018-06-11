# Guidelines:
# When returning any subclass of expr, must call eval on the value first
# Unencapsulated numbers should not exist in an expression tree

import numbers

class Val():
  value = None

  def eval(self):
    raise NotImplementedError("Class Val should not be instantiated!")

  def __eq__(self, other):
    return self.value == other.value

  def __init__(self, value):
    self.value = value

class Var(Val):
  def __str__(self):
    if(self.value):
      return str(value.eval())
    else:
      return self.label

  def __eq__(self, other):
    return isinstance(other, Var) and super().__eq__(other) and self.label == other.label

  def eval(self):
    if(self.value):
      return self.value.eval()
    else:
      return self

  def __init__(self, value, label):
    self.label = label
    super().__init__(value)

class Num(Val):
  def __str__(self):
    # return "{" + str(self.value) + "}" # debug
    return str(self.value)

  def eval(self):
    return self

class Expr():
  def eval(self):
    raise NotImplementedError("Class Expr should not be instantiated!")

  def __eq__(self, other):
    return isinstance(other, Expr) and self.car == other.car and self.cdr == other.cdr

  def __init__(self, car, cdr):
    self.car = car
    self.cdr = cdr

class Product(Expr):
  def __str__(self):
    return str(self.car) + "*" + str(self.cdr)

  def eval(self):
    self.car = self.car.eval()
    self.cdr = self.cdr.eval()

    if(isinstance(self.car, Num) and isinstance(self.cdr, Num)):
      return Num(self.car.value * self.cdr.value)
    else:
      if(isinstance(self.car, Expt) and isinstance(self.cdr, Expt) and self.car.car == self.cdr.car):
        return Expt(self.car.car, Sum(self.car.cdr, self.cdr.cdr)).eval()
      return self

class Sum(Expr):
  def __str__(self):
    return str(self.car) + "+" + str(self.cdr)

  def eval(self):
    self.car = self.car.eval()
    self.cdr = self.cdr.eval()

    if(isinstance(self.car, Num) and isinstance(self.cdr, Num)):
      return Num(self.car.value + self.cdr.value)
    else:
      return self

class Expt(Expr):
  def __str__(self):
    return str(self.car) + "^" + str(self.cdr)

  def eval(self):
    self.car = self.car.eval()
    self.cdr = self.cdr.eval()

    if(isinstance(self.car, Num) and isinstance(self.cdr, Num)):
      return Num(self.car.value ** self.cdr.value)
    else:
      if(self.car.value == 0 or self.car.value == 1):
        return self.car
      elif(self.cdr.value == 0):
        return Num(1)
      elif(self.cdr.value == 1):
        return self.car
      return self

class Diff(Expr):
  def __str__(self):
    return str(self.car) + "-" + str(self.cdr)

  def eval(self):
    self.car = self.car.eval()
    self.cdr = self.cdr.eval()

    if(isinstance(self.car, Num) and isinstance(self.cdr, Num)):
      return Num(self.car.value - self.cdr.value)
    else:
      return self

#print(Expt(Var(None, "e"), Sum(Num(0.5), Num(0.5))).eval())
#print(Product(Expt(Var(None, "f"), Num(3)), Expt(Var(None, "e"), Num(2))).eval())
