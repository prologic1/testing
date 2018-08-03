#a= ['1ST PRIZE 0113\n2ND PRIZE 2962\n3RD PRIZE 8373\nSPECIAL\n7831\n1555\n2791\n6985\n0501\n0272\n6849\n7974\n8059\n5469\nCONSOLATION\n3200\n1845\n4438\n5016\n0824\n5750\n4756\n6654\n4565\n6362']
a= ['  Draw Date : 01/08/2018, Wednesday Draw No. : 4810/18  ', 'Prize payments guaranteed in full', 'TOTO 4D', 'First Prize Second Prize Third Prize', '6956 3439 7365', 'Special Prize', '0566 4699 6437 6887', '0363 8201 0388 1688',
    '  4822 1029  ', 'Consolation Prize', '9380 4829 5526 3848', '1692 9893 6845 3323', '  7295 4208  ',
    'TOTO 4D JACKPOT', 'Jackpot 1 RM 3,270,790.96', '6956 + 3439 6956 + 7365 3439 + 7365', '3439 + 6956 7365 + 6956 7365 + 3439',
    'Jackpot 2 RM 110,043.45', 'Matches any 1 of top 3 and any 1 of special winning numbers',
    'Toto lotto games - chances to become a millionaire!', '', 'SUPREME', 'TOTO 6/58 11 28 32 44 45 52',
    'Jackpot RM 13,955,396.68', 'POWER', 'TOTO 6/55 2 11 14 39 43 51', 'Jackpot RM 6,830,459.52',
    'STAR', 'TOTO 6/50 1 2 3 8 15 33 + 31', 'Jackpot 1 RM 2,926,478.48', 'Jackpot 2 RM 215,114.72', '',
    'Toto 5D & Toto 6D - prize payments guaranteed in full', 'TOTO',
    '5D 1st Prize 70473 4th Prize', '0473', '2nd Prize 88876 5th Prize', '473', '3rd Prize 91324 6th Prize', '73',
    'TOTO', '6D 1st Prize 192877', '2nd Prize 19287', 'or', '92877', '3rd Prize 1928', 'or', '2877', '4th Prize 192', 'or', '877', '5th Prize 19', 'or', '77']
new_array = []
new_array = a[4].splitlines();
#print(new_array)

for item in new_array:
    #print ("first prize:   "+a[4].splitlines()[0:3])
    #print(item[len(item)-4:len(item)])
    print("first prize: " +item[0:4])
    print("second prize: " + item[5:9])
    print("third prize: " + item[10:14])
    firstprize = item [0:4]
    secondprize = item [5:9]
    thirdprize = item[10:14]

print("***************************************************************************************************************")
#SPECIAL PRIZES
special_prize_array = a[6].splitlines();

for item in special_prize_array:
    print("s1:" +item[0:4])
    print("s2:" + item[5:9])
    print("s3:" + item[10:14])
    print("s4:" + item[15:19])

special_prize_array = a[7].splitlines();

for item in special_prize_array:
    print("s5:" + item[0:4])
    print("s6:" + item[5:9])
    print("s7:" + item[10:14])
    print("s8:" + item[15:19])

special_prize_array = a[8].splitlines();

for item in special_prize_array:
    print("s9:" + item[2:6])
    print("s10:" + item[7:11])
print("***************************************************************************************************************")
#CONSOLE PRIZES

special_prize_array = a[10].splitlines();

for item in special_prize_array:
    print("con1:" +item[0:4])
    print("con2:" + item[5:9])
    print("con3:" + item[10:14])
    print("con4:" + item[15:19])

special_prize_array = a[11].splitlines();

for item in special_prize_array:
    print("con5:" + item[0:4])
    print("con6:" + item[5:9])
    print("con7:" + item[10:14])
    print("con8:" + item[15:19])

special_prize_array = a[12].splitlines();

for item in special_prize_array:
    print("con9:" + item[2:6])
    print("con10:" + item[7:11])

print("***************************************************************************************************************")
#TOTO 5D PRIZES

special_prize_array = a[34].splitlines();

for item in special_prize_array:
    print("5D 1st: " +item[12:18])

special_prize_array = a[35].splitlines();

for item in special_prize_array:
    print("5D 4th: " +item[0:4])

special_prize_array = a[36].splitlines();

for item in special_prize_array:
    print("5D 2nd: " +item[10:15])

special_prize_array = a[37].splitlines();

for item in special_prize_array:
    print("5D 5th: " +item[0:3])

special_prize_array = a[38].splitlines();

for item in special_prize_array:
    print("5D 3rd: " +item[10:15])

special_prize_array = a[39].splitlines();

for item in special_prize_array:
    print("5D 6th: " +item[0:2])


print("***************************************************************************************************************")
#TOTO 6D

special_prize_array = a[41].splitlines();

for item in special_prize_array:
    print("6D 1st: " +item[13:19])

special_prize_array = a[42].splitlines();

for item in special_prize_array:
    print("6D 2nd_1: " +item[10:15])

special_prize_array = a[44].splitlines();

for item in special_prize_array:
    print("6D 2nd_2: " +item[0:5])

special_prize_array = a[45].splitlines();

for item in special_prize_array:
    print("6D 3rd_1: " +item[10:14])

special_prize_array = a[47].splitlines();

for item in special_prize_array:
    print("6D 3rd_2: " +item[0:4])

special_prize_array = a[48].splitlines();

for item in special_prize_array:
    print("6D 4th_1: " +item[10:13])

special_prize_array = a[50].splitlines();

for item in special_prize_array:
    print("6D 4th_2: " +item[0:4])

special_prize_array = a[51].splitlines();

for item in special_prize_array:
    print("6D 5th_1: " +item[10:12])

special_prize_array = a[53].splitlines();

for item in special_prize_array:
    print("6D 5th_2: " +item[0:2])