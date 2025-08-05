import random, math
medium = ['binary', 'roadmap', 'talkmore', 'randompositon', 'electric']
hard = ['effective', 'strongerperson', 'whatapp', 'instagram', 'facebook']

useInputOfList = input('In which level you want to play, \n "Easy","Medium","Hard" : ').lower()

i = 0
if ('ea' in useInputOfList or useInputOfList == 1):
    easy = ['country', 'state', 'stage', 'words', 'power']; easy1 = list()
    while len(easy1) <= len(easy):
        h1 = random.randint(0,len(easy) - 1)
        if easy[h1] in easy1:
            pass
        else:
            easy1.append(easy[h1]); y1 = list(); d1 = math.floor(len(easy1[i]) / 2)
            print(easy[h1])
            for x1 in range(d1):
                h2 = random.randint(0, len(easy1[i]) - 1); y1 += [h2]
            # print(y1)
            c2 = 1; c3 = 0
            for c1 in range(len(y1)):
                c2 += c3; c3 += 1
            # print(c2)
            d2 = 0
            for d1 in range(2):
                for f1,f2 in enumerate(easy[h1]):
                    if y1[d2] == f1:
                        print(f2) 
                        pass    
                    else:
                        pass
                d2 += 1
            i += 1
elif ('me' in useInputOfList or useInputOfList == 2):
    pass
elif ('ha' in useInputOfList or useInputOfList == 3):
    pass
else:
    print('Correctly Fill a Valid Level To Play The Game. ("Easy","Medium","Hard")')