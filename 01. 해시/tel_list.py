def inhead(tel, tel_len, lens, set_tel):

    for l in lens:

        if tel_len <= l:
            return False
        
        if tel[:l] in set_tel:
            return True

    return False



def solution(phone_book):

    set_tel = set()
    lens = []

    for tel in phone_book:

        tel_len = len(tel)

        for st in set_tel:
            if st.startswith(tel):
                return False

        if inhead(tel, tel_len, lens, set_tel):
            return False

        set_tel.add(tel)

        if tel_len not in lens:
            lens.append(tel_len)
            lens = sorted(lens)        

    return True


if __name__ == '__main__':

    data_list = [
        (["119", "97674223", "1195524421"], False),
        (["97674223", "1195524421", "119"], False),        
        (["123", "456", "789"],	True),
        (["12", "123", "1235", "567", "88"],	False)
    ]

    for data in data_list:
        print(data[0])

        if data[1] != solution(data[0]):
            print("error")
            print(data)
            break
