from repository.migrations.migration import Migration
from repository.models.task_model import TaskModel
from repository.repository.repository import task

Migration.make(database=task, model=TaskModel)