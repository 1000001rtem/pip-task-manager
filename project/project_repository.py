from project import project as project_entity


class ProjectRepository:
    def __init__(self):
        self.projects = {}

    def add_project(self, name, user_id):
        project = project_entity.Project(name, user_id)
        user_store = self.projects.get(user_id) if user_id in self.projects else {}
        user_store[project.id] = project
        self.projects[user_id] = user_store

    def find_all(self, user_id):
        return self.projects.get(user_id) or {}

    def find_project(self, user_id, project_id):
        user_projects = self.projects.get(user_id)
        return user_projects.get(project_id) if user_projects is not None else None

    def delete_project(self, user_id, project_id):
        projects = self.projects.get(user_id) or {}
        if project_id in projects:
            del projects[project_id]
