from urllib.parse import quote
import datetime
import os
import ssl
from urllib.parse import urlencode
from http import cookiejar
from urllib3.exceptions import InsecureRequestWarning
import hashlib
import random
try:
    import base64
    from requests.exceptions import RequestException
    import requests
    import pystyle
    from concurrent.futures import ThreadPoolExecutor
    from faker import Faker
    from requests import session
    import concurrent.futures
    
except ImportError:
    import os
    os.system("pip install base64")
import requests,os,time,re,json,uuid,random,sys
from concurrent.futures import ThreadPoolExecutor
import datetime
from datetime import datetime
import requests,json
import uuid
import requests
from time import sleep
from random import choice, randint, shuffle
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from os.path import isfile
from pystyle import Colors, Colorate, Write, Center, Add, Box
from time import sleep,strftime
import socket
from pystyle import *
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def runbanner(text, delay=0.001):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

trang = "\033[1;37m\033[1m"
xanh_la = "\033[1;32m\033[1m"
xanh_duong = "\033[1;34m\033[1m"
xanhnhat = '\033[1m\033[38;5;51m'
do = "\033[1;31m\033[1m\033[1m"
xam='\033[1;30m\033[1m'
vang = "\033[1;33m\033[1m"
tim = "\033[1;35m\033[1m"
hongnhat = "#FFC0CB"
kt_code = "</>"
dac_biet = "\033[32;5;245m\033[1m\033[38;5;39m"
colors = [
    "\033[1;37m\033[1m",  # Trắng
    "\033[1;32m\033[1m",  # Xanh lá
    "\033[1;34m\033[1m",  # Xanh dương
    "\033[1m\033[38;5;51m",  # Xanh nhạt
    "\033[1;31m\033[1m\033[1m",  # Đỏ
    "\033[1;30m\033[1m",  # Xám
    "\033[1;33m\033[1m",  # Vàng
    "\033[1;35m\033[1m",  # Tím
    "\033[32;5;245m\033[1m\033[38;5;39m",  # Màu đặc biệt
]
random_color = random.choice(colors)
def idelay(o):
    while(o>0):
        o=o-1
        print(f"{trang}[{do}</>{trang}] \033[1;33mV\033[1;34mu\033[1;35mi \033[1;32mL\033[1;33mò\033[1;34mn\033[1;35mg \033[1;36mC\033[1;33mh\033[1;34mờ {trang}[\033[1;35m.....""]""["+str(o)+"]""    ",end='\r')
        time.sleep(1/6)
        print(f"{trang}[{do}</>{trang}] \033[1;31mV\033[1;32mu\033[1;33mi \033[1;34mL\033[1;35mò\033[1;31mn\033[1;32mg \033[1;33mC\033[1;32mh\033[1;35mờ {trang}[\033[1;33m•{trang}....""]"f"{trang}[{xanhnhat}"+str(o)+f"{trang}]""     ",end='\r')
        time.sleep(1/6)
        print(f"{trang}[{do}</>{trang}] \033[1;32mV\033[1;33mu\033[1;34mi \033[1;35mL\033[1;36mò\033[1;33mn\033[1;34mg \033[1;35mC\033[1;31mh\033[1;32mờ {trang}[\033[1;35m••{trang}...""]"f"{trang}[{xanh_la}"+str(o)+f"{trang}]""     ",end='\r')
        time.sleep(1/6)
        print(f"{trang}[{do}</>{trang}] \033[1;31mV\033[1;33mu\033[1;35mi \033[1;33mL\033[1;31mò\033[1;32mn\033[1;34mg \033[1;36mC\033[1;35mh\033[1;31mờ {trang}[\033[1;32m•••{trang}..""]"f"{trang}[{do}"+str(o)+f"{trang}]""     ",end='\r')
        time.sleep(1/6)
        print(f"{trang}[{do}</>{trang}] \033[1;32mV\033[1;34mu\033[1;36mi \033[1;32mL\033[1;34mò\033[1;31mn\033[1;35mg \033[1;33mC\033[1;36mh\033[1;35mờ {trang}[\033[1;38m••••{trang}.""]"f"{trang}[{tim}"+str(o)+f"{trang}]""     ",end='\r')
        time.sleep(1/6)
        print(f"{xanhnhat}\033[1;37m[</>]\033[1;31mV\033[1;34mu\033[1;36mi \033[1;32mL\033[1;34mò\033[1;32mn\033[1;35mg \033[1;36mC\033[1;34mh\033[1;32mờ {trang}[\033[1;33m•••••{trang}""]"f"{trang}[{vang}"+str(o)+f"{trang}]""     ",end='\r')
        time.sleep(0.1)
        print(f"{trang}[{do}</>{trang}] \033[1;31mV\033[1;34mu\033[1;36mi \033[1;32mL\033[1;34mò\033[1;32mn\033[1;35mg \033[1;36mC\033[1;34mh\033[1;32mờ {trang}[\033[1;33m•••••{trang}""]"f"{trang}[{xanh_la}"+str(o)+f"{trang}]""     ",end='\r')

chontool = f"""
\033[1;32m════════════════════════════════════════════════════╗
\033[1;32m║\033[1;37m██╗░░██╗░█████╗░██████╗░██╗  ██████╗░░██╗░░░░░░░██╗\033[1;32m║
\033[1;32m║\033[1;37m██║░░██║██╔══██╗██╔══██╗██║  ██╔══██╗░██║░░██╗░░██║\033[1;32m║
\033[1;32m║\033[1;37m███████║███████║██████╔╝██║  ██║░░██║░╚██╗████╗██╔╝\033[1;32m║
\033[1;32m║\033[1;37m██╔══██║██╔══██║██╔══██╗██║  ██║░░██║░░████╔═████║░\033[1;32m║
\033[1;32m║\033[1;37m██║░░██║██║░░██║██║░░██║██║  ██████╔╝░░╚██╔╝░╚██╔╝░\033[1;32m║ 
\033[1;32m║\033[1;37m╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝  ╚═════╝░░░░╚═╝░░░╚═╝░░\033[1;32m║  
\033[1;32m╠═══════════════════════════════════════════════════╣
\033[1;32m║\033[1;34m▶ tele : \033[1;37mDw_111                                    \033[1;32m║
\033[1;32m╠\033[1;34m▶ zalo : \033[1;37m0327921302                                \033[1;32m║
\033[1;32m╚═══════════════════════════════════════════════════╝
\033[1;32m-------------------------------------------------"""
clear()
runbanner(chontool)
idcanspam=input(f'\033[1;97m[\033[1;31m</>\033[1;97m] {xanhnhat}ID Box Cần Thả Sớ :{vang} ')
while True:
      ck=input(f'\033[1;97m[\033[1;31m</>\033[1;97m] {xanhnhat}Nhập Cookie Facebook :{vang} ')
      try:
        get=requests.get(f'https://mbasic.facebook.com/privacy/touch/block/confirm/?bid={idcanspam}&ret_cancel&source=profile',headers={'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','cookie': ck,'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1'}).text
        fb_dtsg=get.split('<input type="hidden" name="fb_dtsg" value="')[1].split('" autocomplete="off" />')[0]
        jazoest=get.split('<input type="hidden" name="jazoest" value="')[1].split('" autocomplete="off" />')[0]
        clear()
        break
      except:
        print(f'{do}Cookie sai!!')   
        runbanner(chontool)
params = {
      "icm": '1',
    }
    
headers = {
      "Host":"mbasic.facebook.com",
      "content-length":"87",
      "content-type":"application/x-www-form-urlencoded",
      "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
      "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
      "sec-fetch-site":"same-origin",
      "sec-fetch-mode":"navigate",
      "sec-fetch-user":"?1",
      "sec-fetch-dest":"document",
      "accept-encoding":"gzip, deflate, br",
      "accept-language":"vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
      "cookie":ck,
    }
SO_CHUI = [
f"Bạn là một kho báu... chỉ tiếc là kho báu đấy nằm trong lòng đất, không ai tìm thấy ",
f"Có một loại người, đi đâu cũng làm ánh sáng mờ đi, mà lại cứ tưởng mình là mặt trời. ",
f"Bạn không phải là người tồi, chỉ là bạn làm việc với tất cả sự thiếu hiểu biết mà thôi. ",
f"Nếu sự ngu ngốc là một môn thể thao, chắc bạn đã giành huy chương vàng rồi. ",
f"Có một thứ còn tệ hơn sự im lặng của bạn, đó là khi bạn mở miệng và mọi người phải đau đầu. ",
f"Bạn là minh chứng cho việc thiên nhiên không phải lúc nào cũng làm đúng quyết định trong quá trình tiến hoá. ",
f"Chắc bạn đã nghe câu 'im lặng là vàng', nhưng tiếc là bạn không bao giờ hiểu được giá trị của nó. ",
f"Chắc chắn bạn là người đầu tiên làm cho việc nói 'không biết' trở nên đáng ngưỡng mộ. ",
f"Bạn có thể chẳng bao giờ là người hoàn hảo, nhưng chắc chắn bạn là người khiến người khác cảm thấy mình cũng chẳng đến nỗi nào. ",
f"Nếu sự tự tin là chìa khóa thành công, bạn chắc hẳn sẽ mở được cả một vũ trụ rồi. ",
f"Chắc bạn đã làm bạn với sự ngu dốt lâu đến mức nó trở thành người bạn thân nhất của bạn. ",
f"Nói chuyện với bạn giống như đọc sách hướng dẫn sử dụng… mãi chẳng hiểu được gì! ",
f"Bạn có một trái tim ấm áp… tiếc là bạn chưa bao giờ biết cách sử dụng nó. ",
f"Bạn có thể làm gián đoạn một cuộc trò chuyện bằng cách im lặng, và đó cũng là tài năng đặc biệt của bạn. ",
f"Chắc bạn đã từng nghe câu 'chậm mà chắc', nhưng tiếc là bạn lại làm ngược lại, vừa chậm vừa sai. ",
f"Chắc bạn là người duy nhất có thể khiến một chiếc tivi cũng cảm thấy xấu hổ vì sự tẻ nhạt của mình. ",
f"Bạn giống như một chiếc đèn, nhưng mà chỉ tỏa ra ánh sáng yếu ớt và không đủ để soi sáng cho ai cả. ",
f"Sự khôn ngoan của bạn là một phép màu mà cả thế giới vẫn đang cố gắng giải thích. ",
f"Nếu tôi có thể cho bạn một lời khuyên, đó là nên đóng cửa lại và đừng bao giờ mở miệng nữa. ",
f"Bạn có một bộ óc cực kỳ sáng tạo… chỉ là sáng tạo ra những lý do ngớ ngẩn thôi. ",
]
clear()
runbanner(chontool)
delay=int(input(f'\033[1;97m[\033[1;31m</>\033[1;97m] {xanhnhat}Nhập delay(khuyến cáo trên 1s) :{vang} '))
while True:
        try:
          ping = requests.get("https://www.google.com")
          if ping.status_code == 200:
            for nd in SO_CHUI:
                data = f"fb_dtsg={fb_dtsg}&jazoest={jazoest}&body={nd}&send=Send&tids=cid.g.{idcanspam}&wwwupp=C3&platform_xmd=&referrer=&ctype=&cver=legacy&csid=366a74a7-2d30-45dd-94c2-ad47d662dcfb"  
                response = requests.post("https://mbasic.facebook.com/messages/send/", params=params, headers=headers, data=data.encode('utf-8'))
                NOIDUNG = f"\033[1;35mĐã Gửi Thành Công\033[1;31m : \033[1;97m{nd}"
                print(f"{NOIDUNG}")
                idelay(delay)
        except Exception as e:
          print(f"{do}Lỗi bị ngắt kết lối vui lòng kết lối lại mạng để tiếp tục sớ")
          time.sleep(5)
else:
    print(f"{do} Sai Rồi Em Êy !")   