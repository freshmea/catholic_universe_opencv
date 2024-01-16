class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    def average(self):
        average = (self.korean + self.math + self.english + self.science) / 4
        return average


class Special_student(Student):
    def __init__(self, name, korean, math, english, science, art):
        super().__init__(name, korean, math, english, science)
        self.art = art

    def average(self):
        average = (self.korean + self.math + self.english + self.science + self.art) / 5
        return average


def main():
    kim = Student("kim", 89, 90, 100, 80)
    park = Special_student("park", 89, 90, 100, 80, 100)
    print(f"{kim.name}'s average is : {kim.average()}")
    print(f"{park.name}'s average is : {park.average()}")


if __name__ == "__main__":
    main()
