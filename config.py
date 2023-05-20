from eth_account import Account
from eth_account.signers.local import LocalAccount
from web3 import Web3
from web3_auto.from_key import from_key
from zksync2.core.types import Token, EthBlockParams
from zksync2.module.module_builder import ZkSyncBuilder
from zksync2.manage_contracts.zksync_contract import ZkSyncContract
from zksync2.provider.eth_provider import EthereumProvider

from termcolor import cprint
import time
import random
from tqdm import tqdm
from loguru import logger
import telebot

# PRC providers
ZKSYNC_URL = "https://mainnet.era.zksync.io"
ETH_URL = "https://rpc.ankr.com/eth"

# Amount of ETH to send, the value will randomly choose between MIN_AMOUNT and MAX_AMOUNT.
MIN_AMOUNT = 0.001
MAX_AMOUNT = 0.003

# The GWEI value at which the transaction will take place, otherwise it will wait.
# If the value is empty, the current GWEI of the network will be used
GWEI = 21

# Script execution pause between wallets (randomly between SLEEP_TIME_MIN and SLEEP_TIME_MAX)
SLEEP_TIME_MIN = 100
SLEEP_TIME_MAX = 300

# Setting up the results to be sent to the bot's tg
TG_BOT_SEND = False # True / False. If True, then it will send the results in Telegram
TG_TOKEN = '' # Telegram bot token
TG_ID = 000000000 # Your Telegram user ID (https://t.me/getmyid_bot)

STR_DONE = '✅ '
STR_CANCEL = '❌ '

list_send = []
def send_msg():

    try:
        str_send = '\n'.join(list_send)
        bot = telebot.TeleBot(TG_TOKEN)
        bot.send_message(TG_ID, str_send, parse_mode='html')

    except Exception as error:
        logger.error(error)

def sleeping(from_sleep, to_sleep):

    x = random.randint(from_sleep, to_sleep)
    for i in tqdm(range(x), desc='sleep ', bar_format='{desc}: {n_fmt}/{total_fmt}'):
        time.sleep(1)