from pygame import mixer as mix
mix.init()
def playsong(path):
    mix.music.load(path)
    # r"C:\Users\navee\Downloads\Fear.mp3"
    # python treats backward slash as escape character , to el
    # eliminate we use "r"
    mix.music.play()
    mix.music.set_volume(0.5)
def control(inp):
    if(inp=="Stop"):
        mix.music.stop()
    elif(inp=="Pause"):
        mix.music.pause()
    elif(inp=="Resume"):
        mix.music.unpause()
    
# playsong(r"C:\Users\navee\Downloads\Fear.mp3")

if __name__=="__main":
    print("I am in musicplayer.py")

# while True:
#     inpu=input()
#     control(inpu)



#     # pass -->We dont know the logic but the loop should execute
    #     inp=input("Enter Stop to stop")
    #     if(inp=="Stop"):
    #         mix.music.stop()

