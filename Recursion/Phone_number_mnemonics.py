def phoneNumberMnemonics(phoneNumber):
    key_pad = {'0': '0', '1': '1', '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

    combinations = []

    bla(phoneNumber,key_pad,'',combinations)

    return combinations


def bla(phone_number,key_pad,combination,combinations):

    if phone_number == '':
        combinations.append(combination)

    else:
        for char in key_pad[phone_number[0]]:
            current_combination =  combination + char
            bla(phone_number[1:],key_pad,current_combination,combinations)


print(phoneNumberMnemonics('19145605'))

