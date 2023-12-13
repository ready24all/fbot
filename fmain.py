import asyncio
import logging
import sys
from create_bot import bot, dp
from handlers import command_start_handler, message_get_rate, delete_all_messages, message_handler_info
# , message_handler_command_kb, callback_query_picture, message_handler_inline_kb, message_get_rate, message_remove_kb, message_handler_mersi






async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    logging.info("bot was initialized")
    # And the run events dispatching
    await dp.start_polling(bot)



if __name__ == "__main__":
    # logging.basicConfig(filename='logs.log', level=logging.DEBUG,
    #         format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    logging.basicConfig(level=logging.INFO, stream=sys.stdout,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    asyncio.run(main())