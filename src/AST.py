from typing import Any, Callable


class program:
    
    def __init__(self):
        self.statements = []
        self.scope = []
    
    def __str__(self) -> str:
        finalstr = ""
        for statement in self.statements:
            finalstr += str(statement)
        return finalstr
    
    @staticmethod
    def typeof(statement):
        if statement != 'EOF':
            return statement.type
        elif statement == 'EOF':
            return 'EOF'
        else:
            raise TypeError('Invalid Type')
    
    def add_statement(self, statement : Any):
        if statement != 'EOF':
            
            match(self.typeof(statement)):
                case 'declaration': self.scope.append(statement)
                case 'function': self.scope.append(statement)
                case 'class': self.scope.append(statement)
                case 'subclass': self.scope.append(statement)
            
            
            self.statements.append(statement)
        elif statement == 'EOF':
            self.statements.append('EOF')
        else:
            raise TypeError('Invalid Type')

class Literal:

    def __init__(self, value, type):
        match type:
            case 'true':
                self.value = True
                self.type = 'boolean'
            case 'false':
                self.value = False
                self.type = 'boolean'
            case 'null':
                self.value = None
                self.type = 'NullType'
            case 'number':
                self.value = float(value)
                self.type = 'number'
            case 'string':
                self.value = str(value)
                self.type = 'string'
    def __str__(self):
        return '[literal(' + self.type + ')]: ' + str(self.value)

#-------------------------------------------------------------------------------

class VariableDeclaration:
    def __init__(self, name : str, value : Any, parent : Any):
        self.name = name
        self.value = value
        self.type = 'declaration'
        self.parent = parent
    def __str__(self):
        return self.name + ': created [' + str(self.value) + ']'

#-------------------------------------------------------------------------------

class VariableAssignment:
    def __init__(self, name : str, value : Any, parent : Any):
        self.name = name
        self.value = value
        self.type = 'assignment'
        self.parent = parent
    def __str__(self):
        return self.name + ': updated [' + str(self.value) + ']'

#-------------------------------------------------------------------------------

class Return:
    def __init__(self, value : Any, parent : Any):
        self.value = value
        self.type = 'return'
        self.parent = parent
    def __str__(self):
        return 'return: ' + str(self.value)

#-------------------------------------------------------------------------------

class parameter:
    def __init__(self, name : str, default_value : Any):
        self.name = name
        self.default_value = default_value
        self.Type = 'parameter'
class Function:
    def __init__(self, name : str, parameters : list[parameter], parent : Any):
        self.name = name
        self.parameters = parameters
        self.body = []
        self.type = 'function'
        self.scope = []
        self.parent = parent
        
        for param in self.parameters:
            self.scope.append(param)
    def __str__(self):
        final = 'function: ' + self.name + '('
        for param in self.parameters:
            if param == self.parameters[0]:
                final += param.name
            else:
                final += ', ' +  param.name
        final += ') {'
        for statement in self.body:
            final += '\n\t' + str(statement)
        final += '\n}'
        return final

class Call:
    def __init__(self, callee : str, arguments : list, parent : Any):
        self.callee = callee
        self.arguments = arguments
        self.type = 'call'
        self.parent = parent
    def __str__(self):
        final = 'call: ' + self.callee + '('
        for param in self.arguments:
            if param == self.arguments[0]:
                final += param
            else:
                final += ', ' +  param
        final += ')'
        return final

#-------------------------------------------------------------------------------

class Class:
    def getDunder(self, Methods):
        for method in Methods:
            if method.name == '_init_':
                self.Constructor = method
            elif method.name == '_delete_':
                self.Destructor = method
            
            elif method.name == '_add_':
                self.add = method
            elif method.name == '_sub_':
                self.sub = method
            elif method.name == '_mul_':
                self.mul = method
            elif method.name == '_div_':
                self.div = method
            elif method.name == '_mod_':
                self.mod = method
            elif method.name == '_pow_':
                self.pow = method
            
            elif method.name == '_eq_':
                self.eq = method
            elif method.name == '_ne_':
                self.ne = method
            elif method.name == '_lt_':
                self.lt = method
            elif method.name == '_le_':
                self.le = method
            elif method.name == '_gt_':
                self.gt = method
            elif method.name == '_ge_':
                self.add = method
            elif method.name == '_string_':
                self.string = method
            
            elif method.name == '_call_':
                self.call = method
            elif method.name == '_getitem_':
                self.getitem = method
            elif method.name == '_setitem_':
                self.setitem = method
    
    def __init__(self, name : str, Methods : list[Function], parent : Any):
        self.name = name
        self.methods = Methods
        self.parent = parent
        
        self.getDunder(self.methods)
        
        self.type = 'class'
        self.scope = []
        self.scope += Methods

class SubClass(Class):
    def __init__(self, name : str, Methods : list[Function], Superclass : Class, parent : Any):
        self.super = Superclass
        self.name = name
        self.methods = Methods
        self.parent = parent
        
        self.getDunder(self.methods)
        
        self.type = 'subclass'
        self.scope = []
        self.scope += Methods

#-------------------------------------------------------------------------------------------------


class Binary:
    def __init__(self, Left : Any, Right : Any, Operator : str, parent):
        self.Left = Left
        self.Right = Right
        self.Operator = Operator
        self.type = 'Binary'
        self.parent = parent
    def __str__(self):
        return ' (' + str(self.Left) + ' ' + self.Operator + ' ' + str(self.Right) + ') '

class addition(Binary):
    def __init__(self, Left, Right, parent):
        super().__init__(Left, Right, '+', parent)
class subtraction(Binary):
    def __init__(self, Left, Right, parent):
        super().__init__(Left, Right, '-', parent)
class multiplication(Binary):
    def __init__(self, Left, Right, parent):
        super().__init__(Left, Right, '*', parent)
class division(Binary):
    def __init__(self, Left, Right, parent):
        super().__init__(Left, Right, '/', parent)
class power(Binary):
    def __init__(self, Left, Right, parent):
        super().__init__(Left, Right, '^', parent)
class mod(Binary):
    def __init__(self, Left, Right, parent):
        super().__init__(Left, Right, '%', parent)

#-----------------------------------------------------

class Unary:
    def __init__(self, Operator : str, Right : Any, parent):
        self.Operator = Operator
        self.Right = Right
        self.parent = parent
        self.type = 'unary'
    def __str__(self):
        return ' (' + self.Operator + str(self.Right) + ') '
class UnaryNegate(Unary):
    def __init__(self, Right, parent):
        super().__init__('-', Right, parent)
class UnaryNot(Unary):
    def __init__(self, Right, parent):
        super().__init__('!', Right, parent)

#-----------------------------------------------------

class Condition(Binary):
    operators = [
        '==',
        '>',
        '>=',
        '<',
        '<=',
        '!=',
    ]
    
    def __init__(self, Left, Right, Operator, parent):
        if Operator in self.operators:
            super().__init__(Left, Right, Operator, parent)
        else:
            raise SyntaxError('Expected Comparison Operator')

#--------------------------------------------------------------------

class IfStatement:
    def __init__(self, condition : Condition, parent):
        self.condition = condition
        self.body = []
        self.parent = paren

class Loop(IfStatement):
    def __init__(self, condition : Condition, parent):
        super().__init__(condition, parent)

