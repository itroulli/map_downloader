import time
import datetime
import requests
import os
# for playing sound while on windows
import winsound

today = datetime.datetime.now()
tomorrow = today + datetime.timedelta(days=1)
filename = tomorrow.strftime('%y%m%d.jpg')
new_name = tomorrow.strftime('%d-%m-%y_') + 'ΧΑΡΤΗΣ_ΠΡΟΒΛΕΨΗΣ_ΚΙΝΔΥΝΟΥ_ΠΥΡΚΑΓΙΑΣ.jpg'
destination = r'C:/Users/internet/Desktop/'
new_file = destination + new_name

winsound_path = r'C:/Users/internet/Desktop/map_downloader/gmae.wav'
url = r'https://www.civilprotection.gr/sites/default/gscp_uploads/' + filename


def exists(path):
    r = requests.head(path)
    return r.status_code == requests.codes.ok


if os.path.isfile(new_file):
    print("\n" + 60*"+" + "\n+" + 4*" " + "Έχετε ήδη κατεβάσει το χάρτη της αυριανής ημέρας!!" + 4*" " + "+\n" + 60*"+")
else:
    while True:
        now = datetime.datetime.now()
        if exists(url):
            r = requests.get(url, allow_redirects=True)
            print("\n Downloading...\n")
            open(new_file, 'wb').write(r.content)
            winsound.PlaySound(winsound_path, winsound.SND_LOOP | winsound.SND_ASYNC)
            print(now.strftime('%H:%M') + " Η διαδικασία ολοκληρώθηκε.")
            os.startfile(new_file)
            break
        else:
            try:
                print(now.strftime('%H:%M') + """ 
                Ο χάρτης δεν είναι ακόμα διαθέσιμος, παρακαλώ περιμένετε ή πιέστε Ctrl+C για ακύρωση...
                """)
                time.sleep(60)
            except KeyboardInterrupt:
                print("""
                 Η διαδικασία ακυρώθηκε.
                 """)
                break
