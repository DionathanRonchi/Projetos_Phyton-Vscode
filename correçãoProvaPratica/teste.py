# teste.py
# Testa as funções do módulo cardapio.

from cardapio import cadastrar_item, listar_itens, buscar_por_id
from models import Item


item1 = Item("Pastel", 8.00, "Lanche", True)
item2 = Item("Suco", 7.00, "Bebida", True)

cadastrar_item(item1)
cadastrar_item(item2)

print("Itens cadastrados:")

itens = listar_itens()

for item in itens:
    item.exibir()


print("\nBusca por ID:")

item = buscar_por_id(1)

if item:
    item.exibir()
else:
    print("Item não encontrado.")


print("\nBusca por ID inexistente:")

item = buscar_por_id(9999)

if item:
    item.exibir()
else:
    print("Item não encontrado.")