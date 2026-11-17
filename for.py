'''tokens 
for = 300
target_list = 50
in = 305
expresion_list = 55
: = 60
simple_stmt = 2000
suite = 3000
else = 310
suite_else = 4000
new_line = 65
''' 
def start(tokens):
	error = ''
	i = 0 
	j = 0 
	i, error = for(tokens,i)
 	if error != '':
		return error
	if i<len(tokens):
		return f¨Error sintactico simbolo inesperado '{tokens[i]}'¨
	return 'VALIDO'

def for(tokens,i):
	while i<len(tokens) and tokens[i] == 300:
		if i<len(tokens) and tokens[i] == 300:
			i = i + 1
		else:
			return i, 'La expresion debe comenzar con for'
		elif tokens[i] == 50:
			i = i + 1
		else:
			return i, 'La expresion debe continuar con target_list'
		elif tokens[i] == 305:
			i = i + 1
		else:
			return i, 'La expresion debe continuar con in'
		elif tokens[i] == 55:
			i = i + 1
		else:
			return i, 'La expresion debe continuar con expression_list'
		elif tokens[i] == 60:
			i = i + 1
		else:
			return i, 'La expresion debe continuar con :'