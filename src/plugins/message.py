from typing import AnyStr
import urllib
import urllib.parse
import urllib.request
from warnings import filterwarnings
from bs4 import BeautifulSoup
from nonebot import on_startswith, on_keyword
import nonebot
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Bot, Message, GroupMessageEvent
from random import choice
import json, requests


appid = 'A49AQ4-PR59YG97WK'
def answer(question):
    try:
        serviceurl = 'http://api.wolframalpha.com/v1/result?'
        url = serviceurl + urllib.parse.urlencode({'appid': appid, 'i': question, 'timeout': '15'})
        uh = urllib.request.urlopen(url)
        soup = BeautifulSoup(uh,'lxml')
        short_answer = soup.get_text()
        return short_answer

    except urllib.error.HTTPError:
        full_serviceurl = 'http://api.wolframalpha.com/v2/query?'
        url = full_serviceurl + urllib.parse.urlencode({'input': question, 'appid': appid, 'format': 'plaintext', 'totaltimeout': '15.0'})
        full_answer = ''
        data = urllib.request.urlopen(url)
        soup = BeautifulSoup(data, 'lxml')
        for pt in soup.find_all('plaintext'):
            full_answer += pt.get_text() + '\n'
        if len(full_answer) == 0:
            return 'Cirno does not understand.'
        return full_answer

    except nonebot.adapters.cqhttp.exception.NetworkError:
        return 'Cirno got some problems of network.'

    else:
        return 'Cirno does not understand.'


default = on_startswith('', rule = to_me())
@default.handle()
async def default_answer(bot: Bot, event: GroupMessageEvent, state: T_State):
    if 'fig' in str(event.get_message()):
        ans = ''
        await one_plus_one_question.finish(ans)
    if 'cg' in str(event.get_message()):
        ans = ''
        await one_plus_one_question.finish(ans)
    ans = 'Cirno does not understand.' + '[CQ:image,file=http://34.92.148.104/images/2021/05/21/Jnb7IMO5.jpg]'
    ans = Message(ans)
    await default.finish(ans)

one_plus_one = {'1+1', '1 + 1', '1 + 1 =', '1+1=?','1 + 1 = ?', 'one plus one'}    
one_plus_one_question = on_keyword(one_plus_one, rule = None)
@one_plus_one_question.handle()
async def one_plus_one_question_answer(bot: Bot, event: GroupMessageEvent, state: T_State):
    if 'fig' in str(event.get_message()):
        ans = ''
        await one_plus_one_question.finish(ans)
    ans = '⑨!'
    await one_plus_one_question.finish(ans)

question = on_startswith('fig', rule = None)
@question.handle()
async def question_answer(bot: Bot, event: GroupMessageEvent, state: T_State):
    args = str(event.get_message()).lstrip('fig')
    if '@琪露诺♪数学教室 ' in args:
        args = args.lstrip('@琪露诺♪数学教室 ')
    ans = answer(args)
    ans = Message(ans)
    await question.finish(ans)

ticktock = {'ticktock', '色图', 'eli', '爱莉', 'TickTock', 'lsp'}
ticktockOwO = on_keyword(ticktock, rule = None)
@ticktockOwO.handle()
async def ticktockOwO_answer(bot: Bot, event: GroupMessageEvent, state: T_State): 
    ans = 'Hentai!'
    ans = Message(ans)
    await ticktockOwO.finish(ans)

cry = {'呜呜呜', '呜呜呜呜', '555', '嘤嘤嘤', '哭', '抱抱'}
crying = on_keyword(cry, rule = None)
@crying.handle()
async def crying_answer(bot: Bot, event: GroupMessageEvent, state: T_State): 
    ans = 'Do not worry, everything will be fine!'
    ans = Message(ans)
    await crying.finish(ans)

cirno = {'baka', 'cirno', 'Cirno', '琪露诺', '⑨'}
special = on_keyword(cirno, rule = None)
@special.handle()
async def special_answer(bot: Bot, event: GroupMessageEvent, state: T_State): 
    ans = 'Cirno thinks she is a smart girl.' + '[CQ:image,file=http://34.92.148.104/images/2021/05/18/44525459_p0_master1200.jpg]'

    if 'not' in str(event.get_message()):
        ans = 'Thanks!'
    ans = Message(ans)
    await special.finish(ans)

cgimg = {'cg'}
cgimage = on_keyword(cgimg, rule = to_me())
@cgimage.handle()
async def cgimage_answer(bot: Bot, event: GroupMessageEvent, state: T_State):
    url = 'http://www.dmoe.cc/random.php'
    params = {'return': 'json'}
    res = requests.get(url, params=params).json()
    url = res['imgurl']
    ans = '[CQ:image,file=' + url + ']'
    ans = Message(ans)
    await cgimage.finish(ans)