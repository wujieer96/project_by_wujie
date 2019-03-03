L=[]
L.append(r'<?xml version="1.0"?>')
L.append(r'<root>')
L.append(encode('some&data'))
L.append(r'</root>')
return ''.join(L)