import os
from random import randint
for day in range(0, 1):
    for commits in range(0, randint(1, 4)):
        day = str(day)+' days ago'
        with open('file.txt', 'a')as file:
            file.write(day)
        os.system('git add .')
        os.system('git commit --date="'+day+'" -m "commit"')
os.system('git push -u origin main')