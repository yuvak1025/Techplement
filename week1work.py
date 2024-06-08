import random
import string

def gen_pwd(len, use_uc, use_lc, use_dig, use_spec):
    chars = ""
    if use_uc:
        chars += string.ascii_uppercase
    if use_lc:
        chars += string.ascii_lowercase
    if use_dig:
        chars += string.digits
    if use_spec:
        chars += string.punctuation

    if not chars:
        raise ValueError("No character types selected")

    pwd = ''.join(random.choice(chars) for _ in range(len))
    return pwd

def main():
    len = int(input("Enter the length of the password: "))
    use_uc = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
    use_lc = input("Include lowercase letters? (y/n): ").strip().lower() == 'y'
    use_dig = input("Include digits? (y/n): ").strip().lower() == 'y'
    use_spec = input("Include special characters? (y/n): ").strip().lower() == 'y'

    try:
        pwd = gen_pwd(len, use_uc, use_lc, use_dig, use_spec)
        print("Generated password:", pwd)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
