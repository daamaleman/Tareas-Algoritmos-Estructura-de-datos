
import models.action_model  as am

# Agrega una nueva acción al historial
def add_action(history, redo_stack, action):
    node = am.ActionNode(action)
    if history:
        node.prev = history[-1]
        history[-1].next = node
    history.append(node)
    redo_stack.clear()  # Al hacer una nueva acción, se limpia el stack de rehacer
    print(f"Acción '{action}' realizada.")

# Deshace la última acción realizada
def undo_action(history, redo_stack):
    if not history:
        print("No hay acciones para deshacer.")
        return
    node = history.pop()
    redo_stack.append(node)
    print(f"Acción '{node.action}' deshecha.")

# Rehace la última acción deshecha
def redo_action(history, redo_stack):
    if not redo_stack:
        print("No hay acciones para rehacer.")
        return
    node = redo_stack.pop()
    if history:
        node.prev = history[-1]
        history[-1].next = node
    history.append(node)
    print(f"Acción '{node.action}' rehecha.")

# Muestra el historial actual de acciones
def show_history(history):
    if not history:
        print("Historial vacío.")
        return
    print("\nHistorial de acciones:")
    for i, node in enumerate(history, 1):
        print(f"{i}. {node.action}")
