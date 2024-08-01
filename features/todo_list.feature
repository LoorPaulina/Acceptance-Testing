Feature: To-Do List Management

  Scenario: Adding tasks to the To-Do list
    Given I have an empty To-Do list
    When I add a task with title "Pay bills", description "Pay electricity and water bills", due date "2024-08-05", and priority "Medium"
    And I add a task with title "Buy groceries", description "Buy milk, eggs, and bread", due date "2024-08-01", and priority "High"
    Then the To-Do list should have 2 tasks
    And the tasks should be:
      | title            | description                       | due_date   | priority |
      | Pay bills        | Pay electricity and water bills   | 2024-08-05 | Medium   |
      | Buy groceries    | Buy milk, eggs, and bread          | 2024-08-01 | High     |

  Scenario: Sorting tasks by priority
    Given I have tasks in my To-Do list
    When I sort tasks by priority
    Then the tasks should be sorted by priority
      | title        | description                        | due_date   | priority |
      | Buy groceries | Buy milk, eggs, and bread         | 2024-08-01 | High     |
      | Pay bills    | Pay electricity and water bills    | 2024-08-05 | Medium   |

      
  Scenario: Marking a task as completed
    Given I have tasks in my To-Do list
    When I mark the task with title "Buy groceries" as completed
    Then the task with title "Buy groceries" should be marked as completed

  Scenario: Searching for tasks
    Given I have tasks in my To-Do list
    When I search for tasks with keyword "bills"
    Then I should see tasks that include the keyword "bills"
    And the search results should be:
      | title         | description                       | due_date   | priority |
      | Pay bills     | Pay electricity and water bills   | 2024-08-05 | Medium   |

  Scenario: Clearing all tasks
    Given I have tasks in my To-Do list
    When I clear all tasks
    Then the To-Do list should be empty
