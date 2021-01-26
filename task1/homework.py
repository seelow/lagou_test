class Animal:

    def __init__(self, name, color, age, gender):
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender

    @classmethod
    def cry(cls):
        print('类方法: 叫')

    @classmethod
    def run(cls):
        print('类方法：跑')


class Cat(Animal):

    def __init__(self, hair, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.hair = hair

    def catch(self):
        print('成员方法：捉老鼠')

    def cry(self):
        print('喵喵叫')

    def show(self):
        print(f'name:{self.name}, color:{self.color}, age:{self.age}, gender:{self.gender}, hair:{self.hair}')

if __name__ == '__main__':
    cat = Cat(hair='短发', name='小黑', color='黑', age=1, gender='雄')
    cat.show()
