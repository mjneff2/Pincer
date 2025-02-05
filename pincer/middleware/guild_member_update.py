# Copyright Pincer 2021-Present
# Full MIT License can be found in `LICENSE` at the project root.

"""
Sent when a guild member is updated. This will also fire when the user object
of a guild member changes.
"""

from ..core.dispatch import GatewayDispatch
from ..utils import Coro
from ..utils.conversion import construct_client_dict
from ..objects.events.guild import GuildMemberUpdateEvent


async def guild_member_update_middleware(self, payload: GatewayDispatch):
    """|coro|

    Middleware for ``on_guild_member_update`` event.

    Parameters
    ----------
    self : :class:`Client`
        The current client/bot.

    payload : :class:`GatewayDispatch`
        The data received from the guild member update event.
    """

    return (
        "on_guild_member_update",
        [GuildMemberUpdateEvent.from_dict(
            construct_client_dict(self, payload.data)
        )]
    )


def export() -> Coro:
    return guild_member_update_middleware
