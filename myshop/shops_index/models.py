from django.db import models
from django.urls import reverse
from django.template.defaultfilters import truncatechars
from django.utils.translation import gettext_lazy as _

RATING_CHOICES = ('0', '1', '2', '3', '4', '5')


class Shops(models.Model):
    STATUS_CHOICES = [
        ('d', 'Черновик'),
        ('r', 'Снято с продаж'),
        ('p', 'Продается'),
    ]
    title = models.CharField(max_length=255, verbose_name=_('title'))
    code_thing = models.IntegerField(verbose_name=_('code_thing'), default=0)
    img = models.ImageField(upload_to='images', verbose_name=_('img'))
    description = models.CharField(max_length=10000, verbose_name=_('description'))
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)
    finish_at = models.DateTimeField(auto_now=True)
    price = models.FloatField(verbose_name=_('price'), default=0)
    views_count = models.IntegerField(verbose_name=_('views_count'), default=0)
    group = models.ForeignKey('ShopsGroup', default=None, null=True, on_delete=models.CASCADE,
                              related_name='ShopsGroup', verbose_name=_('group'))
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='d', verbose_name=_('status'))
    tags = models.ManyToManyField('Tag', blank=True, verbose_name=_('tag'))

    class Meta:
        verbose_name_plural = _('goods')
        verbose_name = _('good')

    @property
    def short_description(self):
        return truncatechars(self.description, 15)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('shops', kwargs={'pk': self.pk})


class Tag(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('tag'))

    class Meta:
        verbose_name_plural = _('tags')
        verbose_name = _('tag')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tag', kwargs={'pk': self.pk})


class ShopsGroup(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('name'))
    img = models.ImageField(upload_to='images', verbose_name=_('img'))
    description = models.CharField(max_length=10000, verbose_name=_('description'))

    class Meta:
        verbose_name_plural = _('groups')
        verbose_name = _('group')

    class Meta:
        verbose_name_plural = _('groups')
        verbose_name = _('group')

    @property
    def short_description(self):
        return truncatechars(self.description, 15)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('group', kwargs={'pk': self.pk})


class ShopContacts(models.Model):
    address = models.CharField(max_length=100, verbose_name='Наименование')
    phone = models.CharField(max_length=10000, verbose_name='Описание')
    email = models.EmailField(verbose_name='Почта')


class ShopsComm(models.Model):
    STATUS_CHOICES = [
        ('r', 'Удалено администратором'),
        ('p', 'Опубликованно'),
    ]
    author = models.CharField(max_length=255, verbose_name=_('author'))
    grade = models.FloatField(verbose_name=_('grade'), default=0)
    comm = models.CharField(max_length=10000, verbose_name=_('comm'))
    group = models.ForeignKey('ShopsGroup', default=None, null=True, on_delete=models.CASCADE,
                              related_name='Shops', verbose_name=_('group'))
    shops = models.ForeignKey('Shops', default=None, null=True, on_delete=models.CASCADE,
                              related_name='ShopsGroup', verbose_name=_('shops'))
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='d', verbose_name=_('status'))

    class Meta:
        verbose_name_plural = _('comms')
        verbose_name = _('comm')


    def __str__(self):
        return self.author

    def get_absolute_url(self):
        return reverse('shops', kwargs={'pk': self.pk})
