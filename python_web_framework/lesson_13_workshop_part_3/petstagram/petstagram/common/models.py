## COMMON. MODELS.PY
from django.contrib.auth import get_user_model
from django.db import models

from petstagram.pets.models import Pet

UserModel = get_user_model()


class Comment(models.Model):
    comment = models.TextField()

    pet = models.ForeignKey(
        Pet,
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
