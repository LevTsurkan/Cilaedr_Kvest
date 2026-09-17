import pygame
import os
pygame.mixer.init()
import time
import random
location = 'prihogaya'   # Локация, изначально она прихожая
propusk = True           # Пропуск, изначально он есть
key35O = True            # Наличие ключей от 3 и 5 этажей и отвертки в комнате охраны
keyO = True              # Наличие ключа от комнаты с боссом на 5 этаже
key1O = True             # Наличие ключа от комнаты охраны на лавочке
key5 = False             # ключ от 5 этажа, изначально его нет
key3 = False             # ключ от 3 этажа, изначально его нет
key = False              # ключ от комнаты с боссом, изначально его нет
otvertka = False         # отвертка, изначально ее нет и она не пригодилась в текущей версии игры
key1 = False             # ключ от комнаты охраны, изначально его нет
obyasnitelnaya = 0       # кол-во объяснительных, изначально 0
e=1                      # этаж, нужен для лестницы
milo=0                   # мыло, сначала его нет, потом будет только бутылка, потом заполненая бутылка, потом она будет уже не нужна
HP=100                   # HP персонажа, изначально 100
HPM=100                  # HP монстра, изначально 100
eda=False                # Еда из столовой, изначально у персонажа ее нет
zavhoz="человек"         # Завхоз, изначально человек, но его можно превратить в жабу
ruki='чисты'             # Руки, изначально чисты, но могут перепачкаться в крови и придется мыть их в туалете
lavochka=True            # Лавочка, сначала нормальная, потом можно сломать
cat=0                    # Кот, сначала сидит на 5 этаже, потом на 2 этаже, потом вовсе уходит из игры
keyS=False               # ключ от столовой, изначально его нет
r=0                      # Запускать ли музыку при входе на третй этаж
def start_background_music():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    sound_file = os.path.join(script_dir, "фоновая музыка.mp3")
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play(-1)
def prihogaya():
    global location, propusk
    print('Вы находитесь в прихожей.')
    print('Вы подходите к турникетам, и на вас подозрительно смотрит охранница.')
    print('Что вы сделаете?')
    print('1: приложить пропуск и пройти через турникет.')
    print('2: подойти к охраннице и сказать, что вы забыли пропуск.')
    c = input().strip()  
    if c == '1':
            if propusk:
                print('Вы прикладываете пропуск, турникет щёлкает, и вы проходите на первый этаж.')
                location='etag1'
            else:
                print('Но у вас нет пропуска!')
                a=random.randint(1,2)
                if a==2:
                    time.sleep(2)
                    print('Но тут охранница отворачивается и локтем задевает кнопку автоматического открытия турникета и вы проходите на первый этаж.')
                    location='etag1'
                else:
                    location='prihogaya'
    elif c == '2':
            print('Вы подходите к охраннице и говорите, что забыли пропуск.')
            print('Охранница вздыхает: "Ну ладно, проходите, но больше так не делайте". Вы проходите на первый этаж.')
            location='etag1'
    else:
            print('Неверный ввод. Выберите 1 или 2.')
            location='prihogaya'  
def etag1():
    global location, milo, zavhoz, ruki, key1, keyS
    print('Вы на первом этаже. Здесь как обычно многолюдно, но не очень, и все немного притихшие.')
    print('Что вы сделаете?')
    print('1: пойдете в 105 кабинет.')
    print('2: пойдете в комнату охраны.')
    print('3: пойдете на лестницу.')
    print('4: пойдете в туалет.')
    print('5: пойдете к куллерам.')
    if keyS: print('6: пойдете в столовую')
    c = input().strip()
    if c == '1':
        print("Вы заходите в 105 кабинет.")
        location='c105'
    elif c == '2':
        if key1:
            print('Комната охраны закрыта, но вы отпираете ее ключом и заходите.')
            key1 = False
            location='ohrana'
        elif (not key1) and (not key1O):
            print('Вы заходите в комнату охраны.')
            location='ohrana'
        else:
            print('Комната охраны закрыта.')
            location='etag1'
    elif c == '3':
        print('Вы заходите на лестницу.')
        location='lestnica'
    elif c == '4':
        print("Вы заходите в туалет.")
        location='tualet'
    elif c == '5':
        print("Вы подходите к куллеру. В него не вставлена баклажка с водой.")
        if milo==2:
            print('Что вы сделаете?')
            print('1: зальете в куллер мыло из колбы с надписью "Жи кое мы о".')
            print('2: вернетесь на 1 этаж.')
            c = input().strip()
            l=0
            while l!=1:
                if c=='1':
                    print("Вы заливаете мыло и оно пачкает вам руки. Вы отходите и ждете, пока что-нибудь произойдет.")
                    ruki="в мыле"
                    print("Через некоторое время к куллеру подходит завхоз и ставит на него баклажку с водой и пьет оттуда.Он начинает задыхаться, его глаза закатываются и он превращается в жабу, сшибая баклажка своим телом.")
                    print('''
         o  o   o  o
         |\/ \^/ \/|
         |,-------.|
       ,-.(|)   (|),-.
       \_*._ ' '_.* _/
        /`-.`--' .-'\
   ,--./    `---'    \,--.
   \   |(  )     (  )|   /
    \  | ||       || |  /
     \ | /|\     /|\ | /
     /  \-._     _,-/  \
    //| \\  `---'  // |\\
   /,-.,-.\       /,-.,-.\
  o   o   o      o   o    o

                    ''')
                    zavhoz='жаба'
                    milo=3
                    print("Вы возвращаетесь на 1 этаж.")
                    location='etag1'
                    l=1
                elif c=='2':
                    print("Вы возвращаетесь на 1 этаж.")
                    location='etag1'
                    l=1
                else:
                    print('Неверный ввод. Выберите 1 или 2')
        else:
            print("По этому вы выходите.")
            location='etag1'
    elif c=='6' and keyS:
        print("Вы открываете столовую ключом и входите.")
        location='stolovoya'
    else:
        print('Неверный ввод. Выберите цифру')
        location='etag1'
def stolovaya():
    global zavhoz, location, eda
    print("Вы в столовой.")
    if zavhoz=="человек":
        print("Завхоз выгоняет вас отсюда.")
        location='etag1'
    elif not eda:
        print("Вы забираете еду под злобное кваканье жабы-завхоза и выходите.")
        eda=True
        location='etag1'
    else:
        print("Здесь ничего нет и вы выходите.")
        location='etag1'
def c105():
    global location, obyasnitelnaya
    print('Вы в 105 кабинете. За столом сидит Инга Александровна.')
    a=random.randint(1,2)
    if a == 1:
        time.sleep(1)
        print('Инга Александровна: "А ну вон отсюда! Тебя сюда никто не приглашал! Пиши объяснительную!!!!"')
        print("Вы пишете объяснительную и поникшие выходите из 105 кабинета.")
        obyasnitelnaya=obyasnitelnaya+1
        if obyasnitelnaya==3:
            location='end'
            print("Вы исключены из школы!")
        else:
            location='etag1'
    else:
        print("Она не обращает на тебя внимания. В кабинете нет ничего интересного. Ты возвращаешься обратно.")
        location='etag1'
def ohrana():
    global location, key35O, key3, key5, otvertka
    print("Вы в комнате охраны.")
    if key35O:
        print("На столе лежат ключи от 3 этажа, ключи от 5 этажа и отвертка.")
        print('Что вы сделаете?')
        print('1: возьмете ключи с отверткой и уйдете.')
        print('2: уйдете.')
        c = input().strip()
        if c == '1':
            print("Вы хватаете ключи, отвертку и бесшумно выходите.")
            key3=True
            key5=True
            otvertka=True
            key35O=False
            location='etag1'
        elif c == '2':
            print("Вы выходите.")
            location='etag1'
        else:
            print('Неверный ввод. Выберите 1 или 2.')
            location='ohrana'
    else:
        print("Вы не находите здесь ничего интересного и выходите.")
        location='etag1'
def lestnica():
    global location, e, key3, key5, key35O
    if e==1:
        print("Вы на лестничной площадке первого этажа.")
        print('Что вы сделаете?')
        print('1: зайдете на 1 этаж.')
        print('2: пойдете вверх.')
        print('3: выйдете на задний двор.')
        c = input().strip()
        if c == '1':
            print("Вы заходите на 1 этаж.")
            location='etag1'
        elif c == '2':
            print("Вы идете вверх.")
            e=2
            location='lestnica'
        elif c == '3':
            print("Вы выходите во двор, и дверь за вами захлопывается.")
            location='zadniy_dvor'
        else:
            print('Неверный ввод. Выберите цифру.')
            location='lestnica'
    if e==2 or e==4:
            print(f"Вы на лестничной площадке {e} этажа.")
            print('Что вы сделаете?')
            print(f'1: зайдете на {e} этаж.')
            print('2: пойдете вверх.')
            print('3: пойдете вниз.')
            c = input().strip()
            if c == '1':
                    print(f"Вы заходите на {e} этаж.")
                    location=f'etag{e}'
            elif c == '2':
                    print("Вы идете вверх.")
                    e=e+1
                    location='lestnica'
            elif c == '3':
                    print("Вы идете вниз. ")
                    e=e-1
                    location='lestnica'
            else:
                    print('Неверный ввод. Выберите 1 или 2.')
                    location='lestnica'
    if e==3:
            print("Вы на лестничной площадке 3 этажа.")
            print('Что вы сделаете?')
            print('1: зайдете на 3 этаж.')
            print('2: пойдете вверх.')
            print('3: пойдете вниз.')
            c = input().strip()
            if c == '1':
                    if key3:
                        print("Дверь заперта, но вы открываете ее ключом и заходите на 3 этаж.")
                        key3=False
                        location='etag3'
                    elif (not key3) and (not key35O):
                        print("Вы заходите на 3 этаж.")
                        location='etag3'
                    else:
                        print("Дверь заперта.")
                        location='lestnica'
            elif c == '2':
                    print("Вы идете вверх.")
                    e=e+1
                    location='lestnica'
            elif c == '3':
                    print("Вы идете вниз. ")
                    e=e-1
                    location='lestnica'
            else:
                    print('Неверный ввод. Выберите 1 или 2.')
                    location='lestnica'
    if e==5:
            print("Вы на лестничной площадке 5 этажа.")
            print('Что вы сделаете?')
            print('1: зайдете на 5 этаж.')
            print('2: пойдете вниз.')
            c = input().strip()
            if c == '1':
                    if key5:
                        print("Дверь заперта, но вы открываете ее ключом и заходите на 5 этаж.")
                        key5=False
                        location='etag5'
                    elif (not key3) and (not key35O):
                        print("Вы заходите на 5 этаж.")
                        location='etag5'
                    else:
                        print("Дверь заперта.")
                        location='lestnica'
            elif c == '2':
                    print("Вы идете вниз. ")
                    e=e-1
                    location='lestnica'
            else:
                    print('Неверный ввод. Выберите 1 или 2.')
                    location='lestnica'
def zadniy_dvor():
    global location, lavochka, key1, key1O, zavhoz, ruki
    print("Вы на заднем дворе.")
    print('Что вы сделаете?')
    print('1: пойдете к выходу из школы, во двор.')
    print('2: пойдете к лавочкам.')
    c = input().strip()
    if c == '1':
        location='dvor'
    elif c == '2':
        print("Вы подходите к лавочкам.")
        if key1O:
            print("На лавочке лежат ключи от комнаты охраны.")
            print('Что вы сделаете?')
            print('1: заберете ключи и выйдете на задний двор.')
            print('2: выйдете на задний двор')
            l=0
            while l!=1:
                c = input().strip()
                if c == '1':
                    print('Вы забираете ключи и уходите.')
                    key1=True
                    key1O=False
                    location='zadniy_dvor'
                    l=1
                elif c == '2':
                    print("Вы заходите на задний двор.")
                    location='zadniy_dvor'
                    l=1
                else:
                    print('Неверный ввод. Выберите цифру.')
        elif not key1O:
            if lavochka:
                print('Что вы сделаете?')
                print('1: сломаете лавочку.')
                print('2: выйдете на задний двор.')
                
                l=0
                while l!=1:
                    c = input().strip()
                    if c == '1':
                        print('Вы с размаху бьете скамейку и она ломается. Из скамейки вырывается языческий демон и улетает с пронзительным визгом. В этом визге вы различаете: "Спасибо!".')
                        print('Вы испачкали руки своей кровью.')
                        lavochka=False
                        ruki="в крови"
                        location='zadniy_dvor'
                        l=1
                    elif c == '2':
                        print("Вы заходите на задний двор.")
                        location='zadniy_dvor'
                        l=1
                    else:
                        print('Неверный ввод. Выберите цифру.')
            else:
                print("Вы любуетесь сломаной лавочкой, из которой вы освободили языческого демона.")
                if a:=random.randint(1,4)==1 and zavhoz=="жив":
                    time.sleep(1)
                    print("И тут приходит завхоз и направляется к лавочке с целью починить ее.")
                    time.sleep(1)
                    print('Что вы сделаете?')
                    print('1: нападете на завхоза.')
                    print('2: выйдете на задний двор.')
                    c = input().strip()
                    l=0
                    while l!=1:
                        c = input().strip()
                        if c == '1':
                            print('Вы с размаху бьете завхоза и он убегает, а вы выходите.')
                            print('Вы испачкали руки кровью завхоза.')
                            ruki="в крови з"
                            lavochka=False
                            location='zadniy_dvor'
                            l=1
                        elif c == '2':
                            print("Вы заходите на задний двор, а завхоз чинит лавочку.")
                            lavochka=True
                            location='zadniy_dvor'
                            l=1
                        else:
                            print('Неверный ввод. Выберите 1 или 2.')
                else:
                    print("Вы идете на задний двор.")
                    location='zadniy_dvor'
    else:
        print('Неверный ввод. Выберите 1 или 2.')
        location='zadniy_dvor'
def dvor():
    global location
    print("Вы во дворе.")
    print('''
                 _ _.-'`-._ _
                ;.'________'.;
     _________n.[____________].n_________
    |""_""_""_""||==||==||==||""_""_""_""]
    |"""""""""""||..||..||..||"""""""""""|
    |LI LI LI LI||LI||LI||LI||LI LI LI LI|
    |.. .. .. ..||..||..||..||.. .. .. ..|
    |LI LI LI LI||LI||LI||LI||LI LI LI LI|
    |.. .. .. ..||..||..||..||.. .. .. ..|
    |LI LI LI LI||LI||LI||LI||LI LI LI LI|
    |.. .. .. ..||..||..||..||.. .. .. ..|
    |LI LI LI LI||LI||[]||LI||LI LI LI LI|
 ,,;;,;;;,;;;,;;;,;;;,;;;,;;;,;;,;;;,;;;,;;,,
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
''')
    print('Что вы сделаете?')
    print('1: войдете в школу.')
    print('2: пойдете на задний двор.')
    c = input().strip()
    if c== '1':
            print("Вы поднимаетесь по лестнице и входите в школу.")
            location='prihogaya'
    elif c == '2':
            print("Вы идете на задний двор.")
            location='zadniy_dvor'
    else:
            print('Неверный ввод. Выберите 1 или 2.')
            location='dvor'
def etag2():
    global location
    print("Вы на 2 этаже. Здесь никогого нет.")
    if cat>0: print("Дверь 201 кабинета открыта.")
    print('Что вы сделаете?')
    print('1: попробуете двери классов, вдруг какая-то открыта.')
    print('2: выйдете на лестницу.')
    if cat>0: print('3: пойдете в 201.')
    c = input().strip()
    if c== '1':
            print("Все двери закрыты, кроме двери в учительскую, вы заходите внутрь.")
            location='uchitelskaya'
    elif c == '2':
            print("Вы выходите на лестницу.")
            location='lestnica'
    elif c == '3' and cat>0:
            print("Вы заходите в 201 кабинет.")
            location='c201'
    else:
            print('Неверный ввод. Выберите цифру.')
            location='etag2'
def c201():
    global location, cat, keyS, zavhoz, eda
    print("Вы в 201 кабинете.")
    if cat==1:
        print("Все парты сдвинуты к стене, а за учительским столом сидит Кот.")
        print("Здравствуй, Двуногий! Что тебе нужно?")
        print('1: "Я просто пришел осмотреться."')
        print('2: "Я просто пришел поздороваться. Привет, Кот!"')
        if zavhoz=='жаба': print('3: "Ты можешь превратить завхоза обратно в человека?"')
        if eda: print('4: "Я пришел покормить тебя едой из столовой."')
        c = input().strip()
        if c== '1':
                print('Кот: "А, ну пока!"')
                print('Вы выходите на 2 этаж.')
                location='etag2'
        elif c == '2':
                print('Кот: "Ты очень вежливый, держи ключ от столовой."')
                print('Вы выходите на 2 этаж.')
                keyS=True
                location='etag2'
        elif c== '3':
                print('Кот: "Могу. Все уже готово." Кот хитро ухмыляется и смотрит на тебя.')
                zavhoz="человек"
                print('Вы выходите на 2 этаж.')
                location='etag2'
        elif c== '4':
                print('Кот: "Мяу, спасибо! Пока!" Кот исчезает с громким одобрительным "Мяууууууууууу!"')
                cat=2
                eda=False
                print('Вы выходите на 2 этаж.')
                location='etag2'
        else:
                print('Неверный ввод. Выберите цифру.')
                location='c201'
    else:
        print("Здесь ничего нет. И вы выходите.")
        location="etag2"
def uchitelskaya():
    global location
    print("Вы в учительской. Здесь никого нет. Картина на стене сдвинута, и за ней виднеется проход в 207 кабинет(этот кабинет лаборантская).")
    print('Что вы сделаете?')
    print('1: Зайдете в 207 кабинет.')
    print('2: выйдете на 2 этаж.')
    c = input().strip()
    if c== '1':
            print("Вы заходите в 207 кабинет.")
            location='c207'
    elif c == '2':
            print("Вы выходите на 2 этаж.")
            location='etag2' 
    else:
            print('Неверный ввод. Выберите 1 или 2.')
            location='uchitelskaya'
def c207():
    global location, obyasnitelnaya, e
    print("Вы в 207 кабинете.")
    if a:=random.randint(1,4)==1:
        print("За партой стоит Олег Сергеевич и что-то делает за компьютером.")
        time.sleep(1)
        print('Он поднимает на тебя глаза и кричит:"Что ты тут делаешь! Иди пиши объяснительную!')
        print('Он отводит тебя в 105 кабинет и ты пишешь объяснительную.')
        e=1
        obyasnitelnaya=obyasnitelnaya+1
        if obyasnitelnaya==3:
            print("Вы исключены из школы!")
            location='end'
        else:
            print("Вы поникшие выходите из 105 кабинета.")
            location='etag1'
    else:
        print("На парте лежит компьютер. Вы заглядываете в него. Там ваши оценки по русскому.")
        print("Вдруг компьютер выключается вы в испуге выбегаете в учительскую, а из нее на второй этаж.")
        location='etag2'
def etag3():
    global location, r, key
    if r==1: start_background_music()
    print("Вы на 3 этаже. Из единственной двери доносятся звуки похожие на дыхание.")
    print('Что вы сделаете?')
    print('1: зайдете в эту дверь.')
    print('2: выйдете на лестницу.')
    c = input().strip()
    if c== '1':
            if key==True:
                print("Дверь заперта, но вы открываете ее большим серебряным ключом и входите.")
                location='boss'
            elif not key and not keyO:
                print("Вы открываете дверь, но за ней стена.")
                location='etag3'
            else:
                print("Дверь заперта.")
                location='etag3'
    elif c == '2':
            print("Вы выходите на лестницу.")
            location='lestnica' 
    else:
            print('Неверный ввод. Выберите 1 или 2.')
            location='etag3'
def boss():
    global location, otvertka, HP, HPM, r
    pygame.mixer.music.pause()
    script_dir = os.path.dirname(os.path.abspath(__file__))
    sound_file = os.path.join(script_dir, "босс.mp3")
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play(-1)
    r=1
    print("Вы в огромной темной комнате. Поначалу вы ничего не различаете, но ваши глазы привыкают к темноте и вы видите...")
    time.sleep(2)
    print("...ужасного монстра похожего на большую пчелу, но у него клюв, как у птицы, тело покрыто шерстью, a зубы - как у собаки - пчелоптицепеса!")
    print("Пчелоптицепес нападает на вас и бьет в ногу.")
    HP=HP-15
    if HP<1:
        print("Смерть.")
        print("Монстр убил вас.")
        location='end'
        return
    print("Ваше НP: ", HP)
    print("Что вы сделаете?")
    print('1: ударите монстра в лапу.')
    print('любая другая кнопка: ударите монстру в клюв.')
    c = input().strip()
    if c== '1':
            print("Вы бьете монстра в лапу и он взвывает в ужасе.")
            HPM=HPM-25
            print("НР монстра: ", HPM)
    else:
            print("Вы бьете монстра в клюв. Это оказалось слабое место и птица падает.")
            HPM=HPM-50
            print("НР монстра: ", HPM)
            print("Вы пользуетесь тем, что монстр в обмороке и сьедаете булочку. Ваше НР: ", HP+10)
            HP=HP+10
            print("Монстр медленно встает и злобно смотрит на вас.")
    print("Пчелоптицепес нападает на вас и бьет в руку.")
    HP=HP-25
    if HP<1:
        print("Смерть.")
        print("Монстр убил вас.")
        location='end'
        return
    print("Ваше НP: ", HP)
    print("Что вы сделаете?")
    print('1: ударите монстра в палец на ноге.')
    print('любая другая кнопка: ударите монстра в глаз.')
    c = input().strip()
    if c== '1':
            print("Вы бьете монстра в палец и он сгибается от боли.")
            HPM=HPM-50
            if HPM<1:
                pygame.mixer.music.pause()
                print("Вы убили монстра.")
                print("Вы спускаетесь на 1 этаж и все благодарят вас и подкидывают к потолку. Вы выиграли.")
                location='end'
                return
            print("НР монстра: ", HPM)
    else:
            print("Вы бьете монстра в глаз.")
            HPM=HPM-25
            print("НР монстра: ", HPM)
    print("Пчелоптицепес нападает на вас и бьет в голову.")
    print("Смерть.")
    print("Монстр убил вас.")
    location='end'
    pygame.mixer.music.pause()
def etag4():
    global location
    print("Вы на 4 этаже. Здесь никого нет. Дверь в 401 кабинет открыта.")
    print('Что вы сделаете?')
    print('1: зайдете в 401 кабинет.')
    print('2: выйдете на лестницу.')
    c = input().strip()
    if c== '1':
            print("Вы заходите в 401 кабинет.")
            location='c401'
    elif c == '2':
            print("Вы выходите на лестницу.")
            location='lestnica' 
    else:
            print('Неверный ввод. Выберите 1 или 2.')
            location='etag4'
def c401():
    global location, milo
    print('Вы в 401 кабинете. Здесь никого нет.')
    if milo==0:
        print('На одной из парт лежит колба с надписью "Жи кое мы о".')
        print('Что вы сделаете?')
        print('1: выйдете на 4 этаж.')
        print('2: заберете колбу и выйдете.')
        c = input().strip()
        if c== '1':
                print("Вы выходите на 4 этаж.")
                location='etag4'
        elif c == '2':
                print("Вы забираете колбу и выходите.")
                milo=1
                location='etag4' 
        else:
                print('Неверный ввод. Выберите 1 или 2.')
                location='c401'
    print("Вы выходите, потому что тут ничего нет.")
    location='etag4'
def etag5():
    global location, key, keyO, propusk, cat
    print("Вы на 5 этаже. В углу стоит пустая кошачья миска и упаковка кошачьего корма.")
    if cat==0: print("Здесь бегает и громко мяучет кот.")
    print('Что вы сделаете?')
    print('1: выйдете на лестницу.')
    print('2: осмотритесь.')
    if cat==0: print('3: поймаете кота.')
    c = input().strip()
    if c== '1':
            print("Вы выходите на лестницу.")
            location='lestnica'
    elif c=='2':
            if keyO==True:
                print('Вы видите коробку с надписью "Вставь пропуск".')
                print('Что вы сделаете?')
                print('1: вставите пропуск. ')
                print('2: выйдете на лестницу.')
                l=0
                while l!=1:
                    c = input().strip()
                    if c == '1':
                        print('Вы вставляете пропуск в коробку и достаете большой, резной, серебряный ключ, похожий на лапу собаки, но с крыльями птицы и лапками пчелы.')
                        key=True
                        propusk=False
                        keyO=False
                        location='etag5'
                        l=1
                    elif c == '2':
                        print("Вы выходите на лестницу.")
                        location='lestnica'
                    else:
                        print('Неверный ввод. Выберите 1 или 2.')
    elif cat==0 and c == '3':
            print('Вы ловите кота и он перестает мяукать. Кот: "Зачем ты меня поймал?"')
            print('''           
       \`-._           __
        \\  `-..____,.'  `.
         :`.         /    \`.
         :  )       :      : \
          ;'        '   ;  |  :
          )..      .. .:.`.;  :
         /::...  .:::...   ` ;
         ; _ '    __        /:\
         `:o>   /\o_>      ;:. `.
        `-`.__ ;   __..--- /:.   \
        === \_/   ;=====_.':.     ;
         ,/'`--'...`--....        ;
              ;                    ;
            .'                      ;
          .'                        ;
        .'     ..     ,      .       ;
       :       ::..  /      ;::.     |
      /      `.;::.  |       ;:..    ;
     :         |:.   :       ;:.    ;
     :         ::     ;:..   |.    ;
      :       :;      :::....|     |
      /\     ,/ \      ;:::::;     ;
    .:. \:..|    :     ; '.--|     ;
   ::.  :''  `-.,,;     ;'   ;     ;
.-'. _.'\      / `;      \,__:      \
`---'    `----'   ;      /    \,.,,,/
                   `----`              ''')
            print('Что вы сделаете?')
            print('1: бросите кота. ')
            print('2: покормите кота.')
            print('3: откусите кота.')
            l=0
            while l!=1:
                c = input().strip()
                if c == '1':
                    print('Вы бросаете кота.')
                    location='etag5'
                    l=1
                elif c == '2':
                    print("Вы опускаете кота и насыпаете ему корм.")
                    print('Кот съедает весь корм и говорит:"Спасибо, кстати я волшебный кот! Мяууууу!"')
                    print('Кот исчезает с громким одобрительным "Мяууууу!"')
                    cat=1
                    location='etag5'
                    l=1
                elif c == '3':
                    print("Вы кусаете кота. Вы подавились шерстью кота и умерли, ибо нефиг жрать кота!!!")
                    location='end'
                else:
                    print('Неверный ввод. Выберите 1 или 2.')
    else:
            print('Неверный ввод. Выберите цифру.')
            location='etag5'
def tualet():
    global location, milo, ruki
    print("Вы в туалете.")
    print('Что вы сделаете?')
    print('1: выйдете на 1 этаж.')
    print('2: помоете руки и выйдете.')
    c = input().strip()
    if c== '1':
                print("Вы выходите на 1 этаж.")
                location='etag1'
    elif c == '2':
                print("Вы моете руки. Ваши руки чисты.")
                ruki='чисты'
                if milo==1:
                    print('Вы набираете мыло в колбу с надписью "Жи кое мы о".')
                    milo=2
                print("Вы выходите из туалета.")
                location='etag1'
    else:
                print('Неверный ввод. Выберите 1 или 2.')
                location='tualet'
