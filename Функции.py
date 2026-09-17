import pygame
import os
pygame.mixer.init()
import time
import random
class GameState:
    def __init__(self):
        self.r = 0
        self.location = 'prihogaya'
        self.e = 1                  
        self.propusk = True
        self.key35O = True
        self.keyO = True
        self.key1O = True
        self.key5 = False
        self.key3 = False
        self.key = False
        self.otvertka = False
        self.key1 = False
        self.keyS = False
        self.obyasnitelnaya = 0
        self.milo = 0              # 0 — нет, 1 — колба, 2 — с мылом, 3 — использовано
        self.eda = False
        self.lavochka = True
        self.cat = 0               # 0 — бегает, 1 — в 201, 2 — ушёл
        self.HP = 100
        self.HPM = 100
        self.zavhoz = "человек"
        self.ruki = "чисты"
def start_background_music():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    sound_file = os.path.join(script_dir, "фоновая музыка.mp3")
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play(-1)
def prihogaya(state: GameState):
    print('Вы находитесь в прихожей.')
    print('Вы подходите к турникетам, и на вас подозрительно смотрит охранница.')
    print('Что вы сделаете?')
    print('1: приложить пропуск и пройти через турникет.')
    print('2: подойти к охраннице и сказать, что вы забыли пропуск.')
    c = input().strip()  
    if c == '1':
            if state.propusk:
                print('Вы прикладываете пропуск, турникет щёлкает, и вы проходите на первый этаж.')
                state.location='etag1'
            else:
                print('Но у вас нет пропуска!')
                a=random.randint(1,2)
                if a==2:
                    time.sleep(2)
                    print('Но тут охранница отворачивается и локтем задевает кнопку автоматического открытия турникета и вы проходите на первый этаж.')
                    state.location='etag1'
                else:
                    state.location='prihogaya'
    elif c == '2':
            print('Вы подходите к охраннице и говорите, что забыли пропуск.')
            print('Охранница вздыхает: "Ну ладно, проходите, но больше так не делайте". Вы проходите на первый этаж.')
            state.location='etag1'
    else:
            print('Неверный ввод. Выберите 1 или 2.')
            state.location='prihogaya'  
def etag1(state: GameState):
    print('Вы на первом этаже. Здесь как обычно многолюдно, но не очень, и все немного притихшие.')
    print('Что вы сделаете?')
    print('1: пойдете в 105 кабинет.')
    print('2: пойдете в комнату охраны.')
    print('3: пойдете на лестницу.')
    print('4: пойдете в туалет.')
    print('5: пойдете к куллерам.')
    if state.keyS: print('6: пойдете в столовую')
    c = input().strip()
    if c == '1':
        print("Вы заходите в 105 кабинет.")
        state.location='c105'
    elif c == '2':
        if state.key1:
            print('Комната охраны закрыта, но вы отпираете ее ключом и заходите.')
            state.key1 = False
            state.location='ohrana'
        elif (not state.key1) and (not state.key1O):
            print('Вы заходите в комнату охраны.')
            state.location='ohrana'
        else:
            print('Комната охраны закрыта.')
            state.location='etag1'
    elif c == '3':
        print('Вы заходите на лестницу.')
        state.location='lestnica'
    elif c == '4':
        print("Вы заходите в туалет.")
        state.location='tualet'
    elif c == '5':
        print("Вы подходите к куллеру. В него не вставлена баклажка с водой.")
        if state.milo==2 and state.zavhoz=="человек":
            print('Что вы сделаете?')
            print('1: зальете в куллер мыло из колбы с надписью "Жи кое мы о".')
            print('2: вернетесь на 1 этаж.')
            l=0
            while l!=1:
                c = input().strip()
                if c=='1':
                    print("Вы заливаете мыло и оно пачкает вам руки. Вы отходите и ждете, пока что-нибудь произойдет.")
                    state.ruki="в мыле"
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
                    state.zavhoz='жаба'
                    print("Вы возвращаетесь на 1 этаж.")
                    state.location='etag1'
                    l=1
                elif c=='2':
                    print("Вы возвращаетесь на 1 этаж.")
                    state.location='etag1'
                    l=1
                else:
                    print('Неверный ввод. Выберите 1 или 2')
        else:
            print("По этому вы выходите.")
            state.location='etag1'
    elif c=='6' and state.keyS:
        print("Вы открываете столовую ключом и входите.")
        state.location='stolovaya'
    else:
        print('Неверный ввод. Выберите цифру')
        state.location='etag1'
def stolovaya(state: GameState):
    print("Вы в столовой.")
    if state.zavhoz=="человек":
        print("Завхоз выгоняет вас отсюда.")
        state.location='etag1'
    elif not state.eda:
        print("Вы забираете еду под злобное кваканье жабы-завхоза и выходите.")
        state.eda=True
        state.location='etag1'
    else:
        print("Здесь ничего нет и вы выходите.")
        state.location='etag1'
def c105(state: GameState):
    print('Вы в 105 кабинете. За столом сидит Инга Александровна.')
    a=random.randint(1,2)
    if a == 1:
        time.sleep(1)
        print('Инга Александровна: "А ну вон отсюда! Тебя сюда никто не приглашал! Пиши объяснительную!!!!"')
        print("Вы пишете объяснительную и поникшие выходите из 105 кабинета.")
        state.obyasnitelnaya=state.obyasnitelnaya+1
        if state.obyasnitelnaya==3:
            state.location='end'
            print("Вы исключены из школы!")
        else:
            state.location='etag1'
    else:
        print("Она не обращает на тебя внимания. В кабинете нет ничего интересного. Ты возвращаешься обратно.")
        state.location='etag1'
def ohrana(state: GameState):
    print("Вы в комнате охраны.")
    if state.key35O:
        print("На столе лежат ключи от 3 этажа, ключи от 5 этажа и отвертка.")
        print('Что вы сделаете?')
        print('1: возьмете ключи с отверткой и уйдете.')
        print('2: уйдете.')
        c = input().strip()
        if c == '1':
            print("Вы хватаете ключи, отвертку и бесшумно выходите.")
            state.key3=True
            state.key5=True
            state.otvertka=True
            state.key35O=False
            state.location='etag1'
        elif c == '2':
            print("Вы выходите.")
            state.location='etag1'
        else:
            print('Неверный ввод. Выберите 1 или 2.')
            state.location='ohrana'
    else:
        print("Вы не находите здесь ничего интересного и выходите.")
        state.location='etag1'
def lestnica(state: GameState):
    if state.e==1:
        print("Вы на лестничной площадке первого этажа.")
        print('Что вы сделаете?')
        print('1: зайдете на 1 этаж.')
        print('2: пойдете вверх.')
        print('3: выйдете на задний двор.')
        c = input().strip()
        if c == '1':
            print("Вы заходите на 1 этаж.")
            state.location='etag1'
        elif c == '2':
            print("Вы идете вверх.")
            state.e=2
            state.location='lestnica'
        elif c == '3':
            print("Вы выходите во двор, и дверь за вами захлопывается.")
            state.location='zadniy_dvor'
        else:
            print('Неверный ввод. Выберите цифру.')
            state.location='lestnica'
    elif state.e==2 or state.e==4:
            print(f"Вы на лестничной площадке {state.e} этажа.")
            print('Что вы сделаете?')
            print(f'1: зайдете на {state.e} этаж.')
            print('2: пойдете вверх.')
            print('3: пойдете вниз.')
            c = input().strip()
            if c == '1':
                    print(f"Вы заходите на {state.e} этаж.")
                    state.location=f'etag{state.e}'
            elif c == '2':
                    print("Вы идете вверх.")
                    state.e=state.e+1
                    state.location='lestnica'
            elif c == '3':
                    print("Вы идете вниз. ")
                    state.e=state.e-1
                    state.location='lestnica'
            else:
                    print('Неверный ввод. Выберите 1 или 2.')
                    state.location='lestnica'
    elif state.e==3:
            print("Вы на лестничной площадке 3 этажа.")
            print('Что вы сделаете?')
            print('1: зайдете на 3 этаж.')
            print('2: пойдете вверх.')
            print('3: пойдете вниз.')
            c = input().strip()
            if c == '1':
                    if state.key3:
                        print("Дверь заперта, но вы открываете ее ключом и заходите на 3 этаж.")
                        state.key3=False
                        state.location='etag3'
                    elif (not state.key3) and (not state.key35O):
                        print("Вы заходите на 3 этаж.")
                        state.location='etag3'
                    else:
                        print("Дверь заперта.")
                        state.location='lestnica'
            elif c == '2':
                    print("Вы идете вверх.")
                    state.e=state.e+1
                    state.location='lestnica'
            elif c == '3':
                    print("Вы идете вниз. ")
                    state.e=state.e-1
                    state.location='lestnica'
            else:
                    print('Неверный ввод. Выберите 1 или 2.')
                    state.location='lestnica'
    elif state.e==5:
            print("Вы на лестничной площадке 5 этажа.")
            print('Что вы сделаете?')
            print('1: зайдете на 5 этаж.')
            print('2: пойдете вниз.')
            c = input().strip()
            if c == '1':
                    if state.key5:
                        print("Дверь заперта, но вы открываете ее ключом и заходите на 5 этаж.")
                        state.key5=False
                        state.location='etag5'
                    elif (not state.key5) and (not state.key35O):
                        print("Вы заходите на 5 этаж.")
                        state.location='etag5'
                    else:
                        print("Дверь заперта.")
                        state.location='lestnica'
            elif c == '2':
                    print("Вы идете вниз. ")
                    state.e=state.e-1
                    state.location='lestnica'
            else:
                    print('Неверный ввод. Выберите 1 или 2.')
                    state.location='lestnica'
def zadniy_dvor(state: GameState):
    print("Вы на заднем дворе.")
    print('Что вы сделаете?')
    print('1: пойдете к выходу из школы, во двор.')
    print('2: пойдете к лавочкам.')
    c = input().strip()
    if c == '1':
        state.location='dvor'
    elif c == '2':
        print("Вы подходите к лавочкам.")
        if state.key1O:
            print("На лавочке лежат ключи от комнаты охраны.")
            print('Что вы сделаете?')
            print('1: заберете ключи и выйдете на задний двор.')
            print('2: выйдете на задний двор')
            l=0
            while l!=1:
                c = input().strip()
                if c == '1':
                    print('Вы забираете ключи и уходите.')
                    state.key1=True
                    state.key1O=False
                    state.location='zadniy_dvor'
                    l=1
                elif c == '2':
                    print("Вы заходите на задний двор.")
                    state.location='zadniy_dvor'
                    l=1
                else:
                    print('Неверный ввод. Выберите цифру.')
        elif not state.key1O:
            if state.lavochka:
                print('Что вы сделаете?')
                print('1: сломаете лавочку.')
                print('2: выйдете на задний двор.')
                l=0
                while l!=1:
                    c = input().strip()
                    if c == '1':
                        print('Вы с размаху бьете скамейку и она ломается. Из скамейки вырывается языческий демон и улетает с пронзительным визгом. В этом визге вы различаете: "Спасибо!".')
                        print('Вы испачкали руки своей кровью.')
                        state.lavochka=False
                        state.ruki="в крови"
                        state.location='zadniy_dvor'
                        l=1
                    elif c == '2':
                        print("Вы заходите на задний двор.")
                        state.location='zadniy_dvor'
                        l=1
                    else:
                        print('Неверный ввод. Выберите цифру.')
            else:
                a=random.randint(1,4)
                print("Вы любуетесь сломаной лавочкой, из которой вы освободили языческого демона.")
                if a==1 and state.zavhoz=="человек":
                    time.sleep(1)
                    print("И тут приходит завхоз и направляется к лавочке с целью починить ее.")
                    time.sleep(1)
                    print('Что вы сделаете?')
                    print('1: нападете на завхоза.')
                    print('2: выйдете на задний двор.')
                    l=0
                    while l!=1:
                        c = input().strip()
                        if c == '1':
                            print('Вы с размаху бьете завхоза и он убегает, а вы выходите.')
                            print('Вы испачкали руки кровью завхоза.')
                            state.ruki="в крови з"
                            state.lavochka=False
                            state.location='zadniy_dvor'
                            l=1
                        elif c == '2':
                            print("Вы выходите на задний двор, а завхоз чинит лавочку.")
                            state.lavochka=True
                            state.location='zadniy_dvor'
                            l=1
                        else:
                            print('Неверный ввод. Выберите 1 или 2.')
                else:
                    print("Вы идете на задний двор.")
                    state.location='zadniy_dvor'
    else:
        print('Неверный ввод. Выберите 1 или 2.')
        state.location='zadniy_dvor'
def dvor(state: GameState):
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
            state.location='prihogaya'
    elif c == '2':
            print("Вы идете на задний двор.")
            state.location='zadniy_dvor'
    else:
            print('Неверный ввод. Выберите 1 или 2.')
            state.location='dvor'
def etag2(state: GameState):
    print("Вы на 2 этаже. Здесь никогого нет.")
    if state.cat>0: print("Дверь 201 кабинета открыта.")
    print('Что вы сделаете?')
    print('1: попробуете двери классов, вдруг какая-то открыта.')
    print('2: выйдете на лестницу.')
    if state.cat>0: print('3: пойдете в 201.')
    c = input().strip()
    if c== '1':
            print("Все двери закрыты, кроме двери в учительскую, вы заходите внутрь.")
            state.location='uchitelskaya'
    elif c == '2':
            print("Вы выходите на лестницу.")
            state.location='lestnica'
    elif c == '3' and state.cat>0:
            print("Вы заходите в 201 кабинет.")
            state.location='c201'
    else:
            print('Неверный ввод. Выберите цифру.')
            state.location='etag2'
def c201(state: GameState):
    print("Вы в 201 кабинете.")
    if state.cat == 1:
        print("Все парты сдвинуты к стене, а за учительским столом сидит Кот.")
        print("Здравствуй, Двуногий! Что тебе нужно?")
        print('1: "Я просто пришел осмотреться."')
        print('2: "Я просто пришел поздороваться. Привет, Кот!"')
        print('3: "Ты можешь превратить завхоза обратно в человека?"')
        if state.eda:
            print('4: "Я пришел покормить тебя едой из столовой."')
        c = input().strip()
        if c == '1':
            print('Кот: "А, ну пока!"')
            print('Вы выходите на 2 этаж.')
            state.location = 'etag2'
        elif c == '2':
            print('Кот: "Ты очень вежливый, держи ключ от столовой."')
            print('Вы выходите на 2 этаж.')
            state.keyS = True
            state.location = 'etag2'
        elif c == '3':
            if state.zavhoz=='жаба':
                print('Кот: "Могу. Все уже готово." Кот хитро ухмыляется и смотрит на тебя.')
                state.zavhoz = "человек"
            else:
                print('Кот:"Он не жаба чтобы его превращать. Пока!"')
            print('Вы выходите на 2 этаж.')
            state.location = 'etag2'
        elif c == '4' and state.eda:
            print('Кот: "Мяу, спасибо! Пока!" Кот исчезает с громким одобрительным "Мяууууууууууу!"')
            state.cat = 2
            state.eda = False
            print('Вы выходите на 2 этаж.')
            state.location = 'etag2'
        else:
            print('Неверный ввод. Выберите цифру.')
            state.location = 'c201'
    else:
        print("Здесь ничего нет. И вы выходите.")
        state.location = "etag2"
def uchitelskaya(state: GameState):
    print("Вы в учительской. Здесь никого нет. Картина на стене сдвинута, и за ней виднеется проход в 207 кабинет(этот кабинет лаборантская).")
    print('Что вы сделаете?')
    print('1: Зайдете в 207 кабинет.')
    print('2: выйдете на 2 этаж.')
    c = input().strip()
    if c== '1':
            print("Вы заходите в 207 кабинет.")
            state.location='c207'
    elif c == '2':
            print("Вы выходите на 2 этаж.")
            state.location='etag2' 
    else:
            print('Неверный ввод. Выберите 1 или 2.')
            state.location='uchitelskaya'
def c207(state: GameState):
    print("Вы в 207 кабинете.")
    a = random.randint(1, 4)
    if a == 1:
        print("За партой стоит Олег Сергеевич и что-то делает за компьютером.")
        time.sleep(1)
        print('Он поднимает на тебя глаза и кричит:"Что ты тут делаешь! Иди пиши объяснительную!')
        print('Он отводит тебя в 105 кабинет и ты пишешь объяснительную.')
        state.e=1
        state.obyasnitelnaya=state.obyasnitelnaya+1
        if state.obyasnitelnaya==3:
            print("Вы исключены из школы!")
            state.location='end'
        else:
            print("Вы поникшие выходите из 105 кабинета.")
            state.location='etag1'
    else:
        print("На парте лежит компьютер. Вы заглядываете в него. Там ваши оценки по русскому.")
        print("Вдруг компьютер выключается вы в испуге выбегаете в учительскую, а из нее на второй этаж.")
        state.location='etag2'
def etag3(state: GameState):
    if state.r==1: start_background_music()
    print("Вы на 3 этаже. Из единственной двери доносятся звуки похожие на дыхание.")
    print('Что вы сделаете?')
    print('1: зайдете в эту дверь.')
    print('2: выйдете на лестницу.')
    c = input().strip()
    if c== '1':
            if state.key==True:
                print("Дверь заперта, но вы открываете ее большим серебряным ключом и входите.")
                state.location='boss'
            elif not state.key and not state.keyO:
                print("Вы открываете дверь, но за ней стена.")
                state.location='etag3'
            else:
                print("Дверь заперта.")
                state.location='etag3'
    elif c == '2':
            print("Вы выходите на лестницу.")
            state.location='lestnica' 
    else:
            print('Неверный ввод. Выберите 1 или 2.')
            state.location='etag3'
def boss(state: GameState):
    pygame.mixer.music.pause()
    script_dir = os.path.dirname(os.path.abspath(__file__))
    sound_file = os.path.join(script_dir, "босс.mp3")
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play(-1)
    state.r=1
    print("Вы в огромной темной комнате. Поначалу вы ничего не различаете, но ваши глазы привыкают к темноте и вы видите...")
    time.sleep(2)
    print("...ужасного монстра похожего на большую пчелу, но у него клюв, как у птицы, тело покрыто шерстью, a зубы - как у собаки - пчелоптицепеса!")
    print("Пчелоптицепес нападает на вас и бьет в ногу.")
    state.HP=state.HP-15
    if state.HP<1:
        print("Смерть.")
        print("Монстр убил вас.")
        state.location='end'
        return
    print("Ваше НP: ", state.HP)
    print("Что вы сделаете?")
    print('1: ударите монстра в лапу.')
    print('любая другая кнопка: ударите монстру в клюв.')
    c = input().strip()
    if c== '1':
            print("Вы бьете монстра в лапу и он взвывает в ужасе.")
            state.HPM=state.HPM-25
            print("НР монстра: ", state.HPM)
    else:
            print("Вы бьете монстра в клюв. Это оказалось слабое место и птица падает.")
            state.HPM=state.HPM-50
            print("НР монстра: ", state.HPM)
            print("Вы пользуетесь тем, что монстр в обмороке и сьедаете булочку. Ваше НР: ", state.HP+10)
            state.HP=state.HP+10
            print("Монстр медленно встает и злобно смотрит на вас.")
    print("Пчелоптицепес нападает на вас и бьет в руку.")
    state.HP=state.HP-25
    if state.HP<1:
        print("Смерть.")
        print("Монстр убил вас.")
        state.location='end'
        return
    print("Ваше НP: ", state.HP)
    print("Что вы сделаете?")
    print('1: ударите монстра в палец на ноге.')
    print('любая другая кнопка: ударите монстра в глаз.')
    c = input().strip()
    if c== '1':
            print("Вы бьете монстра в палец и он сгибается от боли.")
            state.HPM=state.HPM-50
            if state.HPM<1:
                pygame.mixer.music.pause()
                print("Вы убили монстра.")
                print("Вы спускаетесь на 1 этаж и все благодарят вас и подкидывают к потолку. Вы выиграли.")
                state.location='end'
                return
            print("НР монстра: ", state.HPM)
    else:
            print("Вы бьете монстра в глаз.")
            state.HPM=state.HPM-25
            print("НР монстра: ", state.HPM)
    print("Пчелоптицепес нападает на вас и бьет в голову.")
    print("Смерть.")
    print("Монстр убил вас.")
    state.location='end'
    pygame.mixer.music.pause()
def etag4(state: GameState):
    print("Вы на 4 этаже. Здесь никого нет. Дверь в 401 кабинет открыта.")
    print('Что вы сделаете?')
    print('1: зайдете в 401 кабинет.')
    print('2: выйдете на лестницу.')
    c = input().strip()
    if c== '1':
            print("Вы заходите в 401 кабинет.")
            state.location='c401'
    elif c == '2':
            print("Вы выходите на лестницу.")
            state.location='lestnica' 
    else:
            print('Неверный ввод. Выберите 1 или 2.')
            state.location='etag4'
def c401(state: GameState):
    print('Вы в 401 кабинете. Здесь никого нет.')
    if state.milo==0:
        print('На одной из парт лежит колба с надписью "Жи кое мы о".')
        print('Что вы сделаете?')
        print('1: выйдете на 4 этаж.')
        print('2: заберете колбу и выйдете.')
        c = input().strip()
        if c== '1':
                print("Вы выходите на 4 этаж.")
                state.location='etag4'
        elif c == '2':
                print("Вы забираете колбу и выходите.")
                state.milo=1
                state.location='etag4' 
        else:
                print('Неверный ввод. Выберите 1 или 2.')
                state.location='c401'
    else:
        print("Вы выходите, потому что тут ничего нет.")
        state.location='etag4'
def etag5(state: GameState):
    print("Вы на 5 этаже. В углу стоит пустая кошачья миска и упаковка кошачьего корма.")
    if state.cat==0 and state.zavhoz=='жаба': print("Здесь бегает и громко мяучет кот.")
    print('Что вы сделаете?')
    print('1: выйдете на лестницу.')
    print('2: осмотритесь.')
    if state.cat==0 and state.zavhoz=='жаба': print('3: поймаете кота.')
    c = input().strip()
    if c== '1':
            print("Вы выходите на лестницу.")
            state.location='lestnica'
    elif c=='2':
            if state.keyO==True:
                print('Вы видите коробку с надписью "Вставь пропуск".')
                print('Что вы сделаете?')
                print('1: вставите пропуск. ')
                print('2: выйдете на лестницу.')
                l=0
                while l!=1:
                    c = input().strip()
                    if c == '1':
                        print('Вы вставляете пропуск в коробку и достаете большой, резной, серебряный ключ, похожий на лапу собаки, но с крыльями птицы и лапками пчелы.')
                        state.key=True
                        state.propusk=False
                        state.keyO=False
                        state.location='etag5'
                        l=1
                    elif c == '2':
                        print("Вы выходите на лестницу.")
                        state.location='lestnica'
                    else:
                        print('Неверный ввод. Выберите 1 или 2.')
    elif state.cat==0 and state.zavhoz=='жаба' and c == '3':
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
                    state.location='etag5'
                    l=1
                elif c == '2':
                    print("Вы опускаете кота и насыпаете ему корм.")
                    print('Кот съедает весь корм и говорит:"Спасибо, кстати я волшебный кот! Мяууууу!"')
                    print('Кот исчезает с громким одобрительным "Мяууууу!"')
                    state.cat=1
                    state.location='etag5'
                    l=1
                elif c == '3':
                    print("Вы кусаете кота. Вы подавились шерстью кота и умерли, ибо нефиг жрать кота!!!")
                    state.location='end'
                    l=1
                else:
                    print('Неверный ввод. Выберите 1 или 2.')
    else:
            print('Неверный ввод. Выберите цифру.')
            state.location='etag5'
def tualet(state: GameState):
    print("Вы в туалете.")
    print('Что вы сделаете?')
    print('1: выйдете на 1 этаж.')
    print('2: помоете руки и выйдете.')
    c = input().strip()
    if c== '1':
                print("Вы выходите на 1 этаж.")
                state.location='etag1'
    elif c == '2':
                print("Вы моете руки. Ваши руки чисты.")
                state.ruki='чисты'
                if state.milo==1:
                    print('Вы набираете мыло в колбу с надписью "Жи кое мы о".')
                    state.milo=2
                print("Вы выходите из туалета.")
                state.location='etag1'
    else:
                print('Неверный ввод. Выберите 1 или 2.')
                state.location='tualet'
