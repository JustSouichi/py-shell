import os
import pwd
import socket
from termcolor import colored 
import datetime

bash_statement = True

while bash_statement == True:
  now = datetime.datetime.now()
  user_name = pwd.getpwuid(os.getuid())[0]
  user_pc = socket.gethostname().split('.')[0]
  user_current_path = os.getcwd()
  if user_current_path == '/Users/' + user_name: 
    user_path_to_print = colored('~', 'green')
  else:
    path_to_print = "~" + user_current_path
    user_path_to_print = colored(path_to_print, 'green')

  terminal_display = user_name + "@" + user_pc + ":" + user_path_to_print + "$"      
  user_input = input(terminal_display + " ")
  user_input_splitted = user_input.split()
  first_user_input_argument = user_input_splitted[0]

  if first_user_input_argument == "quit" or first_user_input_argument == "exit":
    now = datetime.datetime.now()
    print("[ Session Ended At " + str(now.hour) + ":" + str(now.minute) + "]")
    bash_statement = False
  
  elif first_user_input_argument == '':
    pass
  else:
    print("-bash: " + first_user_input_argument + ": command not found")
