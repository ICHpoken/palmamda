import datetime
class Hero():
    def __init__(self, name, sex, date, skills_amount):
        self.name = name
        if sex == 'male':
            self.sex = True
        elif sex == 'female':
            self.sex = False
        self.date = date
        self.skills_amount = skills_amount


    def show(self):
        return print(self.name, self.sex, self.date,self.skills_amount)


    def add(self):
        self.name = input('Напишите имя героя: ')
        self.sex = input('Введите пол героя: ')
        self.date = int(input())
        self.skills_amount = int(input())




class Game():
    def __init__(self, heroes):
        self.heroes = heroes