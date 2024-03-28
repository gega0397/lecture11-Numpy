import numpy as np
from data_generator import generate_data, FULL_NAMES, SUBJECTS

students = generate_data(FULL_NAMES, 100)
subjects = np.concatenate((np.array(['ინგლისური', 'მათემატიკა']), generate_data(SUBJECTS, 3)))

print(subjects)
print(students)

data = np.random.randint(0, 100, size=(len(students), len(subjects)))

print(data)


def get_average(_data, _students=students):
    average = np.mean(_data, axis=1)

    # print(average)
    # print(np.argmax(average, axis=None))
    # print(np.max(average, axis=None))
    # print(students[np.argmax(average, axis=None)])
    # print(np.where(average == np.max(average, axis=None)))
    print(students[np.where(average == np.max(average, axis=None))])


def get_min_max(_data, _subject, _students=students):
    _max = np.max(_data[:, _subject], axis=0)
    _min = np.min(_data[:, _subject], axis=0)
    # print(_max, _min)

    print(_students[np.where((_data[:, _subject] == _max) | (_data[:, _subject] == _min))[0]])


def get_above_average(_data, _subject, _students=students):

    _mean = np.mean(_data[:, _subject], axis=0)

    print(_students[np.where(_data[:, _subject] > _mean)[0]])


if __name__ == '__main__':
    get_average(data)
    get_min_max(data, _subject=np.where(subjects == 'მათემატიკა')[0][0])
    get_above_average(data, _subject=np.where(subjects == 'ინგლისური')[0][0])
