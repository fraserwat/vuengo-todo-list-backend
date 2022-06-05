from doctest import debug_script

from django.db import models


class Task(models.Model):
    TODO = "todo"
    DONE = "done"

    STATUS_CHOCIES = ((TODO, "Todo"), (DONE, "Done"))

    description = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=STATUS_CHOCIES, default=TODO)

    def __str__(self) -> str:
        return f"{ self.description } [{str(self.status).upper()}]"
