from dotenv import load_dotenv
from telethon.sync import TelegramClient, events
import os
import json
import asyncio

# async def getListOfGroups(client):
#     try:
#         dialogs = await client.get_dialogs()
#         groups_info = []
#         for dialog in dialogs:
#             if dialog.is_group or dialog.is_channel:  # Filtra los grupos y canales
#                 group_info = {'group_id': dialog.id, 'group_name': dialog.title}
#                 groups_info.append(group_info)
#                 # Imprimir el nombre y el ID del grupo
#                 print(f"Grupo: {dialog.title}, ID: {dialog.id}")
#         return groups_info
#     except Exception as e:
#         print(f"Error: {e}")
#         return []


async def getListOfGroups(client):
    try:
        dialogs = await client.get_dialogs()
        groups_info = []
        for dialog in dialogs:
            if dialog.is_group or dialog.is_channel:
                entity = await client.get_entity(dialog.id)
                can_send_messages = entity.default_banned_rights is None or not entity.default_banned_rights.send_messages
                if can_send_messages:
                    group_info = {'group_id': dialog.id, 'group_name': dialog.title}
                    groups_info.append(group_info)

        return groups_info
    except Exception as e:
        print(e)
        return []
async def getMessagesFromGroup(client, group_id):
    try:
        all_messages = []
        async for message in client.iter_messages(group_id):
            try:
                all_messages.append(message)
            except:
                pass
        return all_messages
    except Exception as e:
        print(e)
        return []
async def logUserBot():
    load_dotenv()
    api_id = int(22885409)
    api_hash = "231dee303ac43b0ce0b0906de77ca5df"
    phone_number = "51933134824"
    session_name = "bot_spammer"
    client = TelegramClient(session_name, api_id, api_hash)
    await client.connect()
    if not await client.is_user_authorized():
        await client.send_code_request(phone_number)
        await client.sign_in(phone_number, input('Ingrese el código de verificación: '))
    await client.send_message("@spmtenz2", f'<b>Bot encendido</b>', parse_mode="HTML")
    spammer_group = int("-4532673979")
    excluded_groups = [-1002171101200,-1001926519077,-1001907073788,-1001918809414,-1002224408369,-1002095862989,-1001586028282,-1001829996546,-1002112968455,-1002001880141,-4527438300,-4532673979,-1002304840729,-1002291580489]

    while True:
        groups_info = await getListOfGroups(client)
        messages_list = await getMessagesFromGroup(client, spammer_group)
            
        try:
            await client.send_message("@spmtenz2", f"<b>CANTIDAD DE MENSAJES CONSEGUIDOS PARA PUBLICAR</b> <code>{len(messages_list)-1}</code>",parse_mode="HTML")
        except:
            pass
            
        try:
            for i in groups_info:
                if i['group_name'] not in ["Spam 2024","Spam","RESPALDO🇵🇪BINS PERU","➳𝒀𝑨𝑷𝑬 𝑫𝑬 𝑬𝑺𝑻𝑨𝑭𝑨𝑫𝑶𝑹𝑬𝑺 ✧","QUEMANDO ESTAFADORES","𝐏𝐄𝐑Ú 𝐀𝐘𝐔𝐃𝐀","Referencias Elmer 💸","🎭 CANAL MUNDO STREAMING PERÚ 🇵🇪","TU MARKETPLACE"] and i['group_id'] not in excluded_groups:
                    j=0
                    for message_spam in messages_list:
                        j+=1
                        resultado = True
                        try:
                            await client.forward_messages(i["group_id"], message_spam)
                        except Exception as error:
                            await client.send_message("@spmtenz2", f'<b>Error enviando mensajes a {i["group_id"]}</b> - <code>{i["group_name"]}<code>\nCausa:{error}',parse_mode="HTML")
                            resultado = False
                        if resultado:
                            await client.send_message("@spmtenz2", f'<b>Mensaje enviado a {i["group_id"]}</b> - <code>{i["group_name"]}</code>',parse_mode="HTML")  
                        await asyncio.sleep(10)
                        if j==2: break
            await client.send_message("@spmtenz2", f'<b>RONDA ACABADA</b>', parse_mode="HTML")
            await asyncio.sleep(100) 
        except:
            pass
    
            
if __name__ == "__main__":
    asyncio.run(logUserBot())
