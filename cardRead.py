#!/usr/bin/python2

import sys
import getpass
from unixTime import unixTime

cardLog = {}

print 'Swipe your U card now.'

while True:
    raw = getpass.getpass('')
    swipeTime = unixTime()
    if raw == "":
        break

    #print '\t' + raw
    # track 1 begins with % and ends with ?
    # track 2 begins with ? and ends with ?
    start1 = raw.find('%')
    end1 = raw.find('?')
    track1 = raw[start1+1:end1]
    raw2 = raw[end1+1:]
    start2 = raw2.find(';')
    end2 = raw2.find('?')
    track2 = raw2[start2+1:end2]
    data1 = track1.split('^')
    
    if len(data1) < 6:
        badDataStr = "That's not a U card."
        print badDataStr
        say(badDataStr)
        continue

    idNum = data1[1]
    if idNum in cardLog:
        print "You've already swiped in, " + cardLog[idNum]['firstName'] + ' ' + cardLog[idNum]['lastName'] + '!'
        say("You've already swiped in!")
        continue

    fullNameReversed = data1[5]
    fullNameSplit = fullNameReversed.split(', ')
    firstName = fullNameSplit[1]
    lastName = fullNameSplit[0]
    fullNameProper = firstName + ' ' + lastName
    fullNameTts = fullNameProper.replace(' ', ', ') + '!'

    card = [idNum, lastName, firstName]
    cardLog[idNum] = {'time': unixTime(), 'lastName': lastName, 'firstName': firstName}

    print 'Hello, ' + fullNameProper + '!'

print cardLog
say ('Goodbye!')