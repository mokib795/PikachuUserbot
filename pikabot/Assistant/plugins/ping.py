__pika__="""
{i}pika
**Usage**: Checks Ping Speed"""

# Made by @ItzSjDude for Pikabot
from Asst_modules import _ping


@ItzSjDude(pika=True, pattern="pika$")
async def _(event):
    await _ping(event)
