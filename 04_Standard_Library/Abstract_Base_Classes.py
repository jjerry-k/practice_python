from abc import *

class template(ABC):
    """
    비어있는 class의 템플릿을 만들어주는 역할
    """
    @abstractmethod
    def study(self):
        pass

    @abstractmethod
    def rest(self):
        pass


class Student(template):
    def study(self):
        print("공부하자!")

    def rest(self):
        print("휴식하자!")

jerry = Student()

jerry.study()
jerry.rest()

