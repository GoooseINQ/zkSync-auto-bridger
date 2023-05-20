# zkSyncAutoBridger

Python script bridges ETH from Mainnet to zkSync Era and back (https://portal.zksync.io/bridge).

## Configuring config.py and accounts data :

- In the file private_keys.txt write private wallet keys line by line.
- In file config.py we change values of variables for ourselves (more details in the file itself).

## How to run
Install necessary dependencies.

    pip install -r requirements.txt

The command sends ETH from Mainnet to the zkSync Era network.

    python deposit.py

The command sends ETH from the zkSync Era network back to the Mainnet network.

    python withdraw.py


