def msg():
    send=int(input("No. of friends"))
    friends=[]
    emails=[]
    message=input("Enter your message")
    for send1 in range(0,send):
        names=input("Enter your friend name")
        email=input("Enter your friend email:")
        friends.append(names)
        emails.append(email)
    print(friends)
    print(emails)
    import smtplib
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login("vk32446@gmail.com","y8185848792")
    for friends in range(0,len(friends)):
        print(message,":",emails[friends])
        server.sendmail
    ("vk32446@gmail.com",emails[friends],message)
    server.quit()