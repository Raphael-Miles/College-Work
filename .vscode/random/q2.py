worldRecord = False
lane = 1
athlete = input('Who is in lane ' + str(lane) + '? ')
country = input('Which country does ' + athlete + ' represent? ')
time = float(input('Enter the 100m time for: ' + athlete))

if time < 8.0 or time > 20.0:
    time = 'Invalid'
elif time < 9.58:
    worldRecord = True

print('Competitor: ' + athlete)
print('Country: ' + country)
print('Lane number: ' + str(lane))
print('100m time: ' + str(time))
print('New world record: ' + str(worldRecord))