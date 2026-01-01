def s_validators(s):
    value = any(c.isalnum() for c in s)
    print(value)

    value = any(c.isalpha() for c in s)
    print(value)

    value = any(c.isdigit() for c in s)
    print(value)
    
    value = any(c.islower() for c in s)
    print(value)
    
    value = any(c.isupper() for c in s)
    print(value)

if __name__ == '__main__':
    s = input()
    s_validators(s)
