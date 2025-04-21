from collections import defaultdict
from typing import List

class TodoList:
    def __init__(self):
        self.task_counter = 1   #Task Counter to assign unique IDs to tasks
        self.tasks = defaultdict(list) #Use defaultdict to store tasks for each user

    def addTask(self, user_id: int, task_description: str, due_date: int, tags: List[str]) -> int:
        """
        Add a task to TodoList for a give user. Returns a task ID
        """
        task_id = self.task_counter
        self.task_counter += 1

        self.tasks[user_id].append([due_date, task_description, set(tags), task_id, False])
    
    def getAllTasks(self, user_id: int) -> List[int]:
        """
        Return all incomplete tasks
        """
        return [task[1] for task in self.tasks[user_id] if not task[4]]

    def getTasksForTag(self, user_id: int, tag: str) -> List[str]:
        """
        Retrieve all incomplete task for a given user that have specified tag
        """
        return [task[1] for task in self.tasks[user_id] if tag in task[2] and not task[4]]
    
    def compeleteTask(self, user_id: int, task_id: int) -> None:
        """
        Mark a task as complete for a given user
        """
        for task in self.tasks[user_id]:
            if task[3] == task_id:
                task[4] = True
                break

obj = TodoList()
obj.addTask(1, "Learn Go", 12, ["action", "rpg"])
obj.addTask(1, "Contribute to Go", 256, ["Thriller", "Adventure"])
obj.addTask(2, "Learn Advanced Git", 10, ["Mystery", "Psychological"])

print(obj.getAllTasks(1))
print(obj.getTasksForTag(1, "Thriller"))
obj.compeleteTask(1, 1)
print(obj.tasks)
print(obj.getAllTasks(1))
