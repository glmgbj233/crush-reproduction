GIGAHORSE_PATH = "/home/hjj/桌面/crush/gigahorse-data"
DATA_PATH = "/tmp/crush.data"

BLOCK_NUMBER = 16976770

DB_URL = "postgresql://blockchain:123@127.0.0.1:5432/mainnet"

WEB3_HOST = "wss://mainnet.infura.io/ws/v3/e00f6eaff7d9462881761e4a4ce6fd90"


from crush.web3 import connect_web3
w3 = connect_web3()
