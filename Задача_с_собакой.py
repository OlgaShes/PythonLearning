speedFriend1 = 4
speedFriend2 = 5
speedDog = 10
distance = 1000
distanceLimit = 10
count = 0
fromFriend = 1
while (distance > distanceLimit):
  if (fromFriend == 1):
    timeToMeet = distance / (speedDog + speedFriend2)
    distance = distance - timeToMeet * (speedFriend1 + speedFriend2)
    fromFriend = 2
    count = count + 1
  else :
    timeToMeet = distance / (speedDog + speedFriend1)
    distance = distance - timeToMeet * (speedFriend1 + speedFriend2)
    fromFriend = 1
    count = count + 1
print (count, "раз")