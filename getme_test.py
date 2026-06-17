import asyncio
import os
import TelethonFakeTLS
from telethon import TelegramClient
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.environ['API_ID'])
API_HASH = os.environ['API_HASH']

# Telegram servers are blocked directly on this network, so route via a
# fake-TLS ("ee") MTProto proxy. Stock telethon can't speak fake-TLS, so we
# use TelethonFakeTLS (pip install TelethonFakeTLS).
#
# Secret rules (per TelethonFakeTLS): hex secret -> strip leading "ee";
# base64 secret -> strip leading "7".
SERVER = 'abrafagh.cdn.finecooking.info'
PORT = 443
SECRET_EE = 'eef0eeb0bd9adc4fd4a93994ee3b2a216b63646e2e79656b74616e65742e636f6d'
PROXY = (SERVER, PORT, SECRET_EE[2:])  # strip the "ee" prefix


async def main():
    """Minimal connectivity check: connect to Telegram and call get_me()."""
    client = TelegramClient(
        'telethon_session', API_ID, API_HASH,
        connection=TelethonFakeTLS.ConnectionTcpMTProxyFakeTLS,
        proxy=PROXY, timeout=20, connection_retries=2,
    )
    async with client:
        me = await client.get_me()
        print("Connected OK")
        print(f"id:       {me.id}")
        print(f"name:     {me.first_name} {me.last_name or ''}".strip())
        print(f"username: @{me.username}" if me.username else "username: (none)")


if __name__ == "__main__":
    asyncio.run(main())
