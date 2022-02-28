import os
import sys
from time import sleep
from threading import Thread as td
 
 
a ='\033[92m'
b ='\033[91m'
c ='\033[0m'
blue= '\33[94m'
lightblue = '\033[94m'
red = '\033[91m'
white = '\33[97m'
yellow = '\33[93m'
green = '\033[1;32m'
cyan  = "\033[96m"
end = '\033[0m'
logo=yellow+str("""
⠀
          _____                    _____          
         /\    \                  /\    \         
        /::\    \                /::\____\        
       /::::\    \              /:::/    /        
      /::::::\    \            /:::/    /         
     /:::/\:::\    \          /:::/    /          
    /:::/__\:::\    \        /:::/____/           
    \:::\   \:::\    \      /::::\    \           
  ___\:::\   \:::\    \    /::::::\____\________  
 /\   \:::\   \:::\    \  /:::/\:::::::::::\    \ 
/::\   \:::\   \:::\____\/:::/  |:::::::::::\____\
\:::\   \:::\   \::/    /\::/   |::|~~~|~~~~~     
 \:::\   \:::\   \/____/  \/____|::|   |          
  \:::\   \:::\    \            |::|   |          
   \:::\   \:::\____\           |::|   |          
    \:::\  /:::/    /           |::|   |          
     \:::\/:::/    /            |::|   |          
      \::::::/    /             |::|   |          
       \::::/    /              \::|   |          
        \::/    /                \:|   |          
         \/____/                  \|___|          
                                                  
                                           
""")
logo2=red+str("""
+-+-+-+-+-+-+-+ +-+-+ +-+-+-+-+-+-+ +-+-+-+-+-+-+
 |W|e|l|c|o|m|e| |T|o| |S|i|l|e|n|t| |K|i|l|l|e|r|
 +-+-+-+-+-+-+-+ +-+-+ +-+-+-+-+-+-+ +-+-+-+-+-+-+
 """)
print(logo)

username="Silent"
password="Antick"

#input username & password

inu=str(input("Enter Your Username:"))
inp=str(input("Enter Your Password:"))

if username==inu and password==inp:
	print("Your User and Pass correct ")
	pass
else:
	print("Your User and Pass invaild")
	sys.exit()

class Terkey:
  def __init__(self):
    pass
 
  # Banner
  print(logo2)
  def banner(self):
      os.system('clear')
      print(f'{c}Silent Killer{a}[{c}Termux Key{a}]'.center(68))
      print(f'{a}Antick Roy'.center(53))
      print("".join([i for i in "\n"*2]))
 
  # Loading animation
  def animate(self,params):
    self.banner()
    print(logo2)
    print(f"{c}Setting up your key..")
    t = td(target=self.setup,args=(params,))
    t.start()
    while t.is_alive():
          for i in "-\|/-\|/":
              print(f'\r{c}Please wait {a}{i} ',end="",flush=True)
              sleep(0.1)
    self.banner()
    print(f"DONE !\n\n{c}Please run this tool again and select {a}About{c} menu\nfor more informations\nThanks !")
 
  # Of course, like it name, paginate !
  def paginate(self,data,n):
    n_data = round(len(data)/n) + 1
    new_data_part = []
    batas = 0
    for i in range(n_data):
      new_data = []
      for x in range(batas,n+batas):
        try:
          new_data.append(data[x])
        except:
          pass
        batas += 1
      if new_data: new_data_part.append(new_data)
    return new_data_part
 
  # setting up the selected keys
  def setup(self,keys):
      keys = f"extra-keys = {keys}"
      try:
          os.mkdir('/data/data/com.termux/files/home/.termux')
      except:
          pass
      open('/data/data/com.termux/files/home/.termux/termux.properties','w').write(keys)
      os.system('termux-reload-settings')
 
  # If you choose default keys, this function will be executed.
  def standar(self):
    key = "[['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
    return key
 
  def about(self):
    self.banner()
    print(f"""
    {a}W E L C O M E  !{c}
 
    This is Bangladesh, the Termux Keyb shortcut !
    A program from {a}Antick Roy{c} for you.
    This tool is only for Termux app and absolutely FREE !
 
    You can find all default keys in this program at
    {a}https://wiki.termux.com/wiki/Touch_Keyboard{c}
 
    Want to chat with me ? You can find me on
    * Telegram  : {a}@silentkiller365{c}
    * Facebook  : {a}https://www.facebook.com/silentkiller.abalalerbap.365{c}
    * Blog      : {a}https://www.blogger.com/u/2/blog/posts/5696645752341887262{c}
    * Youtube   : {a}https://youtube.com/channel/UCuOxR2IwadVT5fFafFqizlA{c}
 
    And if you want to give me some money, you can visit
    {a}hub WA 01941797375{c}
 
    """
    )
  # And if you select custom keys,
  def custom(self):
    index = 1
    lastindex = 0
    keys = ["CTRL","ALT","FN","SPACE","ESC","TAB","HOME","END","PGUP","PGDN","INS","DEL","BKSP","UP","LEFT","RIGHT","DOWN","ENTER","BACKSLASH","QUOTE","APOSTROPHE","F1","F2","F3","F4","F5","F6","F7","F8","F9","F10","F11","F12","KEYBOARD","DRAWER"]
    print(f"{a} --+ {c}Default Key Lists {a}+--".center(62))
    print()
    for i in self.paginate([*enumerate(keys)],4):
      for x in i:
        en = " " * (15 - len(". ".join([str(x[0]+1),x[1]])))
        print(f"{a}{x[0]+1}.{c} {x[1]}",end=en)
      print()
    print(f"{c}\nInput your selected key number \nand sparate it by comma (,) {a}ex: 1,2,3,4{c}\nOr you can add your own custom key \nlike {a}1,2,3,(,),*,<,>{c} etc.")
 
    selected_keys = []
    user_select = input(f"\n{a}Input {c}: ")
    ranges = [str(i+1) for i in range(len(keys))]
    for i in user_select.split(","):
      if i.isdigit() and i in ranges:
        selected_keys.append(keys[int(i)-1])
      else:
        selected_keys.append(i)
    return selected_keys
 
  # Main
  def start(self):
    self.banner()
    print(f"    {a}[ {c}MENU {a}]")
    print(f"""
  {a}1.{c} Use Default Keys
  {a}2.{c} Custom Keys
  {a}3.{c} About
    """
    )
    menu = input(f"  {c}>{a} ")
    if menu == "1":
      self.banner()
      key = self.standar()
      self.animate(key)
    elif menu == "2":
      self.banner()
      key = self.custom()
      keys = self.paginate(key,7)
      print(f"{c}\nSelected keys: {a}{','.join(key)}{c}\nAre you sure ?")
      try:
        input(f"{c}Press enter to continue or CTRL + C to cancel ")
        self.animate(keys)
      except:
        exit(f"{b}Canceled!{c}")
    elif menu == "3":
      self.about()
    else:
      pass
if __name__=='__main__':
  terkey = Terkey()
  terkey.start()
# ini cuma shortcut buat bantu para nub
# Hansaplast
 