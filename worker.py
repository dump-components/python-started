from planning.search_task import SearchTask
from planning.defined_task_to_job import DefinedTaskToJob

task = SearchTask().get
job = DefinedTaskToJob.by_type_task(task)
job.run()
