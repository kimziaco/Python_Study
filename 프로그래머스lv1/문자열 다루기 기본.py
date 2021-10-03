s = "a234"

if len(s)== 4 or 6:
    print(s.isdigit())
else:
    print('False')

def solution(s):
    return s.isdigit() and len(s) in (4,6)
