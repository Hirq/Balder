from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User


class Quest(models.Model):
    LOW = 'LOW'
    MIDDLE = 'MIDDLE'
    HARD = 'HARD'
    Levels = (
        (LOW, 'LOW'),
        (MIDDLE, 'MIDDLE'),
        (HARD, 'HARD'),
    )
    who = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    quest_name = models.CharField(max_length=400, default='Quest')
    quest_text = models.TextField(max_length=2100, default='text')
    pub_date = models.DateTimeField('date published', default="")
    done_date = models.DateTimeField(null=True, blank=True)
    levels = models.CharField(max_length=6, choices=Levels, default=LOW)
    done_quest = models.BooleanField(default=False)
    today_quest = models.BooleanField(default=False)
    daily_quest = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('todo:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.quest_name

    def __unicode__(self):
        return u"%s %s %s %s" % (self.quest_name, self.quest_text, self.pub_date, self.levels)


class Choice(models.Model):
    quest = models.ForeignKey(Quest, on_delete=models.CASCADE, null=True)
    choice_text = models.TextField(max_length=2100)
    pub_date = models.DateTimeField('date', default='')

    def get_absolute_url(self):
        return reverse('todo:detail')

    def __str__(self):
        return self.choice_text


class Victory(models.Model):
    who = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    victory_text = models.CharField(max_length=400, default='You the best thing what u want save')
    pub_date = models.DateField('date', default='')

    def get_absolute_url(self):
        return reverse('todo:victory')

    def __str__(self):
        return self.victory_text


class Purpose(models.Model):
    who = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    purpose_text = models.CharField(max_length=400, default='Your purpose')
    pub_date = models.DateField('date', default='')

    def get_absolute_url(self):
        return reverse('todo:purpose')

    def __str__(self):
        return self.purpose_text
