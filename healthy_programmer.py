from pygame import mixer
import datetime

water_music="water.mp3"
eyes_music="eyes.mp3"
physical_music="physical.mp3"

water=30
eyes=40
physical=45

t_water,t_eyes,t_physical=0,0,0

t0=datetime.datetime.now().minute

with open("waterdrank.txt", mode="a") as f:
    x = str(datetime.datetime.now()) + "\n"
    f.write(x)

with open("eyesdone.txt", mode="a") as f:
    x = str(datetime.datetime.now()) + "\n"
    f.write(x)

with open("physicaldone.txt", mode="a") as f:
    x = str(datetime.datetime.now()) + "\n"
    f.write(x)

while True:
    t_water+=(water+t0)
    t_eyes+=(eyes+t0)
    t_physical+=(physical+t0)


    if t_water>60: t_water-=60
    if t_eyes>60: t_eyes-=60
    if t_physical>60: t_physical-=60

    water_record=0
    eyes_record=0
    physical_record=0

    while True:

        with open("waterdrank.txt", mode="r") as f:
            lst = f.readlines()[-1].split()[1].split(':')[1]
            water_record = int(lst)

        with open("eyesdone.txt", mode="r") as f:
            lst = f.readlines()[-1].split()[1].split(':')[1]
            eyes_record = int(lst)

        with open("physicaldone.txt", mode="r") as f:
            lst = f.readlines()[-1].split()[1].split(':')[1]
            physical_record = int(lst)

        done_water=0
        done_eyes=0
        done_physical=0

        while t_water==datetime.datetime.now().minute or abs(water_record-datetime.datetime.now().minute)>water:
            mixer.init()

            mixer.music.load(water_music)
            mixer.music.set_volume(0.5)
            mixer.music.play(-1)

            if input("Have You drank the water").lower() == "drank":
                with open("waterdrank.txt",mode="a") as f:
                    x=str(datetime.datetime.now())+"\n"
                    f.write(x)
                mixer.music.stop()
                t_water+=water
                t0=0
                done_water=1
            else: print("Try Again")

            if done_water==1:
                break

        while t_eyes==datetime.datetime.now().minute or abs(eyes_record-datetime.datetime.now().minute)>eyes:
            mixer.init()
            mixer.music.load(eyes_music)
            mixer.music.set_volume(0.5)
            mixer.music.play(-1)

            if input("Are you done with your eyes").lower() == "done":
                with open("eyesdone.txt",mode="a") as f:
                    x=str(datetime.datetime.now())+"\n"
                    f.write(x)
                mixer.music.stop()
                t_water+=water
                t0=0
                done_eyes=1
            else: print("Try Again")

            if done_eyes==1:
                break

        while t_physical==datetime.datetime.now().minute or abs(physical_record-datetime.datetime.now().minute)>physical:
            mixer.init()
            mixer.music.load(physical_music)
            mixer.music.set_volume(0.5)
            mixer.music.play(-1)

            if input("Have You done your excerise").lower() == "done":
                with open("physicaldone.txt",mode="a") as f:
                    x=str(datetime.datetime.now())+"\n"
                    f.write(x)
                mixer.music.stop()
                t_water+=water
                t0=0
                done_physical=1
            else: print("Try Again")

            if done_physical==1:
                break
