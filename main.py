import os
import datetime as dt
# import keyboard

HOST_LIST_FILE = 'C:/Users/ai887/Documents/Python_Scripts/ping_hosts/hosts_list.txt'
PACKETS = 3
FILE_TO_SAVE = 'ping_test.txt'
DATETIME = dt.datetime.strftime(dt.datetime.now(), '%d/%m/%Y %H:%M')
# KEY_T0_STOP = 'q'
# continue_script = True


def output_to_file():
    with open(HOST_LIST_FILE) as f:
        hosts_list = f.read().splitlines()
        print(hosts_list)
    for host in hosts_list:
        ping_host = os.popen(f'ping -n {PACKETS} {host}').read().encode('cp1251').decode('cp866')
        print(ping_host)
        with open(FILE_TO_SAVE, 'a+') as fs:
            fs.write(f'{DATETIME}\n{ping_host}\n')


# def stop():
#     global continue_script
#     continue_script = False
#     return continue_script

output_to_file()

# while continue_script:
#     output_to_file()
#     print('Press Enter to continue or q to quit')
#     if keyboard.read_key() == KEY_T0_STOP:
#         stop()
