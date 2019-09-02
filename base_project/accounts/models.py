from django.db import models


class Profile(models.Model):
    owner = models.OneToOneField('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.owner.get_full_name() or self.owner.username

    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfis"
