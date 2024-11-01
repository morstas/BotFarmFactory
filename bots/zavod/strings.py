# Настройки API
API_URL_GAME_CRAFT = 'https://zavod-api.mdaowallet.com/craftGame'
API_URL_GAME_FIN = 'https://zavod-api.mdaowallet.com/craftGame/finishLevel'
URL_INIT = "https://zavod.mdaowallet.com/"
URL_PROFILE = "https://zavod-api.mdaowallet.com/user/profile"  # GET
URL_FARM = "https://zavod-api.mdaowallet.com/user/profile"  # POST
URL_CLAIM = "https://zavod-api.mdaowallet.com/user/claim"  # GET
URL_UPGRADE_TOOLKIT = 'https://zavod-api.mdaowallet.com/user/upgradeToolkit'
URL_UPGRADE_WORKBENCH = 'https://zavod-api.mdaowallet.com/user/upgradeWorkbench'
URL_BURN_TOKENS = 'https://zavod-api.mdaowallet.com/guilds/burnTokens'
URL_MISSIONS = 'https://zavod-api.mdaowallet.com/missions'
URL_CLAIM_MISSION = 'https://zavod-api.mdaowallet.com/missions/claim/'
URL_CONFIRM_LINK_MISSION = 'https://zavod-api.mdaowallet.com/missions/confirm/link/'
URL_CONFIRM_TELEGRAM_MISSION = 'https://zavod-api.mdaowallet.com/missions/confirm/telegram/'
URL_GUILD_JOIN = 'https://zavod-api.mdaowallet.com/guilds/join'
URL_WORKBENCH_SETTINGS = 'https://zavod-api.mdaowallet.com/user/workbenchSettings'
URL_TOOLKIT_SETTINGS = 'https://zavod-api.mdaowallet.com/user/toolkitSettings'

# Messages
MSG_CLAIM = 'Забрали награду'
MSG_PROFILE = 'Обновили профиль'
MSG_STATE = 'Баланс: {balance}'
MSG_TOKENS = 'Монет: {tokens}'
MSG_TOOLKIT_LEVEL = 'Уровень инструментов: {tool}'
MSG_WORKBENCH_LEVEL = 'Уровень верстака: {work}'
MSG_GUILD = 'Гильдия: {guild}'
MSG_JOINED_GUILD = 'Вступили в гильдию'
MSG_UPGRADED_TOOLKIT = 'Улучшили инструменты'
MSG_UPGRADED_WORKBENCH = 'Улучшили верстак'
MSG_BURNED_TOKENS = 'Сожгли {tokens} монет'
MSG_CLAIMED_MISSION = 'Получили {prize} за {name}'
MSG_LINK_MISSION = 'Делаем задание на {prize} за {name}'
MSG_TELEGRAM_MISSION = 'Выполняем задание {name}'
MSG_GAME_START = 'Начали играть'


HEADERS = {
  'authority': 'zavod-api.mdaowallet.com',
  'accept': 'application/json, text/plain, */*',
  'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,cy;q=0.6',
  'cache-control': 'no-cache',
  'origin': 'https://zavod.mdaowallet.com',
  'pragma': 'no-cache',
  'referer': 'https://zavod.mdaowallet.com/',
  'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
  'sec-ch-ua-mobile': '?1',
  'sec-ch-ua-platform': '"Linux"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-site',
  'user-agent': 'Mozilla/5.0 (Linux; Android 9; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Mobile Safari/537.36 Telegram-Android/11.2.3 (Samsung SM-G973N; Android 9; SDK 28; LOW)',
  'x-requested-with': 'org.telegram.messenger.web',
  'accept-encoding': 'gzip, deflate, br'
}


# Error messages
MSG_ERROR_UPGRADING_TOOLKIT = 'Ошибка обновления инструментов: {error}'
MSG_ERROR_UPGRADING_WORKBENCH = 'Ошибка обновления верстака: {error}'
MSG_ERROR_BURNING_TOKENS = 'Ошибка сжигания монет: {error}'
MSG_ERROR_FETCHING_MISSIONS = 'Ошибка получения заданий: {error}'
MSG_ERROR_CLAIMING_MISSION = 'Ошибка получения задания {id}: {error}'
MSG_ERROR_CONFIRMING_LINK_MISSION = 'Ошибка подтверждения задания {id}: {error}'
MSG_ERROR_CONFIRMING_TELEGRAM_MISSION = 'Ошибка подтверждения задания {id}: {error}'

# Сообщения о включении/отключении
MSG_GAME_DISABLED = "Игра отключена."
MSG_UPGRADES_DISABLED = "Прокачка отключена."
MSG_TOOLKIT_UPGRADES_DISABLED = "Прокачка инструментов отключена."
MSG_WORKBENCH_UPGRADES_DISABLED = "Прокачка верстака отключена."
MSG_GUILD_JOIN_DISABLED = "Вступление в гильдию отключено."

