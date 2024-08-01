from behave import given, when, then

# Initialize the To-Do list
@given('I have an empty To-Do list')
def step_impl(context):
    context.todo_list = []

@given('I have tasks in my To-Do list')
def step_impl(context):
    context.todo_list = [
        {"title": "Pay bills", "description": "Pay electricity and water bills", "due_date": "2024-08-05", "priority": "Medium"},
        {"title": "Buy groceries", "description": "Buy milk, eggs, and bread", "due_date": "2024-08-01", "priority": "High"}
    ]

# Adding tasks
@when('I add a task with title "{title}", description "{description}", due date "{due_date}", and priority "{priority}"')
def step_impl(context, title, description, due_date, priority):
    task = {"title": title, "description": description, "due_date": due_date, "priority": priority}
    context.todo_list.append(task)

# Checking task count
@then('the To-Do list should have {count} tasks')
def step_impl(context, count):
    assert len(context.todo_list) == int(count)

# Sorting tasks
@when('I sort tasks by priority')
def step_impl(context):
    priority_order = {"High": 1, "Medium": 2, "Low": 3}
    context.todo_list.sort(key=lambda x: priority_order[x["priority"]])
    
@then('the tasks should be sorted by priority')
def step_impl(context):
    if context.table:
        expected_tasks = [dict(zip(context.table.headings, row)) for row in context.table.rows]
        for expected_task, actual_task in zip(expected_tasks, context.todo_list):
            assert expected_task["title"] == actual_task["title"]
            assert expected_task["description"] == actual_task["description"]
            assert expected_task["due_date"] == actual_task["due_date"]
            assert expected_task["priority"] == actual_task["priority"]
    else:
        assert context.todo_list == []

# Marking tasks as completed
@when('I mark the task with title "{title}" as completed')
def step_impl(context, title):
    for task in context.todo_list:
        if task["title"] == title:
            task["completed"] = True
            break

@then('the task with title "{title}" should be marked as completed')
def step_impl(context, title):
    for task in context.todo_list:
        if task["title"] == title:
            assert task.get("completed") is True
            return
    assert False, f'Task with title "{title}" not found or not completed.'

# Searching tasks
@when('I search for tasks with keyword "{keyword}"')
def step_impl(context, keyword):
    context.search_results = [task for task in context.todo_list if keyword in task["title"] or keyword in task["description"]]

@then('I should see tasks that include the keyword "{keyword}"')
def step_impl(context, keyword):
    assert all(keyword in (task["title"] + task["description"]) for task in context.search_results)

@then('the search results should be')
def step_impl(context):
    expected_search_results = [dict(zip(context.table.headings, row)) for row in context.table.rows]
    assert context.search_results == expected_search_results

# Clearing tasks
@when('I clear all tasks')
def step_impl(context):
    context.todo_list.clear()

@then('the To-Do list should be empty')
def step_impl(context):
    assert not context.todo_list

# Validating the task list
@then('the tasks should be')
def step_impl(context):
    if context.table:
        expected_tasks = [dict(zip(context.table.headings, row)) for row in context.table.rows]
        assert context.todo_list == expected_tasks
    else:
        assert context.todo_list == []
