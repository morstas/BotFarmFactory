import json
import random
import requests
from time import sleep, time as current_time

from bots.base.utils import to_localtz_timestamp, api_response
from bots.base.base import BaseFarmer, time
from .strings import *
from .configs import *



class BotFarmer(BaseFarmer):
    name = BOT_NAME
    extra_code = EXTRA_CODE
    info = dict(profile={}, farming={})
    initialization_data = dict(peer=name, bot=name, url=URL_INIT)
    payload_base = {}
    codes_to_refresh = (400,)
    refreshable_token = True

    def set_headers(self, *args, **kwargs):
        self.headers = HEADERS.copy()
        self.get = api_response(super().get)
        self.post = api_response(super().post)
        self.delete = api_response(super().delete)

    def authenticate(self, *args, **kwargs):
        auth_data = self.initiator.get_auth_data(**self.initialization_data)['authData']
        self.headers['telegram-init-data'] = auth_data

    def refresh_token(self):
        self.initiator.connect()
        self.authenticate()
        self.initiator.disconnect()

    def set_start_time(self):
        self.start_time = time() + random.uniform(MIN_WAIT_TIME, MAX_WAIT_TIME)

    def update_profile(self):
        if result := self.get(URL_PROFILE):
            self.info['profile'] = result
            self.log(MSG_PROFILE)

    def update_farming(self):
        if result := self.get(URL_FARM):
            self.info['farming'] = result

    @property
    def claim_date(self):
        last_claim = to_localtz_timestamp(self.info['farming'].get('lastClaim'))
        next_claim = last_claim + self.info['farming'].get('claimInterval') / 1000
        return next_claim

    def claim(self):
        if time() >= self.claim_date:
            if result := self.post(URL_CLAIM, return_codes=(500,)):
                self.info['profile'] = result
                self.log(MSG_CLAIM)

    def up(self):
        if not ENABLE_UP:
            self.log('Прокачка выключена')
            return

        guild = self.info['profile']['guildId']
        self.ide = self.get(URL_FARM)
        tokens = round(self.info['profile']['tokens'])
        self.log(MSG_TOKENS.format(tokens=tokens))
        tool = self.ide['toolkitLevel']
        self.log(MSG_TOOLKIT_LEVEL.format(tool=tool))
        work = self.ide['workbenchLevel']
        self.log(MSG_WORKBENCH_LEVEL.format(work=work))
        self.log(MSG_GUILD.format(guild=guild))
        if guild is None and ENABLE_GUILD_JOIN:
            self.post(URL_GUILD_JOIN, json={'guildId': GUILD_ID, })
            self.log(MSG_JOINED_GUILD)

        if ENABLE_UPGRADES:
            if ENABLE_TOOLKIT_UPGRADE:
                self.upgrade_tool(tool, tokens)
            if ENABLE_WORKBENCH_UPGRADE:
                self.upgrade_workbench(work, tokens)

        if tool == TOOLKIT_LEVEL_BURN and work == WORKBENCH_LEVEL_BURN:
            self.burn(tokens)


    def upgrade_tool(self, tool, tokens):
        if not ENABLE_UPGRADES or not ENABLE_TOOLKIT_UPGRADE:
            self.log(MSG_TOOLKIT_UPGRADES_DISABLED)
            return
        tool += 1
        toolkit_settings = self.get(URL_TOOLKIT_SETTINGS)
        cost = {item['level']: item['price'] for item in toolkit_settings}
        if tokens >= cost.get(tool, float('inf')) and tool < 5:
            try:
                self.post(URL_UPGRADE_TOOLKIT)
                self.log(MSG_UPGRADED_TOOLKIT)
                sleep(SLEEP_TIME_UPGRADE)

                self.info['profile']['tokens'] = tokens - cost.get(tool, 0)
            except Exception as e:
                self.log(MSG_ERROR_UPGRADING_TOOLKIT.format(error=e))

    def upgrade_workbench(self, work, tokens):
        if not ENABLE_UPGRADES or not ENABLE_WORKBENCH_UPGRADE:
            self.log(MSG_WORKBENCH_UPGRADES_DISABLED)
            return
        work += 1
        workbench_settings = self.get(URL_WORKBENCH_SETTINGS)
        cost = {item['level']: item['price'] for item in workbench_settings}
        if tokens >= cost.get(work, float('inf')) and work < 49:
            try:
                self.post(URL_UPGRADE_WORKBENCH)
                self.log(MSG_UPGRADED_WORKBENCH)
                sleep(SLEEP_TIME_UPGRADE)

                self.info['profile']['tokens'] = tokens - cost.get(work, 0)
            except Exception as e:
                self.log(MSG_ERROR_UPGRADING_WORKBENCH.format(error=e))

    def burn(self, tokens):
        try:
            self.post(URL_BURN_TOKENS, json={"amount": tokens})
            self.log(MSG_BURNED_TOKENS.format(tokens=tokens))
        except Exception as e:
            self.log(MSG_ERROR_BURNING_TOKENS.format(error=e))

    def process_missions(self):
        if not ENABLE_TASK:
            self.log('Выполнение миссий выключено')
            return

        try:
            task = self.get(URL_MISSIONS, params={
                                'offset': '0',
                                'status': 'ACTIVE',
                            })
            for q in task['missions']:
                id = q['id']
                state = q['state']
                type = q['type']
                if state == 'READY_TO_CLAIM':
                    try:
                        self.taskclaim(id)
                    except Exception as e:
                        self.log(MSG_ERROR_CLAIMING_MISSION.format(id=id, error=e))
                if state == "STARTED" and type == "LINK":
                    try:
                        self.link(id)
                    except Exception as e:
                        self.log(MSG_ERROR_CONFIRMING_LINK_MISSION.format(id=id, error=e))
                if state == "STARTED" and type == "TELEGRAM_CHANNEL":
                    try:
                        self.telegram(id)
                    except Exception as e:
                        self.log(MSG_ERROR_CONFIRMING_TELEGRAM_MISSION.format(id=id, error=e))

        except Exception as e:
            self.log(MSG_ERROR_FETCHING_MISSIONS.format(error=e))

    def taskclaim(self, id):
        sleep(SLEEP_TIME_CLAIM)
        try:
            response = self.post(f'{URL_CLAIM_MISSION}{id}', return_codes=(403,))
            self.log(MSG_CLAIMED_MISSION.format(prize=response['prize'], name=response['name']['ru']))
        except Exception as e:
            self.log(MSG_ERROR_CLAIMING_MISSION.format(id=id, error=e))

    def link(self, id):
        sleep(SLEEP_TIME_CLAIM)
        try:
            response = self.post(f'{URL_CONFIRM_LINK_MISSION}{id}')

            self.log(MSG_LINK_MISSION.format(prize=response['prize'], name=response['name']['ru']))
        except Exception as e:
            self.log(MSG_ERROR_CONFIRMING_LINK_MISSION.format(id=id, error=e))

    def telegram(self, id):
        sleep(SLEEP_TIME_CLAIM)
        try:
            response = self.post(f'{URL_CONFIRM_TELEGRAM_MISSION}{id}')

            self.log(MSG_TELEGRAM_MISSION.format(name=response['name']['ru']))
        except Exception as e:
            self.log(MSG_ERROR_CONFIRMING_TELEGRAM_MISSION.format(id=id, error=e))

    def game_init(self):
        if not ENABLE_GAME:
            self.log(MSG_GAME_DISABLED)
            return

        response = requests.get(API_URL_GAME_CRAFT, headers=self.headers)
        if response.status_code == 200:
            sleep(2)
            self.game()

    def game(self):
        self.log(MSG_GAME_START)
        numbers = random.sample(range(20), 3)
        a, b, c = numbers
        json_data = {
            'selectedSells': [
                a,
                b,
                c,
            ],
            'action': 'SAVE',
        }

        response = requests.post(
            API_URL_GAME_FIN,
            headers=self.headers,
            json=json_data
        )
        if response.status_code != 200:
            test = response.json()
            print(json.dumps(test, indent=4))

        if response.status_code == 200:
            game_data = response.json()
            if game_data['level'] > 0:
                self.log(f"Выиграли lvl: {game_data['level']}")
                sleep(3)
                self.game()
            elif game_data['level'] == 0:
                self.log('Ты проиграл')
        elif response.status_code == 403:
            self.log('Рано еще играть')

        elif response.status_code != 200:
            print(json.dumps(response, indent=4))


    def farm(self):
        self.update_profile()
        self.update_farming()
        sleep(1)
        self.process_missions()
        self.claim()
        sleep(1)
        self.update_farming()
        sleep(2)
        self.up()
        sleep(1)
        self.game_init()
