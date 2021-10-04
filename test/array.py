import numpy as np
if __name__ == '__main__':
    array = [
        [1, 2,12],
        [3, 4,34],
        [5, 6,56],
        [7, 8,78],
        [9, 10,910],
    ]
    data = np.array(array)
    print(data[:2, 2])
