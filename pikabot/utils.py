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

import os 
from functools import wraps
import re
import time 
import logging
import inspect
import math
import subprocess
import sys
import traceback
import datetime
import asyncio
from pikabot import *  
from telethon import *
from var import Var
from var import Client as clIent
from pathlib import Path
from telethon.tl.types import InputMessagesFilterDocument , PeerChannel 
import traceback
import pikabot.sql_helper 
import pikabot.main_plugs.SysRuntime 
import pikabot.main_plugs.plug
from traceback import format_exc
from time import gmtime, strftime
from asyncio import create_subprocess_shell as asyncsubshell, subprocess as asyncsub
from os import remove
from traceback import format_exc
from typing import List
from pikabot import *
from sys import *
from var import Var
from pathlib import Path
from telethon import TelegramClient, functions, types
from telethon.tl.types import InputMessagesFilterDocument
import asyncio, time, io, math, os, logging, asyncio, shutil, re
import sys, json, os

TGBOT_USERS = set(int(x) for x in os.environ.get("BOT_USERS", "779890498").split())
from importlib.util import *
#©ItzSjDude </Kang/Copy with Credits else u will be called ultra gey/>
def pikatgbot(pika=None, silent=None):
    def decorator(func):
        @wraps(func)
        async def wrapper(event):
            _selfpika = await tgbot.get_me()
            if "AdmOnly" in pika:
                _pika = await tgbot.get_permissions(event.chat_id, event.sender_id)
                if _pika.is_admin:
                    await func(event)
                if event.sender_id == bot.uid:
                    pass
                if not _pika.is_admin:
                    if silent is None:
                        await event.reply("You need to be admin to use this command")

            if "AmIAdm" in pika:

                _pika = await tgbot.get_permissions(event.chat_id, _selfpika.id)
                if _pika.is_admin:
                    await func(event)
                else:
                    if silent is None:
                        await event.reply("I am not Admin Nibba😷")

            if "OwnSudo" in pika:
                tgbotusers = list(TGBOT_USERS)
                if event.sender_id == bot.uid or event.sender_id in tgbotusers:
                    await func(event)
                else:
                    if silent is None:
                        await event.reply("**Error**: You are not a Sudo User, Owner.")

            if "Owner" in pika:
                if event.sender_id == bot.uid:
                    await func(event)
                else:
                    if silent is None: 
                        await event.reply("Only Owners can execute this Cmd")

            if "BotSudo" in pika:
                if event.sender_id in list(TGBOT_USERS):
                    await func(event)
     
        return wrapper

    return decorator

#©ItzSjDude </Kang/Copy with Credits else u will be called ultra gey/>
async def pika_msg(_pika, text, _pika_=None, parse_mode=None, link_preview=None):
  parse_mode = parse_mode or "md"; link_preview = link_preview or False
  if _pika_ is None:
      return await _pika.edit(text, parse_mode=parse_mode, link_preview=link_preview)
  else:
      return await _pika.reply(text, parse_mode=parse_mode,link_preview=link_preview)
#©ItzSjDude </Kang/Copy with Credits else u will be called ultra gey/> 
async def is_pikatg(_pika_=None):
  _pika = await _pika_.client.get_me()
  if _pika.id== tgbot.uid:
      return True
  else:
      return False
#©ItzSjDude </Kang/Copy with Credits else u will be called ultra gey/>
async def get_pika_id(_pika):
  _pika_= await _pika.client.get_me() 
  return _pika_.id 
#©ItzSjDude </Kang/Copy with Credits else u will be called ultra gey/>
async def get_pika_tg(_pika_): 
  _tg = await _pika_.client.get_me()
  if _tg.id == tgbot.uid:
      return True
  else:
      return None
try: 
   from pikabot.main_plugs.utils import *
   from pikabot.sql_helper.chats_sql import *
except: 
    pass

#©ItzSjDude </Kang/Copy with Credits else u will be called ultra gey/>
async def add_chat(_pika_):
  if await is_pikatg(_pika_): 
     if not _pika_.is_private:
        if not is_pika_exist(_pika_.chat_id): 
           add_pika(_pika_.chat_id)
           return "Added" 
  else:
    return
 
#©ItzSjDude </Kang/Copy with Credits else u will be called ultra gey/>
def pika_assistant(_pikasst=None):
    if ACTIVATE_ASSISTANT:
                                    #____Imports____
       import sys           
       import pikabot.utils
       from sys import modules
       from __main__ import l as rx
       from pathlib import Path as _asstpath
       import plugins.__init__ as _Modules
       logpa.info('✨STARTING PIKA ASSISTANT✨')
                                    #____Paths/Spec_____
       asstpath = _asstpath(f"./pikabot/Assistant/plugins/{_pikasst}.py")
       asstname = "pikabot.Assistant.plugins.{}".format(_pikasst)
       spec = spec_from_file_location(asstname, asstpath)
       asst = module_from_spec(spec)
                                   #____Pika_Assistant_Plugins_Loader____
       userbot = pikabot; asst.bot = bot; asst.tgbot = tgbot; asst.Var = Var; asst.rx = rx; asst.ItzSjDude = ItzSjDude; asst.pikatgbot = pikatgbot; modules['Asst_modules'] = _Modules       
       PikaAsst[_pikasst] = asst; modules["pikabot"+_pikasst] = asst; spec.loader.exec_module(asst); logpa.info("🔥Imported "+_pikasst)
       
    else: 
       return 

try:
   from pikabot import Pika_Cmd
except:
   Pika_Cmd = {}

chat = Var.SUDO_USERS
TG_HANDLER= os.environ.get("TG_HANDLER", "!")
if TG_HANDLER is not None: 
   _plug=f"\{TG_HANDLER}"
else: 
   _plug="\!"
   
if Var.CUSTOM_CMD is None:
  plug="\."
else:
  plug = f"\{Var.CUSTOM_CMD}"
client = bot 
try:
   from pikabot import tgbot
except:
    tgbot = None
BOTLOG = True

logpl=getLogger("Plugins_Loader..")
logpa=getLogger("ASSISTANT")
def Pikapi(**args):
    args["func"] = lambda e: e.via_bot_id is None
    stack = inspect.stack()
    previous_stack_frame = stack[1]
    file_test = Path(previous_stack_frame.filename)
    file_test = file_test.stem.replace(".py", "")
    if 1 == 0:
        return print("stupidity at its best")
    else:
        pattern = args.get("pattern", None)
        allow_sudo = args.get("allow_sudo", False)
        allow_edited_updates = args.get('allow_edited_updates', False)
        args["incoming"] = args.get("incoming", False)
        args["outgoing"] = True
        if bool(args["incoming"]):
            args["outgoing"] = False

        try:
            if pattern is not None and not pattern.startswith('(?i)'):
                args['pattern'] = '(?i)' + pattern
        except:
            pass

        reg = re.compile('(.*)')
        if not pattern == None:
            try:
                cmd = re.search(reg, pattern)
                try:
                    cmd = cmd.group(1).replace("$", "").replace("\\", "").replace("^", "")
                except:
                    pass

                try:
                    CMD_LIST[file_test].append(cmd)
                    Pika_Cmd[file_test].append(cmd)
                except:
                    Pika_Cmd.update({file_test: [cmd]})
                    CMD_LIST.update({file_test: [cmd]})
            except:
                pass

        if allow_sudo:
            args["from_users"] = list(Config.SUDO_USERS)
            # Mutually exclusive with outgoing (can only set one of either).
            args["incoming"] = True
        del allow_sudo
        try:
            del args["allow_sudo"]
        except:
            pass

        if "allow_edited_updates" in args:
            del args['allow_edited_updates']

        def decorator(func):
            if allow_edited_updates:
                bot.add_event_handler(func, events.MessageEdited(**args))
                bot.add_event_handler(func, events.NewMessage(**args))
            if bot2:
                bot2.add_event_handler(func, events.NewMessage(**args))
            if bot3:
                bot3.add_event_handler(func, events.NewMessage(**args))
            if bot4:
                bot4.add_event_handler(func, events.NewMessage(**args))
            try:
                LOAD_PLUG[file_test].append(func)
            except:
                LOAD_PLUG.update({file_test: [func]})
            return func

        return decorator

def load_module(shortname):
    if shortname.startswith("__"):
        pass
    elif shortname.endswith("_"):
        import pikabot.utils
        import sys
        import importlib
        from pathlib import Path
        path = Path(f"plugins/{shortname}.py")
        name = "plugins.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        logpl.info("Successfully (re)imported "+shortname)
    else:
        try:
          from pikabot import Pika_Cmd
        except:
          Pika_Cmd = {}
        from pikabot.handler import pikaa, pikarestart
        from pikabot import CMD_LIST as pika_cmd
        import logging 
        from __main__ import l as rx
        import plugins
        import pikabot.utils
        import sys
        import importlib
        from pathlib import Path
        path = Path(f"plugins/{shortname}.py")
        name = "plugins.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        userbot = pikabot
        mod = importlib.util.module_from_spec(spec)
        mod.bot = bot
        try: 
           mod.tgbot = bot.tgbot
        except:
            mod.tgbot= tgbot
            pass
        mod.Var = Var
        mod.rx = rx
        mod.command = Pikapi
        mod.ItzSjDude = ItzSjDude
        mod.pikaa = pikaa
        mod.pika_start = pikarestart
        mod.logger = logging.getLogger(shortname)
        sys.modules["SysRuntime"] = pikabot.main_plugs.SysRuntime
        sys.modules["userbot"] = pikabot
        sys.modules["userbot.utils"] = pikabot.utils
        mod.Config = Var
        mod.borg = bot
        sys.modules["uniborg.util"] = pikabot.utils
        # support for paperplaneextended
        sys.modules["userbot.events"] = userbot.utils
        spec.loader.exec_module(mod)
        bot.pika_cmd[shortname] = mod 
        # for imports
        sys.modules["pikabot"+shortname] = mod
        logpl.info("Successfully (re)imported "+shortname)


def remove_plugin(shortname):
    try:
        try:
            for i in LOAD_PLUG[shortname]:
                if bot is not None:
                  bot.remove_event_handler(i)
                if bot2 is not None:
                  bot2.remove_event_handler(i)
                if bot3 is not None:
                  bot3.remove_event_handler(i)
                if bot4 is not None:
                  bot4.remove_event_handler(i)
            del LOAD_PLUG[shortname]

        except:
            name = f"plugins.{shortname}"
            if bot is not None:
              for i in reversed(range(len(bot._event_builders))):
                  ev, cb = bot._event_builders[i],
                  if cb.__module__ == name:
                      del bot._event_builders[i]
            if bot2 is not None:
              for i in reversed (range(len(bot2._event_builders))):
                  ev, cx = bot2._event_builders[i],
                  if cx.__module__ == name:
                      del bot2._event_builders[i]
            if bot3 is not None:
              for i in reversed (range(len(bot3._event_builders))):
                  ev, cy = bot3._event_builders[i],
                  if cy.__module__ == name:
                      del bot3._event_builders[i]  
            if bot4 is not None:
              for i in reversed (range(len(bot4._event_builders))):
                  ev, cz = bot4._event_builders[i],
                  if cz.__module__ == name:
                      del bot4._event_builders[i]          
    except:
        raise ValueError

def admin_cmd(**args):
    args["func"] = lambda e: e.via_bot_id is None
    
    stack = inspect.stack()
    previous_stack_frame = stack[1]
    file_test = Path(previous_stack_frame.filename)
    file_test = file_test.stem.replace(".py", "")
    pattern = args.get("pattern", None)
    allow_sudo = args.get("allow_sudo", False)
    disable_errors = args.get("disable_errors", False)
    # get the pattern from the decorator
    if pattern is not None:
        if pattern.startswith("\#"):
            # special fix for snip.py
            args["pattern"] = re.compile(pattern)
        else:
            args["pattern"] = re.compile(plug + pattern)
            cmd = plug + pattern
            try:
                CMD_LIST[file_test].append(cmd)
                Pika_Cmd[file_test].append(cmd)
            except:
                CMD_LIST.update({file_test: [cmd]})
                Pika_Cmd.update({file_test: [cmd]})
    args["outgoing"] = True
    # should this command be available for other users?
    if allow_sudo:
        args["from_users"] = list(Var.SUDO_USERS)
        # Mutually exclusive with outgoing (can only set one of either).
        args["incoming"] = True
        del args["allow_sudo"]

    # error handling condition check
    elif "incoming" in args and not args["incoming"]:
        args["outgoing"] = True

    # add blacklist chats, UB should not respond in these chats
    args["blacklist_chats"] = True
    black_list_chats = list(Var.UB_BLACK_LIST_CHAT)
    if len(black_list_chats) > 0:
        args["chats"] = black_list_chats

    # check if the plugin should allow edited updates
    allow_edited_updates = False
    if "allow_edited_updates" in args and args["allow_edited_updates"]:
        allow_edited_updates = args["allow_edited_updates"]
        del args["allow_edited_updates"]

    # check if the plugin should listen for outgoing 'messages'
    is_message_enabled = True

    return events.NewMessage(**args)


def ItzSjDude(**args):
    args["func"] = lambda e: e.via_bot_id is None
    stack = inspect.stack()
    previous_stack_frame = stack[1]
    file_test = Path(previous_stack_frame.filename)
    file_test = file_test.stem.replace(".py", "")
    pattern = args.get("pattern", None)
    disable_edited = args.get('disable_edited', True)
    allow_sudo = args.get("allow_sudo", False) 
    disable_errors = args.get("disable_errors", False)
    disable_edited = args.get('disable_edited', True)
    groups_only = args.get('groups_only', False)
    trigger_on_fwd = args.get('trigger_on_fwd', False)
    trigger_on_inline = args.get('trigger_on_inline', False)
    pika = args.get("pika", False)
    args["outgoing"] = True
  
    if pika:
       args["incoming"] = True
       del args["pika"]
       
    if allow_sudo:
        args["from_users"] = list(Var.SUDO_USERS)
        args["incoming"] = True
        del args["allow_sudo"]

    elif "incoming" in args and not args["incoming"]:
        args["outgoing"] = True

    if pattern is not None:
        if pika:
            if pattern.startswith("^/"):
                pikatg = pattern.replace("^/", "\/")
                args["pattern"]= re.compile(pikatg)

            elif pattern.startswith("\#"):
            # special fix for snip.py
                args["pattern"] = re.compile(pattern)
            else: 
                args["pattern"] = re.compile(_plug + pattern)
                pikatg = _plug + pattern
            
            try:
               PikaAsst[file_test].append(pikatg)
            except:
               PikaAsst.update({file_test: [pikatg]})
                    
        else:
            if pattern.startswith("\#"):
                args["pattern"] = re.compile(pattern)
            if pattern.startswith("^."):  
                pikacmd = pattern.replace("^.", "")
                args["pattern"] = re.compile(plug + pikacmd)
                cmd = plug + pikacmd
                try:
                    Pika_Cmd[file_test].append(cmd)
                    CMD_LIST[file_test].append(cmd)
                except:
                    CMD_LIST.update({file_test: [cmd]})
                    Pika_Cmd.update({file_test: [cmd]})
            else:
                args["pattern"] = re.compile(plug + pattern)
                cmd = plug + pattern
                try:
                    Pika_Cmd[file_test].append(cmd)
                    CMD_LIST[file_test].append(cmd)
                except:
                    CMD_LIST.update({file_test: [cmd]})
                    Pika_Cmd.update({file_test: [cmd]})

    # check if the plugin should allow edited updates
    allow_edited_updates = False
    if "allow_edited_updates" in args and args["allow_edited_updates"]:
        allow_edited_updates = args["allow_edited_updates"]
        del args["allow_edited_updates"]
    if "trigger_on_inline" in args:
        del args['trigger_on_inline']
    if "disable_edited" in args:
        del args['disable_edited']
    if "groups_only" in args:
        del args['groups_only']
    if "disable_errors" in args:
        del args['disable_errors']
    if "trigger_on_fwd" in args:
        del args['trigger_on_fwd']
    # check if the plugin should listen for outgoing 'messages'
    is_message_enabled = True

    def decorator(func):
        async def wrapper(check):
            if BOTLOG:
                send_to = BOTLOG_CHATID
            if not trigger_on_fwd and check.fwd_from:
                return
            if check.via_bot_id and not trigger_on_inline:
                return
            if disable_errors:
                return 
            if groups_only and not check.is_group:
                await check.respond("`I don't think this is a group.`")
                return            
            try:
                await func(check)
            except events.StopPropagation:
                raise events.StopPropagation
            except KeyboardInterrupt:
                pass
            except BaseException as e:
                pikalog.exception(e) 
                if not disable_errors:
                    date = strftime("%Y-%m-%d %H:%M:%S", gmtime())

                    text = "**Sorry, I encountered a error!**\n"
                    link = "[https://t.me/PikachuUserbotSupport](Pikabot Support Chat)"
                    text += "If you wanna you can report it"
                    text += f"- just forward this message to {link}.\n"
                    text += "I won't log anything except the fact of error and date\n"

                    ftext = "\nDisclaimer:\nThis file uploaded ONLY here, "
                    ftext += "we logged only fact of error and date, "
                    ftext += "we respect your privacy, "
                    ftext += "you may not report this error if you've "
                    ftext += "any confidential data here, no one will see your data "
                    ftext += "if you choose not to do so.\n\n"
                    ftext += "--------BEGIN PIKABOT TRACEBACK LOG--------"
                    ftext += "\nDate: " + date
                    ftext += "\nGroup ID: " + str(check.chat_id)
                    ftext += "\nSender ID: " + str(check.sender_id)
                    ftext += "\n\nEvent Trigger:\n"
                    ftext += str(check.text)
                    ftext += "\n\nTraceback info:\n"
                    ftext += str(format_exc())
                    ftext += "\n\nError text:\n"
                    ftext += str(sys.exc_info()[1])
                    ftext += "\n\n--------END USERBOT TRACEBACK LOG--------"

                    command = "git log --pretty=format:\"%an: %s\" -5"

                    ftext += "\n\n\nLast 5 commits:\n"

                    process = await asyncsubshell(command,
                                                  stdout=asyncsub.PIPE,
                                                  stderr=asyncsub.PIPE)
                    stdout, stderr = await process.communicate()
                    result = str(stdout.decode().strip()) \
                        + str(stderr.decode().strip())

                    ftext += result

                    file = open("error.log", "w+")
                    file.write(ftext)
                    file.close()

                    if BOTLOG:
                        await check.client.send_file(
                            send_to,
                            "error.log",
                            caption=text,
                        )
                    else:
                        await check.client.send_file(
                            check.chat_id,
                            "error.log",
                            caption=text,
                        )

                    remove("error.log")

        if bot:
            if pika:
                pass
            else:  
                bot.add_event_handler(wrapper, events.NewMessage(**args))
        if bot2:
            if pika:
                pass
            else:
                bot2.add_event_handler(wrapper, events.NewMessage(**args))
        if bot3:
            if pika:
                pass
           
            else:
                bot3.add_event_handler(wrapper, events.NewMessage(**args))
        if bot4:
            if pika:
                pass
            else:
                bot4.add_event_handler(wrapper, events.NewMessage(**args))
        if tgbot:
            if pika:
                tgbot.add_event_handler(wrapper, events.NewMessage(**args))
            else:
                pass
        try:
            LOAD_PLUG[file_test].append(wrapper)
        except Exception as e:
            LOAD_PLUG.update({file_test: [wrapper]})
  
        return wrapper 
    return decorator
    
     
async def progress(current, total, event, start, type_of_ps, file_name=None):
    """Generic progress_callback for both
    upload.py and download.py"""
    now = time.time()
    diff = now - start
    if round(diff % 10.00) == 0 or current == total:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff) * 1000
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = elapsed_time + time_to_completion
        progress_str = "[{0}{1}]\nProgress: {2}%\n".format(
            ''.join(["█" for i in range(math.floor(percentage / 5))]),
            ''.join(["░" for i in range(20 - math.floor(percentage / 5))]),
            round(percentage, 2))
        tmp = progress_str + \
            "{0} of {1}\nETA: {2}".format(
                humanbytes(current),
                humanbytes(total),
                time_formatter(estimated_total_time)
            )
        if file_name:
            await event.edit("{}\nFile Name: `{}`\n{}".format(
                type_of_ps, file_name, tmp))
        else:
            await event.edit("{}\n{}".format(type_of_ps, tmp))


def humanbytes(size):
    """Input size in bytes,
    outputs in a human readable format"""
    # https://stackoverflow.com/a/49361727/4723940
    if not size:
        return ""
    # 2 ** 10 = 1024
    power = 2**10
    raised_to_pow = 0
    dict_power_n = {0: "", 1: "Ki", 2: "Mi", 3: "Gi", 4: "Ti"}
    while size > power:
        size /= power
        raised_to_pow += 1
    return str(round(size, 2)) + " " + dict_power_n[raised_to_pow] + "B"


def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time
    
def time_formatter(milliseconds: int) -> str:
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = ((str(days) + " day(s), ") if days else "") + \
        ((str(hours) + " hour(s), ") if hours else "") + \
        ((str(minutes) + " minute(s), ") if minutes else "") + \
        ((str(seconds) + " second(s), ") if seconds else "") + \
        ((str(milliseconds) + " millisecond(s), ") if milliseconds else "")
    return tmp[:-2]


class Loader():
    def __init__(self, func=None, **args):
        self.Var = Var
        bot.add_event_handler(func, events.NewMessage(**args))


