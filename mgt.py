import os,sys

print "Proxy Management Console"

cont = True
while cont:
    inp = raw_input("-->")

    #Order matters due to .find()
    if inp.find("unblock ") != -1:
        print "Unblocking:", inp[8:]
        f = open("blacklist.txt","r")
        lines = f.readlines()
        f.close()
        f = open("blacklist.txt","w")
        for line in lines:
            if line != inp[8:]+"\n":
                f.write(line)
        f.close()

    elif inp.find("block ") != -1:
        print "Blocking:", inp[6:]
        file = open("blacklist.txt" ,'a+')
        file.write(inp[6:] + "\n")
        file.close()

    elif inp == "close":
        cont = False
    else:
        print "Unknown command"
