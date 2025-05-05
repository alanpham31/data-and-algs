class Student:
    __slots__ = ("_name", "_year", "_id", "_major")

    def __init__(self, name: str, year: int, student_id: str, major: str) -> None:
        # initialize instance variables given in __slots__
        self._name = name
        self._year = year
        self._id = student_id
        self._major = major
    
    def __str__(self) -> str:
        # builds and returns string of what printed Student object should look like
        result = f"{self._name}:\n"
        result += f"\t{}"

def main() -> None:
    miles = Student("Miles Logan", 2, "01234567", "Chemistry")
    alicia = Student("Alicia Sang", 4, "98765432", "Neuroscience")
    print(miles)
    print(alicia)

main()