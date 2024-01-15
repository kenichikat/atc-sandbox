
S = str(input())

if all([
    S[0] == 'A',
    S[2:-1].count('C') == 1,
    S[1:].replace('A', '').replace('C', '').islower()
]):
    print('AC')
else:
    print('WA')
