from django.contrib.auth.models import User
from django.db import models
from audioop import reverse
from django.utils.translation import gettext_lazy as _


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    social = models.CharField(max_length=200, verbose_name=_('social'), null=True, blank=True)
    address = models.CharField(max_length=1000, verbose_name=_('address'), null=True, blank=True)
    img = models.ImageField(blank=False, upload_to='images', default='media/no-image.jpg')
    brightday = models.DateField(verbose_name=_('brightday'), null=True, blank=True)

    class Meta:
        verbose_name_plural = _('users')
        verbose_name = _('user')

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('profile', kwargs={'pk': self.pk})

