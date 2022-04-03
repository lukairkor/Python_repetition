from pathlib import Path
a = Path('mbox-short.txt')
# name = input("Enter file:")
# if len(name) < 1 : name = "mbox-short.txt"
handle = open(a)

def get_email(filename, name):
    count = 0
    user = {}
    handle = open(a)

    for line in handle:      
        if name in line and 'From' in line and 'From:' not in line:
            arr = line.split(' ')
            count += 1
            user['email'] = count

    email = ''.join(arr[1])
    print (email, count)

get_email('mbox-short.txt', 'cwen')
#<= cwen@iupui.edu 5
# get_email('mbox-short.txt', 'david')
# #<= david.horwitz@uct.ac.za 4

# with open(filename) as handle:
#     for line in handle: