from telethon import TelegramClient, events, Button
import requests
#from headers import headers
#import urls
import os
import requests
import cryptg
import asyncio
import shutil
import subprocess
from mega import Mega
mega = Mega()
m = mega.login()
#from flask import request

client = TelegramClient('anfghohn',1416135,"2aae0d7ca32b01970b2c6770a4c0cf8e").start(bot_token="1609758550:AAEvT8Go8IjPMjz2yr8krUzqqdER8QBghGs")

@client.on(events.NewMessage(pattern='/diskusage'))
async def handler(event):
    chat = await event.get_chat()
    stat = shutil.disk_usage("/app/templates/download")
    await client.send_message(chat,str(stat))
        
@client.on(events.NewMessage(pattern="/url"))
async def handler(event):
    link =event.text.split(' ')[1]
    l =event.text.split(' ')[2]
    chat = await event.get_chat()
    
    s = f"http://pdisk.net/api/ndisk_manager/video/create?link_type=link&content_src={link}&source=2000&uid=83773722&title={l}&description=telegram"
    r = requests.get(s).json()
    z=r['data']["item_id"]
   # await event.delete()
   # client.delete_messages()
    markup  = client.build_reply_markup(Button.url("📀 PDisk 📀",f"http://m.pdisk.net/share-video?videoid={z}"))
    await client.send_message(chat, "link will working depends on size it takes half or more ... ", buttons=markup)
            
            #rgx = w
@client.on(events.NewMessage(pattern='/magnet'))
async def handler(event):
    link =event.text.split(' ')[1]
    l =link.split('/')[-1]
    chat = await event.get_chat()
    
    s = f"http://pdisk.net/api/ndisk_manager/video/create?link_type=magnet&content_src={link}&source=2000&uid=83773722&title={l}&description=telegram"
    r = requests.get(s).json()
    z=r['data']["item_id"]
   # await event.delete()
   # client.delete_messages()
    markup  = client.build_reply_markup(Button.url("📀 PDisk 📀",f"http://m.pdisk.net/share-video?videoid={z}"))
    await client.send_message(chat, "link will working depends on size it takes half or more ... ", buttons=markup)
            
@client.on(events.NewMessage(pattern='/telepdisk'))
async def handler(event):
   # 
    chat = await event.get_chat()
    print(chat)
    dw = await event.get_reply_message()
    links =event.text.split(" ")[1]
    await client.send_message(chat,"🌠 downloading 🌠")
    ss=await dw.download_media(links)
    shutil.move(f"/app/{links}",f"/app/templates/download/{links}")
    await client.send_message(chat,f"wait few minutes ...{links}")

    link =f"https://asulinkgen.herokuapp.com/files/{links}"
    l =link.split('/')[-1]
    s = f"http://pdisk.net/api/ndisk_manager/video/create?link_type=link&content_src={link}&source=2000&uid=83773722&title={l}&description=telegram"
    r = requests.get(s).json()
    z=r['data']["item_id"]
   # await event.delete()
   # client.delete_messages()
    markup  = client.build_reply_markup(Button.url("📀 PDisk 📀",f"http://m.pdisk.net/share-video?videoid={z}"))
    await client.send_message(chat, "link will working depends on size it takes half or more ... ", buttons=markup)
    #os.remove(f"/app/templates/download/{links}")        
@client.on(events.NewMessage(pattern='(?i)/ls'))

async def handler(event):

    chat = await event.get_chat()

    link =event.text.split(" ")[1]

    c = subprocess.getoutput(f"pip install {link}")
    print (c)
    await client.send_message(chat,"finish")
@client.on(events.NewMessage(pattern='(?i)/upload'))
async def handler(event):
    chat = await event.get_chat()
    print(chat)
    dw = await event.get_reply_message()
    links =event.text.split(" ")[1]
    await client.send_message(chat,"🌠 downloading 🌠")
    ss=await dw.download_media(links)
    shutil.move(f"/app/{links}",f"/app/templates/download/{links}")
    await client.send_message(chat,f"https://asulinkgen.herokuapp.com/files/{links}")

        

      #  os.rename(ss,links)

        

    if os.path.exists(f"/app/Download/{chat.username}"):
        await client.send_message(chat,"downloading")
        ss=await dw.download_media()
        await client.send_message(chat,f"https://asulinkgen.herokuapp.com/u?url={ss}")
  
@client.on(events.NewMessage(pattern='(?i)/del'))

async def handler(event):

    chat = await event.get_chat()

    

    print(chat.username)

    

    #dw = await event.get_reply_message()

  #  shutil.rmtree("./Downloads/")
  #  os.mkdir("./Downloads")
   # await client.send_message(chat,"ss")
@client.on(events.NewMessage(pattern='/torrent'))
async def handler(event):
    link =event.text.split(' ')[1]
    l =link.split('/')[-1]
    chat = await event.get_chat()
    s = f"http://pdisk.net/api/ndisk_manager/video/create?link_type=magnet&content_src={link}&source=2000&uid=83773722&title={l}&description=telegram"
    r = requests.get(s).json()
    z=r['data']["item_id"]
    await event.delete()
   # client.delete_messages()
    markup  = client.build_reply_markup(Button.url(" 🔥 torrent🔥",f"https://asulinkgen.herokuapp.com/e?url={z}"))
    await client.send_message(chat, "link only after one hour dead torrent not working .....", buttons=markup)
            
            #rgx = w
    


client.start()
client.run_until_disconnected()
