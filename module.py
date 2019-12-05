class Character():
    health = 20
    character = ''
    
    """pick your character """   
    def chooseCharacter(self):
        num= input("Choose your character.\n \
                    1 ---> ʕ•ᴥ•ʔ \n \
                    2 --->(๑•̀ㅂ•́)ﻭ✧\n \
                    3 ---> (▀̿̿Ĺ̯̿▀̿ ̿) \n \
                    4 --->( ͡° ͜ʖ ͡°) ")
        if num == '1':
            self.character= 'ʕ•ᴥ•ʔ'
            return 'ʕ•ᴥ•ʔ'
        elif num == '2':
            self.character= '(๑•̀ㅂ•́)ﻭ✧'
            return '(๑•̀ㅂ•́)ﻭ✧'
        elif num == '3':
            self.character='(▀̿̿Ĺ̯̿▀̿ ̿) '
            return '(▀̿̿Ĺ̯̿▀̿ ̿) '
        elif num == '4':
            self.character= '( ͡° ͜ʖ ͡°)'
            return '( ͡° ͜ʖ ͡°)'
        else:
            self.character = 'ಠ_ಠ'
            return 'You had options and yet you didn\'t pick one so now you\'re this ಠ_ಠ'
        
    """formal representation of health status"""    
    def vitals(self):
        return "Your health level is at "+ str(self.health)
    
    """just health value"""
    def energy(self):
        return self.health
    
    """lowering of health (if wrong option is chosen)"""
    def hurt(self):
        self.health = self.health - 10
        
    def haveInjury(self):
        return "Your health level has been lowered to "+ str(self.health)
        
    """ first riddle told by pig"""    
    def riddle(self):
        solution = input("*PIG*: STOP, YOU MUST ANSWER MY RIDDLE TO CROSS THIS BRIDGE: \n \
                          This is a type of animal\n \
                          Which has a curly tail\n \
                          A female is called a sow\n \
                          And a boar is the male\n")
        if solution == 'pig' or solution == 'Pig':
            input("Dang that's pretty concided for a pig to make themself the answer\n \
                    but anyway congrats let's continue")
        else:
            self.hurt()
            input("whoops you got out smarted by a pig...\n \
                  but I'll let you pass, I'll just take off some health points" )
    
    """decision to fight or talk with the night"""
    def choices(self):
        response = input("What do you want to do fight or talk")
        if response == 'fight' or response == 'Fight':
            self.hurt()
            input("You really tried to fight A KNIGHT??? He has STEEL ARMOUR!\n \
                   Are you crazy?!? You definetely got hurt")
        else:
            input("Wow turns out the knight just wanted a friend to talk too. Congrats he let you through!")
        
