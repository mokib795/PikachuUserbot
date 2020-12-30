#!/usr/bin/env python3
#
# Copyright (C) 2020 by ItzSjDude@Github, < https://github.com/ItzSjDude/PikachuUserbot >.
#
# This file is part of < https://github.com/ItzSjDude/PikachuUserbot > project,
# and is released under the "GNU v3.0 License Agreement".
# 
# Please see < https://github.com/ItzSjDude/PikachuUserbot/blob/master/LICENSE >
#
# All rights reserved 

#!/usr/bin/env python3
#

from Asst_modules import *

@tgbot.on(Pika_CallBack(data=re.compile(rb"pika1\((.+?)\)")))
async def _(_pika):
  pikacmds = tgbot.PikaAsst
  c_p_n = int(pika_.data_match.group(1).decode("UTF-8"))
  buttons = assistent_help(c_p_n + 1, pikacmds, "helpme")
  await pika_.edit(buttons=buttons)

@tgbot.on(Pika_CallBack(data=re.compile(rb"pika2\((.+?)\)")))
async def _(pika_):
    pikacmds = tgbot.PikaAsst
    c_p_n = int(pika_.data_match.group(1).decode("UTF-8"))
    buttons = assistent_help(c_p_n - 1, pikacmds, "helpme")  # pylint:disable=E0602
    await pika_.edit(buttons=buttons)

@tgbot.on(Pika_CallBack(data=re.compile(b"pika3")))
async def _(pika_):
    await pika_.edit("Pika Pi! Restarting wait for 1 Min!")
    await asyncio.sleep(4)
    await pika_.delete()
    pika_start()

@tgbot.on(Pika_CallBack(data=re.compile(b"pika4")))
async def _(pika_):
    _a_ = await pika_.edit("Pika Pi! Menu Closed!")
    await asyncio.sleep(3)
    await _a_.delete()

@tgbot.on(Pika_CallBack(data=re.compile(b"pika5(.*)")))
async def _(pika_):
    a = randint(0, 9)
    _rx_ = f"{_emo_[a]}" + f" {rx}"
    _pikacmds = tgbot.PikaAsst
    _pika_ = pika_.data_match.group(1).decode("UTF-8")
    _pika = _pikacmds[_pika_].__doc__.format(i=_rx_)
    _pikaB = [(custom.Button.inline("⫷BacK", data="pika6"))]
    await pika_.edit(_pika, buttons=_pikaB)

@tgbot.on(Pika_CallBack(data=re.compile(b"pika6(.*)")))
async def _(pika_):
    _pika = f"""Pïkå¢hµ Úsêrßð† {helpstr}"""
    _pikacmds = tgbot.PikaAsst
    _pika += "\n**Currently Loaded Plugins**: {}".format(len(_pikacmds))
    _pika_ = assistent_help(0, _pikacmds, "helpme")
    await pika_.edit(_pika, buttons=_pika_, link_preview=False)

