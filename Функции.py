import pygame
import os
import time
import random

# ─── ASCII-арт ───────────────────────────────────────────────────────────────

FROG_ART = r'''
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
'''

SCHOOL_ART = r"""
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
"""

CAT_ART = r"""
       \`-._           __
        \  `-..____,.'  `.
         :`.         /    `.
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
                   `----`
"""

# ─── Состояние игры ───────────────────────────────────────────────────────────

class GameState:
    def __init__(self):
        self.location = "entrance"
        self.current_floor = 1
        self.restart_music = False

        # Предметы и ключи
        self.has_pass = True
        self.has_boss_key = False
        self.has_boss_key_available = True
        self.has_floor3_key = False
        self.has_floor5_key = False
        self.guard_keys_available = True
        self.has_screwdriver = False
        self.has_guard_room_key = False
        self.guard_room_key_on_bench = True
        self.has_cafeteria_key = False

        # Статусы
        self.notes_count = 0
        self.soap_state = 0
        self.has_food = False
        self.bench_intact = True
        self.cat_state = 0
        self.player_hp = 100
        self.boss_hp = 100
        self.janitor_form = "human"
        self.hands_state = "clean"

# ─── Утилиты ──────────────────────────────────────────────────────────────────

def get_choice():
    return input().strip()

def play_background_music():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    sound_file = os.path.join(script_dir, "фоновая музыка.mp3")
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play(-1)

# ─── Локации ──────────────────────────────────────────────────────────────────

def entrance_hall(state):
    print("Вы находитесь в прихожей.")
    print("Вы подходите к турникетам, и на вас подозрительно смотрит охранница.")
    print("Что вы сделаете?")
    print("1: приложить пропуск и пройти через турникет.")
    print("2: подойти к охраннице и сказать, что вы забыли пропуск.")
    choice = get_choice()
    if choice == "1":
        if state.has_pass:
            print("Вы прикладываете пропуск, турникет щёлкает, и вы проходите на первый этаж.")
            state.location = "floor1"
        else:
            print("Но у вас нет пропуска!")
            if random.randint(1, 2) == 2:
                time.sleep(2)
                print("Но тут охранница отворачивается и локтем задевает кнопку автоматического открытия турникета, и вы проходите на первый этаж.")
                state.location = "floor1"
            else:
                state.location = "entrance"
    elif choice == "2":
        print("Вы подходите к охраннице и говорите, что забыли пропуск.")
        print('Охранница вздыхает: "Ну ладно, проходите, но больше так не делайте". Вы проходите на первый этаж.')
        state.location = "floor1"
    else:
        print("Неверный ввод. Выберите 1 или 2.")
        state.location = "entrance"

def floor1(state):
    print("Вы на первом этаже. Здесь как обычно многолюдно, но не очень, и все немного притихшие.")
    print("Что вы сделаете?")
    print("1: пойдете в 105 кабинет.")
    print("2: пойдете в комнату охраны.")
    print("3: пойдете на лестницу.")
    print("4: пойдете в туалет.")
    print("5: пойдете к куллерам.")
    if state.has_cafeteria_key:
        print("6: пойдете в столовую")
    choice = get_choice()
    if choice == "1":
        print("Вы заходите в 105 кабинет.")
        state.location = "room105"
    elif choice == "2":
        if state.has_guard_room_key:
            print("Комната охраны закрыта, но вы отпираете ее ключом и заходите.")
            state.has_guard_room_key = False
            state.location = "guard_room"
        elif not state.has_guard_room_key and not state.guard_room_key_on_bench:
            print("Вы заходите в комнату охраны.")
            state.location = "guard_room"
        else:
            print("Комната охраны закрыта.")
            state.location = "floor1"
    elif choice == "3":
        print("Вы заходите на лестницу.")
        state.location = "stairs"
    elif choice == "4":
        print("Вы заходите в туалет.")
        state.location = "bathroom"
    elif choice == "5":
        print("Вы подходите к куллеру. В него не вставлена баклажка с водой.")
        if state.soap_state == 2 and state.janitor_form == "human":
            print("Что вы сделаете?")
            print('1: зальете в куллер мыло из колбы с надписью "Жи кое мы о".')
            print("2: вернетесь на 1 этаж.")
            done = False
            while not done:
                choice = get_choice()
                if choice == "1":
                    print("Вы заливаете мыло, и оно пачкает вам руки. Вы отходите и ждёте, пока что-нибудь произойдёт.")
                    state.hands_state = "soapy"
                    print("Через некоторое время к куллеру подходит завхоз и ставит на него баклажку с водой и пьёт оттуда. Он начинает задыхаться, его глаза закатываются, и он превращается в жабу, сшибая баклажку своим телом.")
                    print(FROG_ART)
                    state.janitor_form = "frog"
                    print("Вы возвращаетесь на 1 этаж.")
                    state.location = "floor1"
                    done = True
                elif choice == "2":
                    print("Вы возвращаетесь на 1 этаж.")
                    state.location = "floor1"
                    done = True
                else:
                    print("Неверный ввод. Выберите 1 или 2.")
        else:
            print("Тут ничего интересного, вы выходите.")
            state.location = "floor1"
    elif choice == "6" and state.has_cafeteria_key:
        print("Вы открываете столовую ключом и входите.")
        state.location = "cafeteria"
    else:
        print("Неверный ввод. Выберите цифру.")
        state.location = "floor1"

def cafeteria(state):
    print("Вы в столовой.")
    if state.janitor_form == "human":
        print("Завхоз выгоняет вас отсюда.")
        state.location = "floor1"
    elif not state.has_food:
        print("Вы забираете еду под злобное кваканье жабы-завхоза и выходите.")
        state.has_food = True
        state.location = "floor1"
    else:
        print("Здесь ничего нет и вы выходите.")
        state.location = "floor1"

def room_105(state):
    print("Вы в 105 кабинете. За столом сидит Инга Александровна.")
    if random.randint(1, 2) == 1:
        time.sleep(1)
        print('Инга Александровна: "А ну вон отсюда! Тебя сюда никто не приглашал! Пиши объяснительную!!!!"')
        print("Вы пишете объяснительную и поникшие выходите из 105 кабинета.")
        state.notes_count += 1
        if state.notes_count == 3:
            state.location = "end"
            print("Вы исключены из школы!")
        else:
            state.location = "floor1"
    else:
        print("Она не обращает на тебя внимания. В кабинете нет ничего интересного. Ты возвращаешься обратно.")
        state.location = "floor1"

def guard_room(state):
    print("Вы в комнате охраны.")
    if state.guard_keys_available:
        print("На столе лежат ключи от 3 этажа, ключи от 5 этажа и отвертка.")
        print("Что вы сделаете?")
        print("1: возьмете ключи с отверткой и уйдете.")
        print("2: уйдете.")
        choice = get_choice()
        if choice == "1":
            print("Вы хватаете ключи, отвертку и бесшумно выходите.")
            state.has_floor3_key = True
            state.has_floor5_key = True
            state.has_screwdriver = True
            state.guard_keys_available = False
            state.location = "floor1"
        elif choice == "2":
            print("Вы выходите.")
            state.location = "floor1"
        else:
            print("Неверный ввод. Выберите 1 или 2.")
            state.location = "guard_room"
    else:
        print("Вы не находите здесь ничего интересного и выходите.")
        state.location = "floor1"

def stairs(state):
    if state.current_floor == 1:
        print("Вы на лестничной площадке первого этажа.")
        print("Что вы сделаете?")
        print("1: зайдете на 1 этаж.")
        print("2: пойдете вверх.")
        print("3: выйдете на задний двор.")
        choice = get_choice()
        if choice == "1":
            print("Вы заходите на 1 этаж.")
            state.location = "floor1"
        elif choice == "2":
            print("Вы идете вверх.")
            state.current_floor = 2
            state.location = "stairs"
        elif choice == "3":
            print("Вы выходите во двор, и дверь за вами захлопывается.")
            state.location = "backyard"
        else:
            print("Неверный ввод. Выберите цифру.")
            state.location = "stairs"
    elif state.current_floor in (2, 4):
        print(f"Вы на лестничной площадке {state.current_floor} этажа.")
        print("Что вы сделаете?")
        print(f"1: зайдете на {state.current_floor} этаж.")
        print("2: пойдете вверх.")
        print("3: пойдете вниз.")
        choice = get_choice()
        if choice == "1":
            print(f"Вы заходите на {state.current_floor} этаж.")
            state.location = f"floor{state.current_floor}"
        elif choice == "2":
            print("Вы идете вверх.")
            state.current_floor += 1
            state.location = "stairs"
        elif choice == "3":
            print("Вы идете вниз.")
            state.current_floor -= 1
            state.location = "stairs"
        else:
            print("Неверный ввод. Выберите 1, 2 или 3.")
            state.location = "stairs"
    elif state.current_floor == 3:
        print("Вы на лестничной площадке 3 этажа.")
        print("Что вы сделаете?")
        print("1: зайдете на 3 этаж.")
        print("2: пойдете вверх.")
        print("3: пойдете вниз.")
        choice = get_choice()
        if choice == "1":
            if state.has_floor3_key:
                print("Дверь заперта, но вы открываете ее ключом и заходите на 3 этаж.")
                state.has_floor3_key = False
                state.location = "floor3"
            elif not state.has_floor3_key and not state.guard_keys_available:
                print("Вы заходите на 3 этаж.")
                state.location = "floor3"
            else:
                print("Дверь заперта.")
                state.location = "stairs"
        elif choice == "2":
            print("Вы идете вверх.")
            state.current_floor += 1
            state.location = "stairs"
        elif choice == "3":
            print("Вы идете вниз.")
            state.current_floor -= 1
            state.location = "stairs"
        else:
            print("Неверный ввод. Выберите 1, 2 или 3.")
            state.location = "stairs"
    elif state.current_floor == 5:
        print("Вы на лестничной площадке 5 этажа.")
        print("Что вы сделаете?")
        print("1: зайдете на 5 этаж.")
        print("2: пойдете вниз.")
        choice = get_choice()
        if choice == "1":
            if state.has_floor5_key:
                print("Дверь заперта, но вы открываете ее ключом и заходите на 5 этаж.")
                state.has_floor5_key = False
                state.location = "floor5"
            elif not state.has_floor5_key and not state.guard_keys_available:
                print("Вы заходите на 5 этаж.")
                state.location = "floor5"
            else:
                print("Дверь заперта.")
                state.location = "stairs"
        elif choice == "2":
            print("Вы идете вниз.")
            state.current_floor -= 1
            state.location = "stairs"
        else:
            print("Неверный ввод. Выберите 1 или 2.")
            state.location = "stairs"

def backyard(state):
    print("Вы на заднем дворе.")
    print("Что вы сделаете?")
    print("1: пойдете к выходу из школы, во двор.")
    print("2: пойдете к лавочкам.")
    choice = get_choice()
    if choice == "1":
        state.location = "courtyard"
    elif choice == "2":
        print("Вы подходите к лавочкам.")
        if state.guard_room_key_on_bench:
            print("На лавочке лежат ключи от комнаты охраны.")
            print("Что вы сделаете?")
            print("1: заберете ключи и выйдете на задний двор.")
            print("2: выйдете на задний двор.")
            done = False
            while not done:
                choice = get_choice()
                if choice == "1":
                    print("Вы забираете ключи и уходите.")
                    state.has_guard_room_key = True
                    state.guard_room_key_on_bench = False
                    state.location = "backyard"
                    done = True
                elif choice == "2":
                    print("Вы заходите на задний двор.")
                    state.location = "backyard"
                    done = True
                else:
                    print("Неверный ввод. Выберите цифру.")
        elif not state.guard_room_key_on_bench:
            if state.bench_intact:
                print("Что вы сделаете?")
                print("1: сломаете лавочку.")
                print("2: выйдете на задний двор.")
                done = False
                while not done:
                    choice = get_choice()
                    if choice == "1":
                        print('Вы с размаху бьете скамейку, и она ломается. Из скамейки вырывается языческий демон и улетает с пронзительным визгом. В этом визге вы различаете: "Спасибо!".')
                        print("Вы испачкали руки своей кровью.")
                        state.bench_intact = False
                        state.hands_state = "bloody"
                        state.location = "backyard"
                        done = True
                    elif choice == "2":
                        print("Вы заходите на задний двор.")
                        state.location = "backyard"
                        done = True
                    else:
                        print("Неверный ввод. Выберите цифру.")
            else:
                print("Вы любуетесь сломаной лавочкой, из которой вы освободили языческого демона.")
                if random.randint(1, 4) == 1 and state.janitor_form == "human":
                    time.sleep(1)
                    print("И тут приходит завхоз и направляется к лавочке с целью починить ее.")
                    time.sleep(1)
                    print("Что вы сделаете?")
                    print("1: нападете на завхоза.")
                    print("2: выйдете на задний двор.")
                    done = False
                    while not done:
                        choice = get_choice()
                        if choice == "1":
                            print("Вы с размаху бьете завхоза, и он убегает, а вы выходите.")
                            print("Вы испачкали руки кровью завхоза.")
                            state.hands_state = "bloody_janitor"
                            state.bench_intact = False
                            state.location = "backyard"
                            done = True
                        elif choice == "2":
                            print("Вы выходите на задний двор, а завхоз чинит лавочку.")
                            state.bench_intact = True
                            state.location = "backyard"
                            done = True
                        else:
                            print("Неверный ввод. Выберите 1 или 2.")
                else:
                    print("Вы идете на задний двор.")
                    state.location = "backyard"
    else:
        print("Неверный ввод. Выберите 1 или 2.")
        state.location = "backyard"

def courtyard(state):
    print("Вы во дворе.")
    print(SCHOOL_ART)
    print("Что вы сделаете?")
    print("1: войдете в школу.")
    print("2: пойдете на задний двор.")
    choice = get_choice()
    if choice == "1":
        print("Вы поднимаетесь по лестнице и входите в школу.")
        state.location = "entrance"
    elif choice == "2":
        print("Вы идете на задний двор.")
        state.location = "backyard"
    else:
        print("Неверный ввод. Выберите 1 или 2.")
        state.location = "courtyard"

def floor2(state):
    print("Вы на 2 этаже. Здесь никого нет.")
    if state.cat_state > 0:
        print("Дверь 201 кабинета открыта.")
    print("Что вы сделаете?")
    print("1: попробуете двери классов, вдруг какая-то открыта.")
    print("2: выйдете на лестницу.")
    if state.cat_state > 0:
        print("3: пойдете в 201.")
    choice = get_choice()
    if choice == "1":
        print("Все двери закрыты, кроме двери в учительскую, вы заходите внутрь.")
        state.location = "teachers_room"
    elif choice == "2":
        print("Вы выходите на лестницу.")
        state.location = "stairs"
    elif choice == "3" and state.cat_state > 0:
        print("Вы заходите в 201 кабинет.")
        state.location = "room201"
    else:
        print("Неверный ввод. Выберите цифру.")
        state.location = "floor2"

def room_201(state):
    print("Вы в 201 кабинете.")
    if state.cat_state == 1:
        print("Все парты сдвинуты к стене, а за учительским столом сидит Кот.")
        print("Здравствуй, Двуногий! Что тебе нужно?")
        print('1: "Я просто пришел осмотреться."')
        print('2: "Я просто пришел поздороваться. Привет, Кот!"')
        print('3: "Ты можешь превратить завхоза обратно в человека?"')
        if state.has_food:
            print('4: "Я пришел покормить тебя едой из столовой."')
        choice = get_choice()
        if choice == "1":
            print('Кот: "А, ну пока!"')
            print("Вы выходите на 2 этаж.")
            state.location = "floor2"
        elif choice == "2":
            print('Кот: "Ты очень вежливый, держи ключ от столовой."')
            print("Вы выходите на 2 этаж.")
            state.has_cafeteria_key = True
            state.location = "floor2"
        elif choice == "3":
            if state.janitor_form == "frog":
                print('Кот: "Могу. Все уже готово." Кот хитро ухмыляется и смотрит на тебя.')
                state.janitor_form = "human"
            else:
                print('Кот: "Он не жаба, чтобы его превращать. Пока!"')
            print("Вы выходите на 2 этаж.")
            state.location = "floor2"
        elif choice == "4" and state.has_food:
            print('Кот: "Мяу, спасибо! Пока!" Кот исчезает с громким одобрительным "Мяууууууууууу!"')
            state.cat_state = 2
            state.has_food = False
            print("Вы выходите на 2 этаж.")
            state.location = "floor2"
        else:
            print("Неверный ввод. Выберите цифру.")
            state.location = "room201"
    else:
        print("Здесь ничего нет. И вы выходите.")
        state.location = "floor2"

def teachers_room(state):
    print("Вы в учительской. Здесь никого нет. Картина на стене сдвинута, и за ней виднеется проход в 207 кабинет (этот кабинет — лаборантская).")
    print("Что вы сделаете?")
    print("1: Зайдете в 207 кабинет.")
    print("2: выйдете на 2 этаж.")
    choice = get_choice()
    if choice == "1":
        print("Вы заходите в 207 кабинет.")
        state.location = "room207"
    elif choice == "2":
        print("Вы выходите на 2 этаж.")
        state.location = "floor2"
    else:
        print("Неверный ввод. Выберите 1 или 2.")
        state.location = "teachers_room"

def room_207(state):
    print("Вы в 207 кабинете.")
    if random.randint(1, 4) == 1:
        print("За партой стоит Олег Сергеевич и что-то делает за компьютером.")
        time.sleep(1)
        print('Он поднимает на тебя глаза и кричит: "Что ты тут делаешь! Иди пиши объяснительную!"')
        print("Он отводит тебя в 105 кабинет, и ты пишешь объяснительную.")
        state.current_floor = 1
        state.notes_count += 1
        if state.notes_count == 3:
            print("Вы исключены из школы!")
            state.location = "end"
        else:
            print("Вы поникшие выходите из 105 кабинета.")
            state.location = "floor1"
    else:
        print("На парте лежит компьютер. Вы заглядываете в него. Там ваши оценки по русскому.")
        print("Вдруг компьютер выключается, вы в испуге выбегаете в учительскую, а из нее — на второй этаж.")
        state.location = "floor2"

def floor3(state):
    if state.restart_music:
        play_background_music()
    print("Вы на 3 этаже. Из единственной двери доносятся звуки, похожие на дыхание.")
    print("Что вы сделаете?")
    print("1: зайдете в эту дверь.")
    print("2: выйдете на лестницу.")
    choice = get_choice()
    if choice == "1":
        if state.has_boss_key:
            print("Дверь заперта, но вы открываете ее большим серебряным ключом и входите.")
            state.location = "boss"
        elif not state.has_boss_key and not state.has_boss_key_available:
            print("Вы открываете дверь, но за ней стена.")
            state.location = "floor3"
        else:
            print("Дверь заперта.")
            state.location = "floor3"
    elif choice == "2":
        print("Вы выходите на лестницу.")
        state.location = "stairs"
    else:
        print("Неверный ввод. Выберите 1 или 2.")
        state.location = "floor3"

def boss_fight(state):
    pygame.mixer.music.pause()
    script_dir = os.path.dirname(os.path.abspath(__file__))
    sound_file = os.path.join(script_dir, "босс.mp3")
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play(-1)
    state.restart_music = True
    print("Вы в огромной темной комнате. Поначалу вы ничего не различаете, но ваши глаза привыкают к темноте, и вы видите...")
    time.sleep(2)
    print("...ужасного монстра, похожего на большую пчелу, но у него клюв, как у птицы, тело покрыто шерстью, а зубы — как у собаки: пчелоптицепеса!")
    print("Пчелоптицепес нападает на вас и бьет в ногу.")
    state.player_hp -= 15
    if state.player_hp < 1:
        print("Смерть.")
        print("Монстр убил вас.")
        state.location = "end"
        return
    print(f"Ваше HP: {state.player_hp}")
    print("Что вы сделаете?")
    print("1: ударите монстра в лапу.")
    print("любая другая кнопка: ударите монстра в клюв.")
    choice = get_choice()
    if choice == "1":
        print("Вы бьете монстра в лапу, и он взвывает в ужасе.")
        state.boss_hp -= 25
        print(f"HP монстра: {state.boss_hp}")
    else:
        print("Вы бьете монстра в клюв. Это оказалось слабое место, и птица падает.")
        state.boss_hp -= 50
        print(f"HP монстра: {state.boss_hp}")
        print(f"Вы пользуетесь тем, что монстр в обмороке, и съедаете булочку. Ваше HP: {state.player_hp + 10}")
        state.player_hp += 10
        print("Монстр медленно встает и злобно смотрит на вас.")
    print("Пчелоптицепес нападает на вас и бьет в руку.")
    state.player_hp -= 25
    if state.player_hp < 1:
        print("Смерть.")
        print("Монстр убил вас.")
        state.location = "end"
        return
    print(f"Ваше HP: {state.player_hp}")
    print("Что вы сделаете?")
    print("1: ударите монстра в палец на ноге.")
    print("любая другая кнопка: ударите монстра в глаз.")
    choice = get_choice()
    if choice == "1":
        print("Вы бьете монстра в палец, и он сгибается от боли.")
        state.boss_hp -= 50
        if state.boss_hp < 1:
            pygame.mixer.music.pause()
            print("Вы убили монстра.")
            print("Вы спускаетесь на 1 этаж, и все благодарят вас и подкидывают к потолку. Вы выиграли.")
            state.location = "end"
            return
        print(f"HP монстра: {state.boss_hp}")
    else:
        print("Вы бьете монстра в глаз.")
        state.boss_hp -= 25
        print(f"HP монстра: {state.boss_hp}")
    print("Пчелоптицепес нападает на вас и бьет в голову.")
    print("Смерть.")
    print("Монстр убил вас.")
    state.location = "end"
    pygame.mixer.music.pause()

def floor4(state):
    print("Вы на 4 этаже. Здесь никого нет. Дверь в 401 кабинет открыта.")
    print("Что вы сделаете?")
    print("1: зайдете в 401 кабинет.")
    print("2: выйдете на лестницу.")
    choice = get_choice()
    if choice == "1":
        print("Вы заходите в 401 кабинет.")
        state.location = "room401"
    elif choice == "2":
        print("Вы выходите на лестницу.")
        state.location = "stairs"
    else:
        print("Неверный ввод. Выберите 1 или 2.")
        state.location = "floor4"

def room_401(state):
    print("Вы в 401 кабинете. Здесь никого нет.")
    if state.soap_state == 0:
        print('На одной из парт лежит колба с надписью "Жи кое мы о".')
        print("Что вы сделаете?")
        print("1: выйдете на 4 этаж.")
        print("2: заберете колбу и выйдете.")
        choice = get_choice()
        if choice == "1":
            print("Вы выходите на 4 этаж.")
            state.location = "floor4"
        elif choice == "2":
            print("Вы забираете колбу и выходите.")
            state.soap_state = 1
            state.location = "floor4"
        else:
            print("Неверный ввод. Выберите 1 или 2.")
            state.location = "room401"
    else:
        print("Вы выходите, потому что тут ничего нет.")
        state.location = "floor4"

def floor5(state):
    print("Вы на 5 этаже. В углу стоит пустая кошачья миска и упаковка кошачьего корма.")
    if state.cat_state == 0 and state.janitor_form == "frog":
        print("Здесь бегает и громко мяучет кот.")
    print("Что вы сделаете?")
    print("1: выйдете на лестницу.")
    print("2: осмотритесь.")
    if state.cat_state == 0 and state.janitor_form == "frog":
        print("3: поймаете кота.")
    choice = get_choice()
    if choice == "1":
        print("Вы выходите на лестницу.")
        state.location = "stairs"
    elif choice == "2":
        if state.has_boss_key_available:
            print('Вы видите коробку с надписью "Вставь пропуск".')
            print("Что вы сделаете?")
            print("1: вставите пропуск.")
            print("2: выйдете на лестницу.")
            done = False
            while not done:
                choice = get_choice()
                if choice == "1":
                    print("Вы вставляете пропуск в коробку и достаете большой, резной, серебряный ключ, похожий на лапу собаки, но с крыльями птицы и лапками пчелы.")
                    state.has_boss_key = True
                    state.has_pass = False
                    state.has_boss_key_available = False
                    state.location = "floor5"
                    done = True
                elif choice == "2":
                    print("Вы выходите на лестницу.")
                    state.location = "stairs"
                    done = True
                else:
                    print("Неверный ввод. Выберите 1 или 2.")
        else:
            print("Здесь ничего интересного, вы выходите на лестницу.")
            state.location = "stairs"
    elif choice == "3" and state.cat_state == 0 and state.janitor_form == "frog":
        print('Вы ловите кота, и он перестает мяукать. Кот: "Зачем ты меня поймал?"')
        print(CAT_ART)
        print("Что вы сделаете?")
        print("1: бросите кота.")
        print("2: покормите кота.")
        print("3: откусите кота.")
        done = False
        while not done:
            choice = get_choice()
            if choice == "1":
                print("Вы бросаете кота.")
                state.location = "floor5"
                done = True
            elif choice == "2":
                print("Вы опускаете кота и насыпаете ему корм.")
                print('Кот съедает весь корм и говорит: "Спасибо, кстати я волшебный кот! Мяууууу!"')
                print('Кот исчезает с громким одобрительным "Мяууууу!"')
                state.cat_state = 1
                state.location = "floor5"
                done = True
            elif choice == "3":
                print("Вы кусаете кота. Вы подавились шерстью кота и умерли, ибо нефиг жрать кота!!!")
                state.location = "end"
                done = True
            else:
                print("Неверный ввод. Выберите 1, 2 или 3.")
    else:
        print("Неверный ввод. Выберите цифру.")
        state.location = "floor5"

def bathroom(state):
    print("Вы в туалете.")
    print("Что вы сделаете?")
    print("1: выйдете на 1 этаж.")
    print("2: помоете руки и выйдете.")
    choice = get_choice()
    if choice == "1":
        print("Вы выходите на 1 этаж.")
        state.location = "floor1"
    elif choice == "2":
        print("Вы моете руки. Ваши руки чисты.")
        state.hands_state = "clean"
        if state.soap_state == 1:
            print('Вы набираете мыло в колбу с надписью "Жи кое мы о".')
            state.soap_state = 2
        print("Вы выходите из туалета.")
        state.location = "floor1"
    else:
        print("Неверный ввод. Выберите 1 или 2.")
        state.location = "bathroom"

# ─── Диспетчер локаций ────────────────────────────────────────────────────────

LOCATIONS = {
    "entrance": entrance_hall,
    "floor1": floor1,
    "floor2": floor2,
    "floor3": floor3,
    "floor4": floor4,
    "floor5": floor5,
    "room105": room_105,
    "guard_room": guard_room,
    "stairs": stairs,
    "backyard": backyard,
    "courtyard": courtyard,
    "teachers_room": teachers_room,
    "room207": room_207,
    "room401": room_401,
    "bathroom": bathroom,
    "boss": boss_fight,
    "cafeteria": cafeteria,
    "room201": room_201,
}
