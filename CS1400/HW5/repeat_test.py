joke_response = input('''Pete, Pete, and Repeat went out on the lake in their
boat. Pete and Pete fell out. Who is left? ''')

if joke_response.upper() == 'REPEAT':
    loop_flag = True

elif joke_response.upper() == 

else:
    print('Nice try. Now, listen closely this time.')
    loop_flag = True

while loop_flag == True:
    joke_response = input('''Pete, Pete, and Repeat went out on the lake in
their boat. Pete and Pete fell out. Who is left? ''')
    try:
        if joke_response.upper() == 'QUIT':
            print('Goodbye, thank you for playing.')
            loop_flag = False
