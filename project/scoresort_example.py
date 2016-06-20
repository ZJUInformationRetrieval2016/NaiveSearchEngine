import ScoreSort

query = ['statement','period','that','ended','on','Wednesday']
K = 20
print ('Search for: ')
print(query)
print('return top',K,'\n')
result = ScoreSort.sort(query,K)
for index in range(len(result)):
    print (result[index])
