# Chaturbate YOUTUBE-DL Remote Anonymous Freechat Recorder v.1.0.7 by horacio9a for Python 2.7.14
# coding: utf-8

import sys, os, urllib, urllib3, ssl, re, time, datetime, requests, random, command
urllib3.disable_warnings()
from urllib3 import PoolManager
reload(sys)
sys.setdefaultencoding('utf-8')
from colorama import init, Fore, Back, Style
from termcolor import colored
import ConfigParser
config = ConfigParser.ConfigParser()
config.read('config.cfg')

init()
print
print(colored(" => START <=", "yellow", "on_blue"))
print

if __name__=='__main__':
   import sys
model = sys.argv[1]

url ='https://chaturbate.com/{}/'.format(model)
manager = PoolManager(10)
r = manager.request('GET', url)
enc = (r.data)
dec=urllib.unquote(enc).decode()

if "HTTP 404" not in dec:
 try:
  pwd0 = dec.split(' password: ')[1]
  pwd = pwd0.split("'")[0]
 except:
  print(colored(" => Try again <=", "yellow",'on_red'))
  print
  print(colored(" => END <=", "yellow","on_blue"))
  sys.exit()

 if "currently offline" not in dec:
  hlsurl0 = dec.split("source src='")[1]
  hlsurl1 = hlsurl0.split("'")[0]

  if len(hlsurl1) > 180:
   print(colored(" => TRY AGAIN <=", "yellow","on_blue"))
   sys.exit()
  else:
   pass

   if len(hlsurl1) > 1:
      hlsurl2 = hlsurl1.split('&amp')[0]
      hlsurl = re.sub('_fast_', '_', hlsurl2)

      if "_aac" not in hlsurl:
        urlf = 'amlst'
      else:
        urlf = 'aac'

      bg0 = dec.split("gender: '")[1]
      bg = bg0.split("'")[0]
      print (colored(" => INFO => HLS_URL: ({}) * BG: ({}) <= ", "yellow", "on_blue")).format(urlf,bg)

      timestamp = str(time.strftime("%d%m%Y-%H%M%S"))
      path = config.get('folders', 'output_folder')
      filename = model + '_CB_' + timestamp
      pf = (path + filename + '.ts')
      youtube = config.get('files', 'youtube')

      print
      print (colored(' => YTDL-REC => {}.ts <=', 'yellow', 'on_red')).format(filename)
      print
      command = ('{} -i --hls-use-mpegts --no-part -q {} -o {}'.format(youtube,hlsurl,pf))
      os.system(command)
      print
      print(colored(" => END <= ", 'yellow','on_blue'))
      sys.exit()

   else:
      print(colored(" => Model is PVT/HIDDEN or AWAY <=", "yellow","on_red"))
      print
      print(colored(" => END <=", "yellow","on_blue"))
      sys.exit()

 else:
   print(colored(" => Model is OFFLINE <=", "yellow","on_red"))
   print
   print(colored(" => END <=", "yellow","on_blue"))
   sys.exit()

else:
   print(colored(" => Page Not Found <=", 'yellow','on_red'))
   print
   print(colored(" => END <=", "yellow","on_blue"))
   sys.exit()
