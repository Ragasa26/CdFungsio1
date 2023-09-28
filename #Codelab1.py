#Kegiatan 1
def plus (x,y):
    return x+y

def minus (x,y):
    return x-y

result = minus(5,2)
print(result)

def mult (x,y):
    return x*y

result = mult(5,2)
print(result)

def div(x,y):
    return x/y

result = div(5,2)
print(result)

def treee(node) :
    if type(node) in (int,float):
      return node
    elif type(node) is tuple and len(node) == 3:
      operator, left_operand, right_operand = node
    if operator == '+':
          return treee(left_operand) + treee(right_operand)
    elif operator == '-':
          return treee(left_operand) + treee(right_operand)
    elif operator == '*':
          return treee(left_operand) + treee(right_operand)
    elif operator == '-':
          return treee(left_operand) + treee(right_operand)

expression_tree = ('*',('+',2,3),('-',5,1))
print(treee(expression_tree))

def treee(node) :
    if type(node) in (int,float):
      return node
    elif type(node) is tuple and len(node) == 3:
       left_operand, operator, right_operand = node
    if operator == '+':
          return treee(left_operand) + treee(right_operand)
    elif operator == '-':
          return treee(left_operand) + treee(right_operand)
    elif operator == '*':
          return treee(left_operand) + treee(right_operand)
    elif operator == '-':
          return treee(left_operand) + treee(right_operand)
expression_tree = ((2,'+',3),'*',(5,'-',1))
print(treee(expression_tree))