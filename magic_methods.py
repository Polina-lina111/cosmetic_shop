class CourseModule:
    def __init__(self, title, duration_hours, practice_tasks):
        self.title = title
        self.duration_hours = duration_hours
        self.practice_tasks = practice_tasks

    def __str__(self):
        return f"Модуль: {self.title}, тривалість: {self.duration_hours} год."

    def __repr__(self):
        return (
            f"CourseModule("
            f"title='{self.title}', "
            f"duration_hours={self.duration_hours}, "
            f"practice_tasks={self.practice_tasks})"
        )

    def __len__(self):
        return self.practice_tasks

    def __add__(self, other):
        if isinstance(other, CourseModule):
            return self.duration_hours + other.duration_hours

        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, CourseModule):
            return self.practice_tasks == other.practice_tasks

        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, CourseModule):
            return self.duration_hours < other.duration_hours

        return NotImplemented

if __name__ == "__main__":

    module1 = CourseModule("Python Basics", 12, 5)
    module2 = CourseModule("Django Intro", 20, 8)
    module3 = CourseModule("REST API", 10, 5)

    print("Перевірка __str__():")
    print(module1)

    print("\nПеревірка __repr__():")
    print(repr(module1))

    print("\nПеревірка __len__():")
    print(len(module2))

    print("\nПеревірка __add__():")
    print(module1 + module2)

    print("\nПеревірка __eq__():")
    print(module1 == module3)

    print("\nПеревірка __lt__():")
    print(module3 < module2)

    print("\nСортування модулів:")
    modules = [module1, module2, module3]

    sorted_modules = sorted(modules)

    for module in sorted_modules:
        print(module)