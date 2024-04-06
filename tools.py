async def is_user_on_chat(bot: TelegramClient, chat_id: int, user_id: int) -> bool:
    try:
        check = await bot.get_permissions(chat_id, user_id)
        return check
    except:
        return False
