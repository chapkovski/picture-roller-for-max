from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

from os import listdir
import os, json, random
from os.path import isfile, join
from django.conf import settings

author = 'Philipp Chapkovski, chapkovski@gmail.com'

doc = """
how to show n pictures randomly
"""


class Constants(BaseConstants):
    name_in_url = 'picturerollerapp'
    players_per_group = None
    mypath = settings.STATICFILES_DIRS[0]
    photos = [f for f in listdir(join(mypath, 'picturerollerapp/photos')) if f.endswith(('.jpg'))]
    num_rounds = len(photos)


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            for p in self.session.get_participants():
                photos = Constants.photos.copy()
                random.shuffle(photos)
                p.vars['photos'] = json.dumps(photos)
        for p in self.get_players():
            p.photos = p.participant.vars['photos']


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    photos = models.CharField()
