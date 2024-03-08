class Node():
  def __init__(self, data, next=None): #Data no se almacena ese nodo y next a donde nos lleva
    self.data = data #Nos va a llevar a data
    self.next = next #Nos va a llevar al siguiente

node1 = None #Los lugares a los que apuntan estos nodos pueden ser modificados
node2 = Node("A", None)
node3 = Node("B", node2)

node1 = Node("C", node3)

head = None

print(node2) # <__main__.Node object at 0x7fc842dd6e90> #La referencia en memoria
print(node2.data) # A #El dato que tiene
print(node2.next) # None #Lo que sigue despues, es decir el espacio por llenar none
print(node3.next) # <__main__.Node object at 0x7f241fc96e90>
print(node3.next.data) # A #Aqui vemos que el siguiente nos lleva al nodo 1 y además nos muestra el dato de nodo 1 que esta asociado
print(node1.next) # AttributeError: 'NoneType' object has no attribute 'next'

print(node1.next.data) # B <= porque pusimos en la linea 14 que ahora el node1 apunta a node3
print(node1.data) # C

for count in range(1,5): #Itera en count en un rango de 1 a 5
  head = Node(count, head) #Por lo tanto ahora va a recibir el conteo

while head != None: #Aqui los organiza 
  print(head.data)
  head = head.next