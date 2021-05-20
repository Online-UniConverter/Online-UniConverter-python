import os
import json
import time
from mediaio.resource import Create, Info, Wait
from mediaio.mediaiorestclient import default_client

class Job(Create, Info, Wait):
    """Task class wrapping the REST v2/tasks endpoint. Enabling New Task Creation, Showing a task, Waiting for task,
    Finding a task, Deleting a task, Cancelling a running task.

    Usage::        
        >>> Job.create(name="import/url")
    """

    path = "v2/jobs"    


Job.convert_resources['jobs'] = Job
Job.convert_resources['job'] = Job
