def swap_case(s):
    case_name=""
    for i in s:
        if i.isupper():
            case_name+=i.lower()
        elif not i.isupper():
            case_name+=i.upper()
    return case_name

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
