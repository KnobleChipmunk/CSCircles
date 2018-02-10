width = int(input())

while width % 2 == 0:
    text = input()
    totalDots = chr(46) * (width - len(text))
    halfDots = int(width / 2)
    halfLen = len(text) / 2
    firstDots = chr(46) * (halfDots - int(halfLen))
    secondDots = chr(46) * (halfDots - int(halfLen))
   
    if text == "END":
        break
      
    elif len(text) % 2 != 0:
        secondDots = chr(46) * (halfDots - int(halfLen) - 1)
        print(firstDots+text+secondDots)
      
    elif len(text) % 2 == 0:
        print(firstDots+text+secondDots)
      
while width % 2 != 0:
    text = input()
    totalDots = chr(46) * (width - len(text))
    halfDots = int(width / 2)
    halfLen = len(text) / 2
    firstDots = chr(46) * (halfDots - int(halfLen))
    secondDots = chr(46) * (halfDots - int(halfLen))
   
    if text == "END":
        break
      
    elif len(text) % 2 != 0:
        print(firstDots+text+secondDots)
      
    elif len(text) % 2 == 0:
        firstDots = chr(46) * (halfDots - int(halfLen) + 1)
        print(firstDots+text+secondDots)
