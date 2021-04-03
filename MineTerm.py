import sys
from mcpi.minecraft import Minecraft as minc

passwords   = {'pi':'testberry'}
version     = '0.0.1 PreAlpha build'
prompt      = '>_'
str_input   = None
commands    =  ['nick', 'tp']

print('MineTerm \n' + version, 'running on Python', sys.version,  '''
By LEHAtupointow: lehatupointow.blogspot.com
use /help for more information on commands.''')
login = input('MineTerm.login:')
password = input('PassWord.Mineterm.local:')
try:
    if password == passwords[login]:
        print('pass ok')
except:
    raise ImportError ('Incorrect Login')
    sys.exit()
    
    
mc = minc.create()
nick =  input('Your Nickname:')
nick = '<' + nick + '>'
while str_input != 'quit':
    str_input =  input(prompt)
    if not str_input.startswith('/') and not str_input == 'quit':
        mc.postToChat(nick + ': ' + str_input)
    elif str_input == 'quit':
        mc.postToChat(nick + ' Left MineTerm.')
    else:
        cmnd = str_input.lstrip('/')
        if cmnd in commands:
            indx = commands.index(cmnd)
            cmnd.lstrip(commands[indx])
            if indx == 0:
                mc.postToChat('your nick is ' + nick)
            elif indx == 1:
                args = cmnd.split(' ')
                try:
                    mc.player.setPos(args[0], args[1], args[2])
                except:
                    print('error')

        else:
            print('Pardon? UnknownCommand error.')
            
            
