from typing import Text
from linebot.models import TextSendMessage
from models.message_request import MessageRequest
from skills import add_skill


@add_skill('{text}')
def get(message_request: MessageRequest):
    msg = TextSendMessage(text='Hello')

    txt = '$ LINE emoji $ $'

    emoji = [
        {
            "index": 0,
            "productId": "5ac1bfd5040ab15980c9b435",
            "emojiId": "001"
        },
        {
            "index": 13,
            "productId": "5ac1bfd5040ab15980c9b435",
            "emojiId": "002"
        },
        {
            "index": 15,
            "productId": "5ac21e6c040ab15980c9b444",
            "emojiId": "004"
        }
    ]

    print(txt.find('$', 2))

    # emoji_message = TextSendMessage(text='$ LINE emoji $', emojis=emoji)
    return [
        TextSendMessage(text=txt, emojis=emoji)
    ]
