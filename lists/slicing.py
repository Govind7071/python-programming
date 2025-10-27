players = ['charles', 'martina', 'michael', 'florence', 'eli']
'''print(players[0:3])
print(players[-3:-1])
print(players[1:])
print(players[:3])'''
print(players[0:4])
print(players[0:4:2])#third argument give the items to be skipped
players2=players[:]#copy previous list in new one
print(players2)
players.append('smith')
players2.append('rahul')
print(players[:])
print(players2[:])