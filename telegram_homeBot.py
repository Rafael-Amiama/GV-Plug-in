import os
import glob
import datetime  
import time
import telepot   
from telepot.loop import MessageLoop    
from time import sleep      
import ffmpeg
from multiprocessing import Process


mydir = os.getcwd()
backdoorCamStream = "rtsp://xxxxxxxxxx:554/11"
frontDoorCamStream = "rtsp://xxxxxxxxxx:554/11"
GarageCamStream = "rtsp://xxxxxxxxxxxx:554/11"
DrivewayCamStream = "rtsp://xxxxxxxxxxxxx:554/11"
CornerCamStream = "rtsp://xxxxxxxxxxxxxxxxxxxx:554/stream0"
PatioCamStream = "rtsp://xxxxxxxxxxxxxxxx:554/stream0"
user_001 = xxxxxxxxxxxx # this is the chat_id of the user that wants to receive motion notifications, multiple users will be added later



def testing001():
    #print(os.listdir(mydir + "\\campics"))
    folderName = os.listdir(mydir + "\\campics")
    num = 0
    for x in folderName:
        print(folderName[num])
        num += 1



def imgRequest(chat_id, stream, command):
    
    picFolder = command.split('_')[1]
    bot.sendMessage(chat_id, str("Retrieving photo from " + picFolder + " live stream."))
    if os.path.exists(mydir + "\\campics\\" + picFolder):
        pass
    else:
        os.mkdir(mydir + "\\campics\\" + picFolder)

    try:
        os.system('C:\\ffmpeg\\bin\\ffmpeg.exe -rtsp_transport tcp -y -i ' + stream + ' -vframes 1 ' + mydir + "\\campics\\" + picFolder +"\\picture.jpg")
        sleep (3.0)
    except:
        bot.sendMessage(chat_id, str("Generating Image Failed!"))
        sleep (1.0)
        bot.sendMessage(chat_id, str("Retrying Request..."))
        imgRequest(chat_id, stream, command)

    bot.sendPhoto (user_001, photo = open(mydir + "\\campics\\" + picFolder +"\\picture.jpg", 'rb'))
    sleep (3.0)
    if os.path.exists(mydir + "\\campics\\" + picFolder +"\\picture.jpg"):
        os.remove(mydir + "\\campics\\" + picFolder +"\\picture.jpg")
    else:
        print("The file does not exist.")


def handle(msg):
    now = datetime.datetime.now()
    localtime = time.asctime( time.localtime(time.time()) )
    chat_id = msg['chat']['id'] # Receiving the message from telegram
    command = msg['text']   # Getting text from the message
    
    print ('Received: ' + "\"" + command + "\"" + " from user " + str(chat_id))
    #print(command)
    #print (chat_id)

    # Comparing the incoming message to send a reply according to it
    if command == '/hi':
        bot.sendMessage (chat_id, str("Hi! Nito"))
        print(mydir)

    elif command == '/cmd':
        bot.sendMessage (chat_id, str("/hi = greeting\n" +
                                    "/Request_Backdoor_Pic\n" +
                                    "/Request_Frontdoor_Pic\n" +
                                    "/Request_Garage_Pic\n" +
                                    "/Request_Driveway_Pic\n" +
                                    "/Request_CornerCam_Pic\n" +
                                    "/Request_Patio_Pic\n" +

                                    "/test\n"
                                    ))
    elif command == '/test':
        testing001()

    elif command == '/Request_Backdoor_Pic':       
        imgRequest(chat_id, backDoorCamStream, command)

    elif command == '/Request_Frontdoor_Pic':       
        imgRequest(chat_id, frontDoorCamStream, command)

    elif command == '/Request_Garage_Pic':       
        imgRequest(chat_id, GarageCamStream, command)

    elif command == '/Request_Driveway_Pic':       
        imgRequest(chat_id, DrivewayCamStream, command)

    elif command == '/Request_CornerCam_Pic':       
        imgRequest(chat_id, CornerCamStream, command)

    elif command == '/Request_Patio_Pic':       
        imgRequest(chat_id, PatioCamStream, command)

bot = telepot.Bot('620301439:AAFkfcA5C3VMw9XDnrVaAvAErt5eg_GTneA')
print (bot.getMe())

MessageLoop(bot, handle).run_as_thread()
print ('Listening....')


CamStreams = ["backdoorCamStream - rtsp://admin:twisted8@192.168.1.110:554/11",
            "CornerCamStream - rtsp://admin:twisted8@192.168.1.117:554/stream0",
            "DrivewayCamStream - rtsp://admin:twisted8@192.168.1.217:554/11",
            "frontDoorCamStream - rtsp://admin:twisted8@192.168.1.113:554/11",
            "GarageCamStream - rtsp://admin:twisted8@192.168.1.122:554/11",
           "PatioCamStream - rtsp://admin:twisted8@192.168.1.157:554/stream0"
           ]

StreamActivity = ["backdoor - 0",
                    "CornerCam - 0",
                    "Driveway - 0",
                    "frontdoor - 0",
                    "Garage - 0",
                    "Patio - 0"
                    ]

while 1:

    sleep(1)

    def picNotifier():
        folderName = os.listdir(mydir + "\\campics")
        num = 0
        for x in folderName:
            #print(folderName[num])
            if int(StreamActivity[num].split(" - ")[1]) == 1:
                print("one if")
                #picFiles = glob.glob(mydir + "\\campics\\folderName[num]\\*.*", recursive=True)
                #for f in picFiles:
                try:
                    #os.remove(f)
                    if os.listdir(mydir + "\\campics\\" + folderName[num]):
                        fileFolder = os.listdir(mydir + "\\campics\\" + folderName[num])
                        os.remove(mydir + "\\campics\\" + folderName[num] + "\\" + fileFolder[0])
                except OSError as e:
                    print(e)
                result = int(StreamActivity[num].split(" - ")[1]) - 1
                StreamActivity[num] = StreamActivity[num].split(" - ")[0] + " - " + str(result)
                num += 1
            elif int(StreamActivity[num].split(" - ")[1]) == 0:
                print("First if")
                #sleep(1.0)
                #num += 1
                if os.listdir(mydir + "\\campics\\" + folderName[num]):
                    print('found it file inside ' + folderName[num])
                    print(os.listdir(mydir + "\\campics\\" + folderName[num]))
                    fileFolder = os.listdir(mydir + "\\campics\\" + folderName[num])
                    print(mydir + "\\campics\\" + folderName[num] + "\\" + fileFolder[0])
                    #picFiles = glob.glob(mydir + "\\campics\\folderName[num]\\*.jpg", recursive=True)
                    #for f in picFiles:
                    try:
                        #os.remove(f)
                        os.system('del /f ' + mydir + "\\campics\\" + folderName[num] + "\\" + fileFolder[0])
                        #os.remove(mydir + "\\campics\\" + folderName[num] + "\\" + fileFolder[0])
                    except OSError as e:
                        print(e)

                    command = "/Request_" + folderName[num] + "_Pic"
                    imgRequest(user_001, CamStreams[num].split(" - ")[1], command) # this should run on seperate thread
                    print(num)
                    StreamActivity[num] = StreamActivity[num].split(" - ")[0] + " - 60"
                    sleep(0.01)
                num += 1
            elif int(StreamActivity[num].split(" - ")[1]) != 0:
                print('else')
                result = int(StreamActivity[num].split(" - ")[1]) - 1
                StreamActivity[num] = StreamActivity[num].split(" - ")[0] + " - " + str(result)
                sleep(0.01)
                print(StreamActivity)
                num += 1
                



        
        

    picNotifier()


    #print('testing loop...') #loop works for detecting


































