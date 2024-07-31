class Task:
    def __init__(self, title, description, due_date, priority):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def __str__(self):
        return f"{self.title} (Due: {self.due_date}, Priority: {self.priority}) - {'Completed' if self.completed else 'Pending'}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description, due_date, priority):
        task = Task(title, description, due_date, priority)
        self.tasks.append(task)

    def sort_tasks(self, by='priority'):
        if by == 'priority':
            self.tasks.sort(key=lambda x: x.priority)
        elif by == 'due_date':
            self.tasks.sort(key=lambda x: x.due_date)

    def list_tasks(self):
        return [str(task) for task in self.tasks]

    def mark_task_as_completed(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_as_completed()
                return True
        return False

    def clear_tasks(self):
        self.tasks = []
    
    def search_tasks(self, keyword):
        return [str(task) for task in self.tasks if keyword in task.title or keyword in task.description]

# Example usage
if __name__ == "__main__":
    todo_list = ToDoList()
    todo_list.add_task("Pay bills", "Pay electricity and water bills", "2024-08-05", "Medium")
    todo_list.add_task("Buy groceries", "Buy milk, eggs, and bread", "2024-08-01", "High")
    print(todo_list.list_tasks())
    todo_list.sort_tasks(by='due_date')
    print(todo_list.list_tasks())
    todo_list.mark_task_as_completed("Buy groceries")
    print(todo_list.list_tasks())
    print(todo_list.search_tasks("bills"))
    todo_list.clear_tasks()
    print(todo_list.list_tasks())
