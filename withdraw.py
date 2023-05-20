from zksync2.transaction.transaction_builders import TxWithdraw
from config import *

web3 = ZkSyncBuilder.build(ZKSYNC_URL)
eth_web3 = Web3(Web3.HTTPProvider(ETH_URL))


def withdrawal(privatekey):
    try:

        account: LocalAccount = from_key(private_key=privatekey)

        amount = web3.zksync.get_balance(account.address, EthBlockParams.LATEST.value)

        eth_balance = eth_web3.eth.get_balance(account.address)
        logger.info(f"Eth: balance: {Web3.from_wei(eth_balance, 'ether')}")

        withdrawal = TxWithdraw(web3=web3,
                                token=Token.create_eth(),
                                amount=Web3.to_wei(amount, "ether"),
                                gas_limit=0,  # unknown
                                account=account)
        estimated_gas = web3.zksync.eth_estimate_gas(withdrawal.tx)
        tx = withdrawal.estimated_gas(estimated_gas)
        signed = account.sign_transaction(tx)
        tx_hash = web3.zksync.send_raw_transaction(signed.rawTransaction)
        logger.info(f"ZkSync Tx: https://explorer.zksync.io/tx/{web3.to_hex(tx_hash)}")
        list_send.append(f'{STR_DONE}zkSync Era withdrawal | {account.address}')

    except Exception as error:
        logger.error(f'Withdrawal ETH from ZkSync Era| {error}')
        list_send.append(f'{STR_CANCEL}zkSync Era withdrawal | {account.address}')


if __name__ == "__main__":

    with open("private_keys.txt", "r") as f:
        keys_list = [row.strip() for row in f]

    random.shuffle(keys_list)

    for privatekey in keys_list:
        cprint(f'\n=============== start : {privatekey} ===============', 'yellow')
        withdrawal(privatekey)
        sleep = random.randint(SLEEP_TIME_MIN, SLEEP_TIME_MAX)
        sleeping(sleep, sleep)

    if TG_BOT_SEND == True:
        send_msg()