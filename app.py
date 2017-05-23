from apistar import App, Include, Route, schema
from apistar.docs import docs_routes
from apistar.http import Response
from apistar.statics import static_routes


_items = [
    # (0, 'Get Water'),
]


class ToDoTitle(schema.String):
    min_length=1


def list_todo_items() -> schema.List[ToDoTitle]:
    """
    List all available todos
    """
    return [ToDoTitle(item[1]) for item in _items]


def add_todo(todo_title: ToDoTitle) -> ToDoTitle:
    todo_obj = ToDoTitle(
        todo_title
    )
    _items.append((len(_items), todo_obj))
    return todo_obj


def get_todo(todo_id: int) -> ToDoTitle:
    return ToDoTitle(_items[todo_id][1])


def edit_todo(todo_id: int, new_title: ToDoTitle) -> ToDoTitle:
    _items[todo_id] = (todo_id, new_title)
    return ToDoTitle(new_title)


def delete_todo(todo_id: int) -> ToDoTitle:
    return _items.pop(todo_id)[1]


routes = [
    Route('/todos', 'GET', list_todo_items),
    Route('/todos', 'POST', add_todo),
    Route('/todos/{todo_id}/', 'GET', get_todo),
    Route('/todos/{todo_id}/', 'PUT', edit_todo),
    Route('/todos/{todo_id}/', 'DELETE', delete_todo),
    Include('/docs', docs_routes),
    Include('/static', static_routes)
]


app = App(routes=routes)
