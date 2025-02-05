from __future__ import annotations

from typing import TYPE_CHECKING
from typing import Union

from ..objects.message.embed import Embed
from ..objects.message.file import File
from ..objects.message.message import Message
from ..objects.app.interaction_flags import InteractionFlags

PILLOW_IMPORT = True

try:
    from PIL.Image import Image
except (ModuleNotFoundError, ImportError):
    PILLOW_IMPORT = False

if TYPE_CHECKING:
    from pincer import Client


def convert_message(
        client: Client,
        message: Union[Embed, Message, str]
) -> Message:
    """Converts a message to a Message object"""
    if isinstance(message, Embed):
        message = Message(embeds=[message])
    elif PILLOW_IMPORT and isinstance(message, (File, Image)):
        message = Message(attachments=[message])
    elif not isinstance(message, Message):
        message = Message(message) if message else Message(
            client.received_message,
            flags=InteractionFlags.EPHEMERAL
        )
    return message
