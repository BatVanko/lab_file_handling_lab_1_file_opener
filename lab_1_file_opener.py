file = open('text.txt','w')
file.writelines('''This is some random line
This is the second line
And this is the third one
''')

try :
    if file:
        print('File found')
except:
    print('File not found')
