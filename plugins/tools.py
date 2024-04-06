async def is_user_on_chat(client, chat_id: int, user_id: int) -> bool:
 
    try:
        chat_member = await client.get_chat_member(chat_id, user_id)
        return True if chat_member else False
    except:
        return False
