# BotFarmFactory
Небольшой "фрейемворк" для создания ферм по прокачке телеграм "тапалок"

## Использование
Примерынй алгоритм действий:
1. В `config.py` находится конфигурация клиента Telegram, ее желательно не трогать. Так же есть флаг DEBUG. (при значении True будет писать диагностическую информацию в файл debug.log)
1. Отредактировать `config.py`:

| Параметр | Описание |
| - | - |
| `ACCOUNTS_DIR` | Дефолтное имя каталога, где будут храниться сессии телеграм. |
| `TELEGRAM_AUTH` | Не трогать, если не понимаете что делаете. Это кредсы для работы бота с телеграм аккаунтами. |
| `DEBUG` | Включение записи диагностической информации в `debug.log` |
| `RETRY_ATTEMPTS` | Количество ретраев при запросах |
| `ENABLED_BOTS` | Список включенных ботов. Пустой список - все боты |включены. Если добавить хоть один бот - работать будет только он. |
| `DISABLED_BOTS` | Список выключенных ботов. Все боты что в списке будут выключены. |
| `SLEEP_AT_NIGHT` | Атрибут указывает, стоит ли боту фармить ночью |
| `NIGHT_HOURS` | Ночные часы (с какого часа и по какой) бот "спит" |
| `MULTITHREAD` | Многопоточность. В боте реализована небольшая многопоточность. При включении боты для каждого аккаунта телеграм будут фармиться в отдельных потоках. То есть аккаунты будут фармиться не один за другим, а параллельно. |

**ВАЖНО: Многопоточность стоит включать после того, как будут созданы сессии для аккаунтов**

2. Заполнить файл `accounts.py` (`accounts_local.py`) здесь нужен номер телефона на котором висит телеграм аккаунт и прокси, через который будут ходить все тапалки на этом аккаунте.
3. Устновить python 3 (если вдруг не установлен, инструкции есть в интернете)
4. Установить зависимости выполнив команду в терминале `pip install -r requirements.txt` (если перекачали скрипт, стоит каждый раз это выполнять. может измениться набор пакетов)
5. Запустить фарминг `python3 factory.py`

После запуска, бот аутентифицируется в учетках телеграма и под каждой учеткой получает токены и прочие кредсы для доступа к ботам, с которыми бот умеет работать.


## Для разработчиков
Было бы неплохо если бы разработчики брались за написание модулей для фабрики и помогали [комьюнити](https://t.me/cryptoautofarm) расти. 
Методы, атрибуты и подходы, которые помогут в написании модулей. [Руководство будет здесь](bots/base/DEV_GUIDE.md)

В данный момент реализованы боты:

- [cellcoin_bot](https://t.me/cellcoin_bot?start=102796269)
- [simple_tap_bot](https://t.me/Simple_Tap_Bot?start=1718085881160)
- [blum](https://t.me/BlumCryptoBot/app?startapp=ref_ItXoLRFElL)
- [iceberg](https://t.me/IcebergAppBot?start=referral_102796269)
- [MDAO Wallet (ZAVOD)](https://t.me/Mdaowalletbot?start=102796269)
- [anon](https://t.me/AnonEarnBot) (Если не регается, ищем рефки в интернете)
- [hamster kombat](https://t.me/Hamster_kombat_bot/start?startapp=kentId102796269)
- [timeton](https://t.me/TimeTONbot?start=TotalAwesome)
- [Solstone](https://t.me/solstonebot?start=102796269)

### Комьюнити модули:

- [TapCoinsBot](https://t.me/tapcoinsbot/app?startapp=ref_QjG2zG)
- [HEXN](https://t.me/hexn_bot/app?startapp=63b093b0-fcb8-41b5-8f50-bc61983ef4e3)
- [AltOOshka](https://t.me/altooshka_bot?start=z6HfRqEhax4)


Боты начнут последовательно (или параллельно) фармить на каждом аккаунте

Если все выполнено правильно, вы увидите примерно следующую картину:
![example](https://github.com/user-attachments/assets/f907a5e6-7b5f-4a62-aff4-7aa3144fefeb)

Ответы почти на все вопросы уже есть в канале или в чате и в закрепе: https://t.me/cryptoearnfactory

### Донаты приветствуются: 

USDT TRC20: `TAijXFWvcAjeVQQCZGsiZ1z9CbbXojGLob`

![Tron](https://github.com/user-attachments/assets/2a332718-8465-4415-8333-16f1c379f5fa)

TON, USDT TON: `UQBcSKPEA0N6wjbux7UqiLcG8aLFx-Mxi7jF0bP4nizcHuA9`, `EQBcSKPEA0N6wjbux7UqiLcG8aLFx-Mxi7jF0bP4nizcHr34`
![TON](https://github.com/user-attachments/assets/0f313ba0-be4e-4ed1-9e95-3f46926cc374)
