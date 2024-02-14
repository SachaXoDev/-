import csv
from datetime import*
def song_time(d,Ln,Ls):
    b = [int(i) for i in d.split('.')]
    a = (date(2023,5,12)-date(b[2],b[1],b[0])).days
    return int(abs(a/(len(Ln)+len(Ls)))*10_000)
    
    
with open('songs.csv', encoding = 'utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter = ';', quotechar ='"')
    answer = list(reader)[1:]

q = []
for i in answer:
    if i[0] == '0':
        i[0] = song_time(i[3],i[1],i[2])

with open('songs_new.csv','w', newline='',encoding='utf-8') as file:
    w = csv.writer(file)
    w.writerow(['streams','artist_name','track_name','date'])
    w.writerows(answer)


a = []
for i in answer:
    if int(i[3][-4:])<=2002:
        a.append([i[2],i[1],i[0]])
        print(' '.join([i[2],'-',i[1],'-',i[0]]))
print()

    
    
