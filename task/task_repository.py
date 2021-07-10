from task import task as task_entity


class TaskRepository:
    def __init__(self):
        self.tasks = {}

    def add_task(self, name, user_id, project_id):
        task = task_entity.Task(name, user_id, project_id)
        user_store = self.tasks.get(user_id) if user_id in self.tasks else {}
        user_store[task.id] = task
        self.tasks[user_id] = user_store

    def find_all_by_project(self, user_id, project_id):
        return filter(lambda t: t.project_id == project_id, (self.tasks.get(user_id) or {}).values())

    def find_task(self, user_id, task_id):
        user_tasks = self.tasks.get(user_id)
        return user_tasks.get(task_id) if user_tasks is not None else None

    def delete_task(self, user_id, task_id):
        tasks = self.tasks.get(user_id) or {}
        if task_id in tasks:
            del tasks[task_id]
