def req():
    with open('data.txt', 'r', encoding='utf-8') as file:
        data_file = []
        for line in file.readlines():
            l = line.split('\t')
            data_file.append(l)
    return data_file


if __name__ == '__main__':
    req()
