import  string
import  random
import argparse

def create_password(len=8, upper=False, lower=False, digit=False, pun=False):

    pool = ''
    if upper:
        pool += string.ascii_uppercase

    if lower:
        pool += string.ascii_lowercase

    if digit:
        pool += string.digits

    if pun:
        pool += string.punctuation

    if pool == '':
        pool = string.ascii_letters

    return ''.join(random.choices(pool, k=len))


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('length', type=int, help="length of password")
    parser.add_argument('-u', '--upper', help="Upper Case Password", action="store_true")
    parser.add_argument('-l', '--lower', help="Lower Case Password", action="store_true")
    parser.add_argument('-d', '--digit', help=" Digit Password", action="store_true")
    parser.add_argument('-p', '--pun', help=" punctuation Password", action="store_true")

    args = parser.parse_args()

    print(create_password(args.length, args.upper, args.lower, args.digit, args.pun))