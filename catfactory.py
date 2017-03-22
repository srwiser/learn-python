import os
import platform
import subprocess
import requests
import shutil
import settings_local

def main():
    print_the_header()
    base_folder = os.path.abspath(os.path.dirname(__file__))
    folder = settings_local.catwebsite['localfolder']
    full_path = os.path.join(base_folder, folder)
    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print('Creating new directory at {}'.format(full_path))
        os.mkdir(full_path)

    user_input = 'EMPTY'
    while user_input != 'nay':
        user_input = raw_input('Want to see a cat pic? Yay or Nay:  ')
        user_input = user_input.lower().strip()

        if user_input == 'yay':
            rawdata = get_pic(url=settings_local.catwebsite['url'])
            save_pic(rawdata, full_path)
            show_pic(full_path)
        elif user_input != 'nay' and user_input:
            print("Sorry, we don't understand '{}'.".format(user_input))

    print('Done, goodbye.')

def print_the_header():
    print '---------------------------------'
    print '           Random CAT Pics'
    print '---------------------------------'
    print ''


def get_pic(url):
    response = requests.get(url, stream=True)
    return response.raw

def save_pic(rawdata,full_path):
    catpic = os.path.join(full_path, 'random' + '.jpg')
    with open(catpic, 'wb') as fout:
        shutil.copyfileobj(rawdata, fout)
    return full_path


def show_pic(full_path):
    print('Displaying cats in OS window.')
    if platform.system() == 'Darwin':
        subprocess.call(['open', full_path])
    elif platform.system() == 'Windows':
        subprocess.call(['explorer', full_path])
    elif platform.system() == 'Linux':
        subprocess.call(['xdg-open', full_path])
    else:
        print("We don't support your os: " + platform.system())

if __name__ == '__main__':
    main()
