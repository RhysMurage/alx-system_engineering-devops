import requests
import sys

def fetch_employee_todo_list(employee_id):
    """
    Fetches the TODO list for a given employee ID and displays the progress.

    Args:
        employee_id (int): The ID of the employee whose TODO list is to be fetched.

    Returns:
        None
    """
    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
    response = requests.get(url)
    todos = response.json()

    if response.status_code != 200:
        print(f"Error: Unable to fetch TODO list for employee ID {employee_id}")
        return

    completed_tasks = [todo['title'] for todo in todos if todo['completed']]
    total_tasks = len(todos)
    num_completed_tasks = len(completed_tasks)

    user_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    employee_name = user_response.json()['name']

    print(f"Employee {employee_name} is done with tasks ({num_completed_tasks}/{total_tasks}):")
    print(f"{employee_name}: {num_completed_tasks}/{total_tasks}")
    for task in completed_tasks:
        print(f"\t{task}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    fetch_employee_todo_list(employee_id)
