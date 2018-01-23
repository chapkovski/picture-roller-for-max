from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import json


class MyPage(Page):
    def vars_for_template(self):
        return {'cur_photo': 'picturerollerapp/photos/{}'.format(
            json.loads(self.participant.vars['photos'])[self.round_number - 1])}


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [
    MyPage,
]
