from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.types import InputPeerEmpty
from tqdm import tqdm

api_id = change       # Your API ID
api_hash = 'change'  # Your API HASH


def download_media(group, cl, name):
    messages = cl.get_messages(group, limit=2000)

    for message in tqdm(messages):
        message.download_media('./' + name + '/')


with TelegramClient('change', api_id, api_hash) as client:
    result = client(GetDialogsRequest(
        offset_date=None,
        offset_id=0,
        offset_peer=InputPeerEmpty(),
        limit=500,
        hash=0,
    ))

    title = 'change'         # Title for channel
    channel = client(GetFullChannelRequest(title))
    print(channel.full_chat)

    download_media(channel.full_chat, client, title)