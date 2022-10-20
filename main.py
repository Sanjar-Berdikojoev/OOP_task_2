class Animal:
    def __init__(self, lifespan , height , weight , breathing_organ, number_of_limbs, habitat):
        self.lifespan = lifespan
        self.height = height
        self.weight = weight
        self.breathing_organ = breathing_organ
        self.number_of_limbs = number_of_limbs
        self.habitat = habitat
    def __str__(self):
        return f'Средняя продолжительность жизни (лет) - {self.lifespan}\n' \
               f'Средняя Высота/Рост/Длина (в см) - {self.height}\n' \
               f'Средний Вес (в кг) - {self.weight}\n' \
               f'Органы дыхания - {self.breathing_organ}\n' \
               f'Количество конечностей - {self.number_of_limbs}\n'\
               f'Ареал обитания - {self.habitat}'
class Mammals(Animal):
    def __init__(self, lifespan, height, weight, breathing_organ, number_of_limbs, habitat, milk_secretion , tail):
        super().__init__(lifespan, height, weight, breathing_organ, number_of_limbs, habitat)
        self.milk_secretion = milk_secretion
        self.tail = tail
    def __str__(self):
        return super(Mammals, self).__str__()+f'\nВыделение молока - {self.milk_secretion}\n' \
                                              f'Хвост - {self.tail}'
    def Intelligence (self, mind):
        return f'Разум - {mind}'
    def Danger (self, danger):
        return f'Опасность - {danger}'
Human = Mammals (70 , 175 , 75 , 'лёгкие' , 4 ,'вся Земля', 'да', 'нет, кроме случаев мутации (хвостатый мальчик)' )
print ('Млекопитающие: Человек')
print (Human)
print (Human.Intelligence(str('есть')))
print ('-'*50)
Platypus = Mammals (17 , 50 , 2.5 , 'лёгкие' , 4 ,'Австралия', 'да' , 'есть')
print ('Млекопитающие: Утконос')
print (Platypus)
print (Platypus.Danger(str('яд на шпорах')))
print ('-'*50)
Lion = Mammals (15 , 200 , 180 , 'лёгкие' , 4 ,'Африка', 'да', 'есть')
print ('Млекопитающие: Лев')
print (Lion)
print (Lion.Danger(str('острые зубы и когти, быстрая реакция')))
print ('-'*50)
class Reptiles(Animal):
    def __init__(self, lifespan, height, weight, breathing_organ, number_of_limbs, habitat, skin , tail):
        super().__init__(lifespan, height, weight, breathing_organ, number_of_limbs, habitat)
        self.skin = skin
        self.tail = tail
    def __str__(self):
        return super(Reptiles, self).__str__() + f'\nКожа - {self.skin}\n' \
                                                f'Хвост - {self.tail}'
    def Super_ability (self, ability):
        return f'Секретная способность - {ability}'
    def Danger(self, danger):
        return f'Опасность - {danger}'
Python = Reptiles(30, 700, 75 , 'лёгкие', 0, 'Индия, Индокитай, Индонезия', 'сухая, чешуйчатая', 'есть')
print('Пресмыкающиеся (Рептилии) : Питон')
print(Python)
print(Python.Super_ability(str('Компилирование кода')))
print(Python.Danger(str('Засчет большого размера может задушить')))
print('-' * 50)
Lizard = Reptiles(6, 11.5 , 0.025 , 'лёгкие', 4, 'вся Земля, кроме Севера России, Аляски и Канады', 'сухая, чешуйчатая', 'есть')
print('Пресмыкающиеся (Рептилии): Ящерица')
print(Lizard)
print(Lizard.Super_ability(str('Регенерация хвоста')))
print('-' * 50)
Crocodile = Reptiles(60 , 450, 300, 'лёгкие', 4, 'Африка, юг Китая, Латинская Америка', 'чешуйчатая, сухая (мокрая в воде)', 'есть')
print('Пресмыкающиеся (Рептилии): Крокодил')
print(Crocodile)
print(Crocodile.Danger(str('Острые зубы, скрытность в воде , высокая скорость по прямой')))
print ('-'*50)
class Arachnids(Animal):
    def __init__(self, lifespan, height, weight, breathing_organ, number_of_limbs, habitat, number_of_eyes):
        super().__init__(lifespan, height, weight, breathing_organ, number_of_limbs, habitat)
        self.number_of_eyes = number_of_eyes
    def __str__(self):
        return super(Arachnids, self).__str__() + f'\nКоличество глаз - {self.number_of_eyes}\n'
    def Use(self, use):
        return f'Польза - {use}'
Spider = Arachnids(0.3, 0.2, 0.01, 'трахеи', 8, 'вся Земля, кроме Гренландии', 8)
print('Паукообразные : Паук-Крестовик')
print(Spider)
print(Spider.Use(str('Ловит надоедливых мух и др. насекомых')))
print('-' * 50)
class Birds(Animal):
    def __init__(self, lifespan, height, weight, breathing_organ, number_of_limbs, habitat, plumage, tail, laying_eggs):
        super().__init__(lifespan, height, weight, breathing_organ, number_of_limbs, habitat)
        self.plumage = plumage
        self.tail = tail
        self.laying_eggs = laying_eggs
    def __str__(self):
        return super(Birds, self).__str__() + f'\nОперение - {self.plumage}\n' \
                                                 f'Хвост - {self.tail}\n'\
                                                 f'Откладывание яиц - {self.laying_eggs}'
    def Speed(self, speed):
        return f'Скорость (в км/ч) - {speed}'
    def Danger(self, danger):
        return f'Опасность - {danger}'
    def Use(self, use):
        return f'Польза - {use}'
    def Domestic(self, domestic):
        return f'Домашнее животное - {domestic}'
Eagle = Birds(40, 100, 6.7, 'лёгкие', 0, 'Азия, восток Европы, запад США и Канады', 'густое', 'есть', 'да (самки)')
print('Птицы : Орёл')
print(Eagle)
print(Eagle.Speed(int(320)))
print(Eagle.Danger(str('Острые когти, высокая скорость')))
print('-' * 50)
Chicken = Birds(5, 50, 1.5, 'лёгкие', 4, 'вся Земля', 'густое', 'есть', 'да (самки)')
print('Птицы : Курица')
print(Chicken)
print(Chicken.Use(str('приносит яйца, мясо и пух')))
print(Chicken.Domestic(str('да')))
print('-' * 50)
Ostrich = Birds(75, 210, 100, 'лёгкие', 4, 'Африка', 'густое', 'есть', 'да (самки)')
print('Птицы : Страус')
print(Ostrich)
print(Ostrich.Danger(str('Большой размер, высокая скорость')))
print(Ostrich.Speed(int(70)))
print ('-'*50)
class Fish(Animal):
    def __init__(self, lifespan, height, weight, breathing_organ, number_of_limbs, habitat, spawning):
        super().__init__(lifespan, height, weight, breathing_organ, number_of_limbs, habitat)
        self.spawning = spawning
    def __str__(self):
        return super(Fish, self).__str__() + f'\nНерест - {self.spawning}'
    def Danger(self, danger):
        return f'Опасность - {danger}'
    def Use(self, use):
        return f'Польза - {use}'
    def Singularity(self, singularity):
        return f'Особенность - {singularity}'
Salmon = Fish(13, 150, 43, 'жабры', 5, 'Атлантический и Тихий океаны', 'да')
print('Рыбы : Лосось')
print(Salmon)
print(Salmon.Use(str('мясо(рыба), Благодаря нему у нас есть роллы Филадельфия')))
print('-' * 50)
Shark = Fish(30, 460, 635, 'жабры', 5, 'Во всех океанах', 'нет')
print('Рыбы : Акула')
print(Shark)
print(Shark.Singularity(str('Нет костей')))
print(Shark.Danger(str('Очень острые зубы, незаметность, высокая скорость под водой')))
print('-' * 50)
Blobfish = Fish(7, 25, 2, 'жабры', 5, 'Австралия, глубина 600-1200 м', 'да')
print('Рыбы : Рыба-Капля ')
print(Blobfish)
print(Blobfish.Singularity(str('на поверхности выглядит очень грустной :(')))
print ('-'*50)
class Insects(Animal):
    def __init__(self, lifespan, height, weight, breathing_organ, number_of_limbs, habitat, number_of_wings):
        super().__init__(lifespan, height, weight, breathing_organ, number_of_limbs, habitat)
        self.number_of_wings = number_of_wings
    def __str__(self):
        return super(Insects, self).__str__() + f'\nКоличество крыльев (не пар) - {self.number_of_wings}'
    def Danger(self, danger):
        return f'Опасность - {danger}'
    def Singularity(self, singularity):
        return f'Особенность - {singularity}'
Fly = Insects('28 дней', 0.6, 43, 'трахеи', 6, 'вся Земли кроме Гренландии', 2)
print('Насекомые : Муха')
print(Fly)
print(Fly.Danger(str('является переносчиком многих болезней (заразы)')))
Butterfly = Insects('15-29 дней', 'варьируется в зависимости от вида бабочки', 0.005 , 'трахеи', 6, 'вся Земля', 4)
print('-' * 50)
print('Насекомые : Бабочка')
print(Butterfly)
print(Butterfly.Singularity(str('Появляются из куколки, которая в прошлом была гусеницей')))
print(Butterfly.Danger(str('Очень острые зубы, незаметность, высокая скорость под водой')))
print('-' * 50)
Redbug = Insects('неизвестно', 0.1, 'очень маленький' , 'трахеи', 6, 'вся Земля', 0)
print('Насекомые : Красноклоп (солдатик)')
print(Redbug)
print(Redbug.Singularity(str('любимый жук детства (по крайней мере у меня)')))
print ('-'*50)
class Zoo_Show:
    def __init__ (self, cost , description):
        self.cost = cost
        self.description = description
    def __str__ (self):
        return f'Стоимость билета (в $) - {self.cost}\n' \
               f'Описание шоу - {self.description}\n'
Ostrich_Race =  Zoo_Show(30,'Наши профессионалы покажут вам самые незабываемые гонки в вашей жизни.\n'
          'Вас будет ожидать огромная извилистая трасса протяженностью 15 км с препятствиями,за которой Вы будете\n'
          'наблюдать на высокой башне вблизи трассы. Длительность шоу: 30 минут')
Spider_Hunt =  Zoo_Show(10,'Многие люди боятся пауков, считают их страшными. Но на самом деле, если присмотреться\n'
                           'они довольно миленькие. Однако все же они остаются хищниками. В этом шоу мы предлагаем\n'
                           'нашим зрителям посмотреть за охотой пауков на разных насекомых. Вам будут выданы\n'
                           'специальные увеличительные очки, чтобы вы могли вдоволь насладиться процессом поимки\n'
                           'насекомых. Длительность шоу: 10-25 минут')
Lion_Circus =  Zoo_Show(40,'Цирк со львами наверно один из самых интересных и захватывающих из наших шоу.\n'
                           'Наши львы покажут вам самые разные трюки, за которыми вы будете наблюдать на\n'
                           'большом круглом поле. Не беспокойтесь, Вас будет отделять толстое прозрачное ограждение\n'
                           ',если вы наблюдаете за шоу внизу. Длительность шоу: 1 час')
Run_Away_From_Crocodile =  Zoo_Show('35 (для игрока) и 20 для (наблюдателя)','Это шоу наверно самое интерактивное и привлекательное.Вы можете выбрать быть наблюдателем или игроком\n'
                                       'Если Вы игрок Вам необходимо будет убегать от крокодила, вернее от его голограммы.\n'
                                       'Не беспокойтесь крокодил закрыт на другом поле. Ваша задача как игрока , не дать крокодилу вас поймать.\n'
                                       'На поле есть препятствия, которые вам надо будет избегать.Но он также видит вашу голограмму и охотится за ней.\n' 
                                       'Ваша цель убежать от крокодила и добраться до выхода. Если вы наблюдатель, то\n'
                                       'вы можете смотреть этим за захватывающим шоу в специальных комнатах. Длительность шоу: 30 минут')
Fast_Rolls_Making =  Zoo_Show(15,'Любите покушать?. Тогда это шоу для вас. Наши профессиональные повара покажут вам как надо готовить роллы.\n'
                                 'После завершения шоу , вы сможете вкусно поесть).')
print ('Виды шоу: \n'
       '1)Гонки на страусах \n'
       '2)Охота паука\n'
       '3)Цирк со львами\n'
       '4)Убеги от крокодила\n'
       '5)Шоу-готовка Роллов')
print ('Мы гарантируем вашу безопасность!\n'
       'Для выбора шоу введите его номер ')
show_name = int(input())
if show_name == 1:
    print(Ostrich_Race)
elif show_name == 2:
    print(Spider_Hunt)
elif show_name == 3:
    print(Lion_Circus)
elif show_name == 4:
    print(Run_Away_From_Crocodile)
elif show_name == 5:
    print(Fast_Rolls_Making)
else:
    print('К сожалению пока что у нас нет других шоу(')

