import time
from datetime import datetime as dt


# a few variables
time_delay = 5  # help
start_time = 8
end_time = 17

hosts_temp = 'hosts'
hosts_path = r'C:\Windows\System32\drivers\etc\hosts'
redirect = '127.0.0.1'
websites = ['www.cnn.com', 'cnn.com', 'www.foxnews.com', 'foxnews.com']

file_written_flag = False

while True:
    time.sleep(time_delay)
    current_hour = dt.now().hour
    if dt.now().second > 30:

    #if (current_hour > start_time) and (current_hour < end_time):

        if file_written_flag:
            pass
            print('current seconds is-- {} seconds'.format(dt.now().second))
        else:
            with open(hosts_temp, 'r+') as file:
                content = file.read()
                for site in websites:
                    if site not in content:
                        print("writing to file")
                        file.write(redirect + " " + site + "\n")
                    else:
                        print('need to delete files')
            file_written_flag = True
    else:
        print('play time')
        if file_written_flag:
            print('rewriting files')
            with open(hosts_temp, 'r+') as file:
                content = file.readlines()
                file.seek(0)
                for line in content:
                    if not any(website in line for website in websites):
                        file.write(line)
                file.truncate()

            file_written_flag = False
        else:
            print('files already rewritten')



