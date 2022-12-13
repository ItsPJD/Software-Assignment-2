import random

wholeGameLoop = True

endCounter = 0
ending1 = False
ending2 = False
ending3 = False
ending4 = False
ending5 = False
ending6 = False
ending7 = False
ending8 = False
ending9 = False
ending10 = False
ending11 = False
ending12 = False
ending13 = False

while wholeGameLoop:

  def mainMenu(endCount, end1, end2, end3, end4, end5, end6, end7, end8, end9, end10, end11, end12, end13):
    print("\n \n \n \n")
    print("==================")
    print("=== WELCOME TO ===")
    print("====== ZORK ======")
    print("================== \n")

    print("= ENDING ACHIEVEMENTS = \n")

    if endCount == 0:
      print("(You have not completed any endings yet.)")

    else:
      if end1 == True:
        print("'Vampire Slayer' (Achieve Ending 1.) \n")#throneRoom
      if end2 == True:
        print("'Where no one has gone before' (Achieve Ending 1 (and a bit).) \n")#northOfNorth
      if end3 == True:
        print("'Giving up' (Achieve Ending 2.) \n")#dungeon
      if end4 == True:
        print("'No pebbles allowed here' (Achieve Ending 2.5.) \n")#dungeon
      if end5 == True:
        print("'Learning to quit early' (Achieve Ending 3.) \n")#deeperDungeon
      if end6 == True:
        print("'Nothing to see here...' (Achieve Ending 4.) \n")#hollowEarth
      if end7 == True:
        print("'Looks like you're going to the shadow realm, Jimbo' (Achieve Ending 5.) \n")#abyssRealm
      if end8 == True:
        print("'Welcome to Los Rock'us Hermanos' (Achieve Ending 5.25.) \n")#LordOfStone
      if end9 == True:
        print("'Blood for the Blood God' (Achieve Ending 5.5.) \n")#sacrifice
      if end10 == True:
        print("'Is this just fantasy?' (Achieve Ending 6.) \n")#procedural
      if end11 == True:
        print("'Self Reflection and Improvement' (Achieve Ending 7.) \n")#despairShack
      if end12 == True:
        print("'Infernal Contraptions' (Achieve Ending 8.) \n")#shacktronic
      if end13 == True:
        print("'So... what's the catch?' (Achieve Ending 9.) \n") #fishingWorld

    print(str(endCount)+ "/13 ENDINGS UNLOCKED")

  mainMenu(endCounter, ending1, ending2, ending3, ending4, ending5, ending6, ending7, ending8, ending9, ending10, ending11, ending12, ending13)
  
  
  validClassNums = ["1", "2", "3", "4"]
  player1Health = " "
  player2Health = " "
  player1MaxHP = " "
  player2MaxHP = " "
  player1Dmg = " "
  player2Dmg = " "
  player1Min = " "
  player1Max = " "
  player2Min = " "
  player2Max = " "
  player1Class = " "
  player2Class = " "
  player1Weapon = " "
  player2Weapon = " "
  player1Heal = False
  player2Heal = False
  keyItem = False
  
  characterStats = {
    1: {
      "name":
      "Gorebrand, Brute of the West",
      "class":
      "Warrior",
      "weapon":
      "War Axe",
      "health":
      20,
      "weaponDmg":
      "4-7 damage",
      "maxHP":
      20,
      "weaponMin":
      4,
      "weaponMax":
      7,
      "description":
      "Raised in the bitter sands of Gildor, Gorebrand knows much of hardship. He has sworn not only to raise his lands back from the sea of glass that once swallowed his kin whole, but to defy the great evil that tears this world apart."
    },
    2: {
      "name":
      "Slakurn, Master of Keys",
      "class":
      "Rogue",
      "weapon":
      "Twin daggers",
      "health":
      25,
      "weaponDmg":
      "1-9 damage",
      "maxHP":
      25,
      "weaponMin":
      1,
      "weaponMax":
      9,
      "description":
      "Slakurn was born into a wealthy family in Alenfir, but after learning of their atrocities committed against the people they swore to protect, he ran and became a hero for the weak, and an omen to the wicked."
    },
    3: {
      "name":
      "Milandril, Protector of the Five",
      "class":
      "Paladin",
      "weapon":
      "Greatsword",
      "health":
      30,
      "weaponDmg":
      "4-5 damage",
      "maxHP":
      30,
      "weaponMin":
      4,
      "weaponMax":
      5,
      "description":
      "Once oathbound to the King of Alenfir, Milandril was blamed for the assassination of the very man he swore his life to defend. Now out for answers, he is now on a mission to outrun the approaching Eternal Eclipse to save his kingdom and his friends - no matter the cost."
    },
    4: {
      "name":
      "Cyrene, Mistress of Time",
      "class":
      "Sorcerer",
      "weapon":
      "Mythic Tome",
      "health":
      20,
      "weaponDmg":
      "2 - 10 damage",
      "maxHP":
      20,
      "weaponMin":
      2,
      "weaponMax":
      10,
      "description":
      "A half-human, half-elf woman, Cyrene was gifted with both the power of her elvish brethren, and the ambition of human nature. When her lands were brought down from the sky in the Event of the Falling Horizon, she took it upon herself to seek out the ends of the Earth and become the one true master of time - in the hopes that one day, the Fleeting City would rise again from the ashes."
    }
  }
  
  
  def showChar(stats, id):
    for items in stats:
      if items == id:
        name = stats[id]["name"]
        charClass = stats[id]["class"]
        weapon = stats[id]["weapon"]
        health = stats[id]["health"]
        damage = stats[id]["weaponDmg"]
        description = stats[id]["description"]
  
        print("--------------------------------------------")
        print("Name: " + name)
        print("Class: " + charClass)
        print("Weapon: " + weapon)
        print("HP: " + str(health))
        print("DMG: " + damage)
        print("Description: \n" + description)
  
  
  warriorName = "Gorebrand, Brute of the West"
  rogueName = "Slakurn, Master of Keys"
  paladinName = "Milandril, Protector of the Five"
  sorcererName = "Cyrene, Mistress of Time"
  print("\nPlayer 1, choose from one of these characters: ")
  showChar(characterStats, 1)
  showChar(characterStats, 2)
  showChar(characterStats, 3)
  showChar(characterStats, 4)
  print("------------------------------------")
  print("[1] " + warriorName + " [2] " + rogueName + " [3] " + paladinName + " [4] " + sorcererName)
  print("------------------------------------")
  Player1ChoiceLooping = True
  while Player1ChoiceLooping:
    try:
      Player1CharChoice = int(input("Player 1, Make your choice: "))
    except ValueError:
      print("Ivalid input, please try again.")
  
    else:
      for things in characterStats:
        if things == Player1CharChoice:
          player1Health = characterStats[Player1CharChoice]["health"]
          player1MaxHP = characterStats[Player1CharChoice]["maxHP"]
          player1Class = characterStats[Player1CharChoice]["class"]
          player1Dmg = characterStats[Player1CharChoice]["weaponDmg"]
          player1Min = characterStats[Player1CharChoice]["weaponMin"]
          player1Max = characterStats[Player1CharChoice]["weaponMax"]
          player1Weapon = characterStats[Player1CharChoice]["weapon"]
          Player1ChoiceLooping = False
  
  print("\n \n \n ")
  print("------------------------------------")
  print("PLAYER 1 HAS SELECTED")
  showChar(characterStats, Player1CharChoice)
  
  print("\n \n \n ")
  print("------------------------------------")
  print("Player 2, choose from one of these characters: ")
  print("------------------------------------")
  print("[1] " + warriorName + " [2] " + rogueName + " [3] " + paladinName + " [4] " + sorcererName)
  print("------------------------------------")
  
  Player2ChoiceLooping = True
  while Player2ChoiceLooping:
    try:
      Player2CharChoice = int(input("Player 2, Make your choice: "))
  
    except ValueError:
      print("Invalid input, please try again.")
  
    else:
      if Player2CharChoice == Player1CharChoice:
        print("Player 1 has already selected this class.")
      else:
        for things in characterStats:
          if things == Player2CharChoice:
            player2Health = characterStats[Player2CharChoice]["health"]
            player2MaxHP = characterStats[Player2CharChoice]["maxHP"]
            player2Class = characterStats[Player2CharChoice]["class"]
            player2Dmg = characterStats[Player2CharChoice]["weaponDmg"]
            player2Min = characterStats[Player2CharChoice]["weaponMin"]
            player2Max = characterStats[Player2CharChoice]["weaponMax"]
            player2Weapon = characterStats[Player2CharChoice]["weapon"]
            Player2ChoiceLooping = False
  
  print("\n \n \n ")
  print("------------------------------------")
  print("PLAYER 2 HAS SELECTED")
  showChar(characterStats, Player2CharChoice)
  print("\n \n \n ")
  
  enemyStats = {
    1: {
      "enemyName":"Skeleton ",
      "enemyHealth":10,
      "enemyMin":0,
      "enemyMax":4,
      "enemyStartQuip":"'You sh-shall not p-pass here mortals! I f-f-forbid it!' ",
      "enemyQuip1":"'I t-told you before m-mortals, My might is i-i-immense! Ha!' ",
      "enemyQuip2":"'I've still g-got a b-b-bone to pick with you two! Haha!' ",
      "enemyQuip3":"'Looks like y-you don't know w-when to give up do you? ",
      "enemyHitFailQuip":"'Oh. W-well, that's just... d-d-disappointing.' ",
      "enemyHurtDesc1":"The skeleton looks down at you as your blow hits them with a satisfying, chiming 'clink!'. The skeleton doesn't seem mad. Just disappointed. ",
      "enemyHurtDesc2":"The skeleton is knocked back by your blow, causing its bones to shake uncontrollably, and one in particular dislodges, falling to the ground and into dust. 'Look w-what you've done n-now! I spent c-centuries l-looking for that one! ",
      "enemyDeath":"'This is n-not the last y-you have seen of m-m-me!!' ",
      "enemyTalk1":"'I d-don't have time f-for conversing with you m-mortal! I got a joke book to r-read - it's a real b-bone tickler hehe!'",
      "enemyTalk2":"'You t-talk too much! Less chatting, m-more stabbing!'",
      "enemyTalk3":"'Hmm, f-fighting you is a bit t-tiring... yea- n-no! I won't give in to your n-nice words just yet m-mortal!'",
      "enemyTalkSuccess":"'F-fine, fine... I'll let you g-go... but d-don't tell my friends I d-did this for you! I h-have an image to uphold!'"
    },
    2: {
      "enemyName":"Rock Golem ",
      "enemyHealth":14,
      "enemyMin":0,
      "enemyMax":5,
      "enemyStartQuip":"'Hey... you uh, you ain't supposed to be here and all. Guess I gotta crush you's now.' ",
      "enemyQuip1":"'He... you's look funny when i squish you's with my fist... I'm gonna try that again.' ",
      "enemyQuip2":"'Why's you lookin' so sad... I'm havin's fun. '",
      "enemyQuip3":"'Come on you's... I'm only doings my job and all that... '",
      "enemyHitFailQuip":"'Aww, I missed... maybe I'll get you's next time around.' ",
      "enemyHurtDesc1":"You strike a blow at the Rock Golem, bashing at it's mighty bedrock body. The Rock Golem however, ignores you completely, looking down at its stone sudial watch, quitely counting the seconds away. It seems to want to be elsewhere... ",
      "enemyHurtDesc2":"You stike a powerful blow, loosening some cobbles from its body. The Rock Golem still doesn't seem to mind however, simply looking off into the distance with a somber look on it's face... Huh. You start to feel a bit bad for it now... ",
      "enemyDeath":"'Aww shucks... You's got me pretty good. I think I'm gonna goes lay down... for a while...' ",
      "enemyTalk1":"'Hey, no using thems words stuff on me... I ain't gots the patience for thems.'",
      "enemyTalk2":"'I gots places to be it's true... but I always gots times for crushing... hehe...'",
      "enemyTalk3":"'Don'ts be going using thems vocab-... vocabulo-... vocabulair-... oh yous making me feel stupid nows - not smart thing for yous to do!'",
      "enemyTalkSuccess":"'Okay... I guess you guys can goes... just makes sure to do some bashin' and crushin' for me would ya? hehehe...'"
    },
    3: {
      "enemyName": "Slime ",
      "enemyHealth": 15,
      "enemyMin": 0,
      "enemyMax": 6,
      "enemyStartQuip": "'I am the great slime! No other slime is better at DESTROYING than me!' ",
      "enemyQuip1": "'I, the great slime will squish you!' ",
      "enemyQuip2": "'You'll be CRUSHED to hear the bad news of your imminent deaths my friends!' ",
      "enemyQuip3": "'Fear me you fools!' ",
      "enemyHitFailQuip": "'Even the great almighty slime can make mistakes...' ",
      "enemyHurtDesc1": "'Ah! You dare to hit me?' ",
      "enemyHurtDesc2": "'Insects! You are but ants to the great slime!'",
      "enemyDeath": "'This is not the end! The great slime will return again...'",
      "enemyTalk1": "'I like your funny words, they make me feel even GREATER!'",
      "enemyTalk2": "'You think that talking me out of this is that easy? Ha!'",
      "enemyTalk3": "'You can't make me back down fools!'",
      "enemyTalkSuccess": "'I will leave you alive this time... but I shall return once more! The great slime decrees it so!'"
    },
    4: {
      "enemyName": "Zombie ",
      "enemyHealth": 12,
      "enemyMin": 0,
      "enemyMax": 3,
      "enemyStartQuip": "'Brains...'",
      "enemyQuip1": "'Must... eat... brains...' ",
      "enemyQuip2": "'urghhhhhhhh...'",
      "enemyQuip3": "'eat...brains...eat...more...'",
      "enemyHitFailQuip": "'urgh...'",
      "enemyHurtDesc1": "'urgh...'",
      "enemyHurtDesc2": "'rahhh! urghr...'",
      "enemyDeath": "'ughhhh....'",
      "enemyTalk1": "'brains...'",
      "enemyTalk2": "'urghhhh.'",
      "enemyTalk3": "'feed...more...'",
      "enemyTalkSuccess": "'will find...more...brains...'"
    }
  }
  
  bossStats = {
    1:{
      "bossName": "Orglond the Vile ",
      "bossHealth": 60,
      "bossMin": 2,
      "bossMax": 8,
      "bossStartQuip": "'Cower before me mortals, and despair!'",
      "bossQuip1": "'Pitiful... you are but ants before the heel of my might!'",
      "bossQuip2": "'If you were smarter, you would have given up by now...'",
      "bossQuip3": "'You are not a coward for fighting me - only a fool.'",
      "bossHurtDesc1": "'Your attempts at hurting me are laughable.'",
      "bossHurtDesc2": "'A pathetic excuse of a hit.'",
      "bossDeath": "'Impossible! You will regret this day mortals, I swear to you...'",
      "bossKeyItem": "Gilded Key of Orglond "
    },
    2:{
      "bossName": "Lord of Stone ",
      "bossHealth": 60,
      "bossMin": 2,
      "bossMax": 8,
      "bossStartQuip": "'...' - It doesn't say much. It's kind of just a pile of rocks.",
      "bossQuip1": "'...' Still a bunch of rocks. Not much conversation.",
      "bossQuip2": "'...' Doesn't seem to want to learn linguistics just yet.",
      "bossQuip3": "'...' Perhaps it would talk more if it carved out a mouth for itself? Those are usually useful for talking.",
      "bossHurtDesc1": "'...' - Seems to not care too much.",
      "bossHurtDesc2": "'...' - At least if it can't talk it can't hurt your feelings back, so... that's a victory I suppose?",
      "bossDeath": "'...' - The rocks fall to the ground. You win! - I guess...",
      "bossKeyItem": "Waters of Life "
    },
    3:{
      "bossName": "Shack O'Tronic ",
      "bossHealth": 60,
      "bossMin": 2,
      "bossMax": 8,
      "bossStartQuip": "'*Beep* *boop* you will be - destroyed!'",
      "bossQuip1": "'*Boop* *bop* computing your chances of success... *beep* *beep* ...0 percent.'",
      "bossQuip2": "'You are - *beep* *boop* pathetic.'",
      "bossQuip3": "'*bop* Did you think that was going to do anything?'",
      "bossHurtDesc1": "'*beep* *beep* *beep* Malfunctioning.'",
      "bossHurtDesc2": "'*beep* *boop* *bop* Internal systems damaged. Calling local repair manager... call failed - no phones have yet been invented for this feature, please consult the manual for further information.'",
      "bossDeath": "'*boop* *boop* shutting down...'",
      "bossKeyItem": "Shack O'Tronic Assembly Manual "
    },
    4:{
      "bossName": "The Big Catch ",
      "bossHealth": 60,
      "bossMin": 2,
      "bossMax": 8,
      "bossStartQuip": "'You'll be frying tonight fools - although this time, it's YOU who will be fried!'",
      "bossQuip1": "'You really think a small little thing like that is going to hurt me? Ha!'",
      "bossQuip2": "'Nice try, but you're in my domain now - time to die!'",
      "bossQuip3": "'I am NOT impressed by that, idiots.'",
      "bossHurtDesc1": "'I've met plankton that hit harder than you.'",
      "bossHurtDesc2": "'That *agh!* was nothing...'",
      "bossDeath": "'No...no... this *agh!* can't be...'",
      "bossKeyItem": "Fishie Food of Fear "
    }
  }
  
  def combatFunction(combat_stats, combat_player1Min, combat_player1Max,combat_player2Min, combat_player2Max, combat_player1Weapon,combat_player2Weapon):
                  
    global player1Health
    global player2Health
    global player1MaxHP
    global player2MaxHP
    global player1Heal
    global player2Heal
    global keyItem
  
    enemyRandom = random.randint(1, 4)
  
    for things in combat_stats:
      if things == enemyRandom:
        enemyName = combat_stats[enemyRandom]["enemyName"]
        enemyHealth = combat_stats[enemyRandom]["enemyHealth"]
        enemyMin = combat_stats[enemyRandom]["enemyMin"]
        enemyMax = combat_stats[enemyRandom]["enemyMax"]
        enemyStartQuip = combat_stats[enemyRandom]["enemyStartQuip"]
        enemyQuip1 = combat_stats[enemyRandom]["enemyQuip1"]
        enemyQuip2 = combat_stats[enemyRandom]["enemyQuip2"]
        enemyQuip3 = combat_stats[enemyRandom]["enemyQuip3"]
        enemyHitFailQuip = combat_stats[enemyRandom]["enemyHitFailQuip"]
        enemyHurtDesc1 = combat_stats[enemyRandom]["enemyHurtDesc1"]
        enemyHurtDesc2 = combat_stats[enemyRandom]["enemyHurtDesc2"]
        enemyDeath = combat_stats[enemyRandom]["enemyDeath"]
        enemyTalk1 = combat_stats[enemyRandom]["enemyTalk1"]
        enemyTalk2 = combat_stats[enemyRandom]["enemyTalk2"]
        enemyTalk3 = combat_stats[enemyRandom]["enemyTalk3"]
        enemyTalkSuccess = combat_stats[enemyRandom]["enemyTalkSuccess"]
  
    print("But before you can do anything, a " + enemyName + "appears!")
    print(enemyStartQuip)
  
    fightHealth = enemyHealth
    talkCountRandom = random.randint(4, 20)
    talkCounter = 0
  
    print("==================================================================")
    print("                     [COMBAT STARTED!]                            ")
    print("==================================================================")
    print("\n \n")
  
    fightLoop = True
    while fightLoop:
      print("=================")
      print("[ENEMY'S TURN]")
      print("=================")
      print("HP: " + str(fightHealth))
      print("\n")
      enemyRoll = random.randint(enemyMin, enemyMax)
      enemyPlayerChoose = random.randint(1, 2)
      if enemyPlayerChoose == 1:
        player1Health = player1Health - enemyRoll
      else:
        player2Health = player2Health - enemyRoll
  
      print("The " + enemyName + "hit player " + str(enemyPlayerChoose) +" for " + str(enemyRoll) + " damage!")
  
      quipChoose = random.randint(1, 3)
      if quipChoose == 1:
        print(enemyQuip1)
      elif quipChoose == 2:
        print(enemyQuip2)
      else:
        print(enemyQuip3)
  
      if player1Health <= 0 and player2Health <= 0:
        print("the " + enemyName +"was too much for our heroes! They fall to the ground instantly, their finals breaths drawn forever...")
        quipChoose = random.randint(1, 3)
        if quipChoose == 1:
          print(enemyQuip1)
        elif quipChoose == 2:
          print(enemyQuip2)
        else:
          print(enemyQuip3)
  
        fightLoop = False
        break
  
      elif enemyRoll == 0:
        print("(The " + enemyName + "didn't really do anything...)")
        print(enemyHitFailQuip)
  
      else:
        pass
  
      player1Loop = True
  
      if player1Health <= 0:
        player1Loop = False
      else:
        while player1Loop:
          print("=================")
          print("[PLAYER 1'S TURN]")
          print("=================")
          print("HP: " + str(player1Health))
          print("\n")
          print("YOU CAN: [1] TALK [2] OPEN INVENTORY [3] FIGHT")
          print("\n")
          try:
            player1Input = str(input("What would you like to do?: "))
          except ValueError:
            print("Invalid input, please try again.")
          else:
            if player1Input == "1":
              print("\n")
              print("You talk to the " + enemyName + ".")
              talkCounter = talkCounter + 1
              if talkCounter == talkCountRandom:
                print(enemyTalkSuccess)
                player1Loop = False
                break
  
              else:
                enemyTalkRandom = random.randint(1, 3)
                if enemyTalkRandom == 1:
                  print(enemyTalk1)
                elif enemyTalkRandom == 2:
                  print(enemyTalk2)
                else:
                  print(enemyTalk3)
                print("\n")
                print("(You haven't quite convinced it yet...)")
                player1Loop = False
  
            elif player1Input == "2":
              print("Player 1 opens their inventory.")
              if player1Heal:
                print("HP POTION: ACTIVE")
              else:
                print("HP POTION: EMPTY")
  
              if keyItem:
                print("KEY ITEM: ACTIVE")
              else:
                print("KEY ITEM: EMPTY")
  
              if player1Heal == False and keyItem == False:
                print("You can't use anything right now.")
              else:
                try:
                  player1InvInput = int(
                    input("SELECT AN ITEM: [1] HEALTH [2] KEY ITEM: "))
                except ValueError:
                  print("Invalid input, please try again.")
                else:
                  if player1InvInput == 1:
                    if player1Heal == True:
                      useHeal1 = input("Would you like to use this item? [y/n]: ")
                      if useHeal1 == "y":
                        if player1Health == player1MaxHP:
                          print("You are already at Maximum Health.")
                        else:
                          player1Health = player1Health + 5
                          if player1Health >= player1MaxHP:
                            player1Health == player1MaxHP
                          print("You have used a health potion. Your current HP is: "+ str(player1Health))
                      else:
                        pass
                    else:
                      print("You do not have anything in this slot at the moment.")
                      pass
  
                  elif player1InvInput == 2:
                    if keyItem == True:
                      keyItemUse = input("Would you like to use this key item? (NOTE: This is only effective on boss enemies.) [y/n]: ")
                      if keyItemUse == "y":
                        print("You used the key item.")
  
                      else:
                        pass
  
                  else:
                    pass
  
              print("You close your inventory.")
  
            elif player1Input == "3":
              player1Roll = random.randint(combat_player1Min, combat_player1Max)
              print("\n")
              print("Player 1 hit " + enemyName + "for " + str(player1Roll) +" damage!")
              print("======================")
              if player1Roll < 2:
                print("Player 1 tries maiming " + enemyName + "with their " +combat_player1Weapon +", but it doesn't seem to do much. Perhaps they should have just stayed at home and took a nap.")
              else:
                print("Player 1 strikes out at the " + enemyName +"with their mighty " + combat_player1Weapon +", and pummels the foul creature, dealing great pain to their foe.")
                enemyHurt1 = random.randint(1, 2)
                if enemyHurt1 == 1:
                  print(enemyHurtDesc1)
                else:
                  print(enemyHurtDesc2)
  
              fightHealth = fightHealth - player1Roll
              if fightHealth <= 0:
                print("------------------------")
                print("You defeated the " + enemyName + "!")
                print("------------------------")
                print(enemyDeath)
  
                if player2Health == 0 and player1Health != 0:
                  print("Their foe slain, Player 1 appraoches their companion, and whisper a short spell of rejuvination. Their partner rises from the grave, feeling slightly sick but otherwise well. Player 2's health is set to 5.")
                  player1Health = player1Health + 5
  
                else:
                  pass
                player1Loop = False
              else:
                player1Loop = False
                pass
  
            else:
              print("Invalid input, please try again.")
  
      if fightHealth <= 0:
        fightLoop = False
        break
  
      if talkCounter == talkCountRandom:
        fightLoop = False
        break
  
      player2Loop = True
  
      if player2Health <= 0:
        player2Loop = False
      else:
        while player2Loop:
          print("=================")
          print("[PLAYER 2'S TURN]")
          print("=================")
          print("HP: " + str(player2Health))
          print("\n")
          print("YOU CAN: [1] TALK [2] OPEN INVENTORY [3] FIGHT")
          print("\n")
          try:
            player2Input = str(input("What would you like to do?: "))
          except ValueError:
            print("Invalid input, please try again.")
          else:
            if player2Input == "1":
              print("\n")
              print("You talk to the " + enemyName + ".")
              talkCounter = talkCounter + 1
  
              if talkCounter == talkCountRandom:
                print(enemyTalkSuccess)
                player2Loop = False
  
              else:
                enemyTalkRandom = random.randint(1, 3)
                if enemyTalkRandom == 1:
                  print(enemyTalk1)
                elif enemyTalkRandom == 2:
                  print(enemyTalk2)
                else:
                  print(enemyTalk3)
                print("\n")
                print("(You haven't quite convinced it yet...)")
                player2Loop = False
  
            elif player2Input == "2":
              print("Player 1 opens their inventory.")
              if player2Heal:
                print("HP POTION: ACTIVE")
              else:
                print("HP POTION: EMPTY")
  
              if keyItem:
                print("KEY ITEM: ACTIVE")
              else:
                print("KEY ITEM: EMPTY")
  
              if player2Heal == False and keyItem == False:
                print("You can't use anything right now.")
              else:
                try:
                  player2InvInput = int(
                    input("SELECT AN ITEM: [1] HEALTH [2] KEY ITEM: "))
                except ValueError:
                  print("Invalid input, please try again.")
                else:
                  if player2InvInput == 1:
                    if player2Heal == True:
                      useHeal2 = input("Would you like to use this item? [y/n]: ")
                      if useHeal2 == "y":
                        if player2Health == player2MaxHP:
                          print("You are already at Maximum Health.")
                        else:
                          player2Health = player2Health + 5
                          if player2Health >= player2MaxHP:
                            player2Health == player2MaxHP
                          print("You have used a health potion. Your current HP is: "+ str(player1Health))
                      else:
                        pass
                    else:
                      print("You do not have anything in this slot at the moment.")
                      pass
  
                  elif player2InvInput == 2:
                    if keyItem == True:
                      keyItemUse = input("Would you like to use this key item? (NOTE: This is only effective on boss enemies.) [y/n]: ")
                      if keyItemUse == "y":
                        print("You used the key item.")
  
                      else:
                        pass
  
                  else:
                    pass
  
              print("You close your inventory.")
  
            elif player2Input == "3":
              player2Roll = random.randint(combat_player2Min, combat_player2Max)
              print("\n")
              print("Player 2 hit " + enemyName + "for " + str(player2Roll) + " damage!")
              print("=================")
              if player2Roll < 2:
                print("Player 2 tries maiming " + enemyName + "with their " + combat_player2Weapon +", but it doesn't seem to do much. Perhaps they should have just stayed at home and took a nap.")
              else:
                print("Player 2 strikes out at the " + enemyName +"with their mighty " + combat_player2Weapon +", and pummels the foul creature, dealing great pain to their foe.")
                enemyHurt1 = random.randint(1, 2)
                if enemyHurt1 == 1:
                  print(enemyHurtDesc1)
                else:
                  print(enemyHurtDesc2)
  
              fightHealth = fightHealth - player2Roll
              if fightHealth <= 0:
                print("------------------------")
                print("You defeated the " + enemyName + "!")
                print("------------------------")
                print(enemyDeath)
  
                if player1Health == 0 and player2Health != 0:
                  print(
                    "Their foe slain, Player 2 appraoches their companion, and whisper a short spell of rejuvination. Their partner rises from the grave, feeling slightly sick but otherwise well. Player 1's health is set to 5."
                  )
                  player1Health = player1Health + 5
  
                else:
                  pass
                player2Loop = False
              else:
                player2Loop = False
                pass
  
            else:
              print("Invalid input, please try again.")
  
      if fightHealth <= 0:
        fightLoop = False
        break
  
      if talkCounter == talkCountRandom:
        fightLoop = False
        break
  
    if player1Health <= 0 and player2Health <= 0:
      print("==================================================================")
      print("                     [YOU BOTH DIED!]                             ")
      print("==================================================================")
    else:
      print("==================================================================")
      print("                     [ENEMY DEFEATED!]                            ")
      print("==================================================================")
  
    return player1Health
    return player2Health
  
  
  def bossFunction(combat_player1Min, combat_player1Max,combat_player2Min, combat_player2Max, combat_player1Weapon,combat_player2Weapon, bossNumber):
  
    global bossStats
    global player1Health
    global player2Health
    global player1MaxHP
    global player2MaxHP
    global player1Heal
    global player2Heal
    global keyItem
    
  
    for things in bossStats:
      if things == bossNumber:
        enemyName = bossStats[bossNumber]["bossName"]
        enemyHealth = bossStats[bossNumber]["bossHealth"]
        enemyMin = bossStats[bossNumber]["bossMin"]
        enemyMax = bossStats[bossNumber]["bossMax"]
        enemyStartQuip = bossStats[bossNumber]["bossStartQuip"]
        enemyQuip1 = bossStats[bossNumber]["bossQuip1"]
        enemyQuip2 = bossStats[bossNumber]["bossQuip2"]
        enemyQuip3 = bossStats[bossNumber]["bossQuip3"]
        enemyHurtDesc1 = bossStats[bossNumber]["bossHurtDesc1"]
        enemyHurtDesc2 = bossStats[bossNumber]["bossHurtDesc2"]
        enemyDeath = bossStats[bossNumber]["bossDeath"]
        enemyKeyItem = bossStats[bossNumber]["bossKeyItem"]
  
  
    print(enemyName+ "has appeared!")
    print(enemyStartQuip)
  
    fightHealth = enemyHealth
  
    print("==================================================================")
    print("                     [COMBAT STARTED!]                            ")
    print("==================================================================")
    print("\n \n")
    if keyItem == True:
      print("The " +enemyKeyItem+ "begins to glow - " +enemyName+ "takes a heavy toll! [Boss HP has been reduced by 50%]")
      fightHealth = fightHealth - 30
      
    fightLoop = True
    while fightLoop:
      print("=================")
      print("[ENEMY'S TURN]")
      print("=================")
      print("HP: " + str(fightHealth))
      print("\n")
      enemyRoll = random.randint(enemyMin, enemyMax)
      enemyPlayerChoose = random.randint(1, 2)
      if enemyPlayerChoose == 1:
        player1Health = player1Health - enemyRoll
      else:
        player2Health = player2Health - enemyRoll
  
      print("The " + enemyName + "hit player " + str(enemyPlayerChoose) + " for " + str(enemyRoll) + " damage!")
  
      quipChoose = random.randint(1, 3)
      if quipChoose == 1:
        print(enemyQuip1)
      elif quipChoose == 2:
        print(enemyQuip2)
      else:
        print(enemyQuip3)
  
      if player1Health <= 0 and player2Health <= 0:
        print(enemyName + "was too much for our heroes! They fall to the ground instantly, their finals breaths drawn forever...")
        quipChoose = random.randint(1, 3)
        if quipChoose == 1:
          print(enemyQuip1)
        elif quipChoose == 2:
          print(enemyQuip2)
        else:
          print(enemyQuip3)
  
        fightLoop = False
        break
  
      else:
        pass
  
      player1Loop = True
  
      if player1Health <= 0:
        player1Loop = False
      else:
        while player1Loop:
          print("=================")
          print("[PLAYER 1'S TURN]")
          print("=================")
          print("HP: " + str(player1Health))
          print("\n")
          print("YOU CAN: [1] OPEN INVENTORY [2] FIGHT")
          print("\n")
          try:
            player1Input = str(input("What would you like to do?: "))
          except ValueError:
            print("Invalid input, please try again.")
          else:
            if player1Input == "1":
              print("Player 1 opens their inventory.")
              if player1Heal:
                print("HP POTION: ACTIVE")
              else:
                print("HP POTION: EMPTY")
  
              if keyItem:
                print("KEY ITEM: ACTIVE")
              else:
                print("KEY ITEM: EMPTY")
  
              if player1Heal == False and keyItem == False:
                print("You can't use anything right now.")
              else:
                try:
                  player1InvInput = int(input("SELECT AN ITEM: [1] HEALTH [2] KEY ITEM: "))
                except ValueError:
                  print("Invalid input, please try again.")
                else:
                  if player1InvInput == 1:
                    if player1Heal == True:
                      useHeal1 = input(
                        "Would you like to use this item? [y/n]: ")
                      if useHeal1 == "y":
                        if player1Health == player1MaxHP:
                          print("You are already at Maximum Health.")
                        else:
                          player1Health = player1Health + 5
                          if player1Health >= player1MaxHP:
                            player1Health == player1MaxHP
                          print(
                            "You have used a health potion. Your current HP is: "
                            + str(player1Health))
                      else:
                        pass
                    else:
                      print(
                        "You do not have anything in this slot at the moment.")
                      pass
  
                  elif player1InvInput == 2:
                    if keyItem == True:
                      print("Key Item is currently in use.")
  
                    else:
                      pass
  
                  else:
                    pass
  
              print("You close your inventory.")
  
            elif player1Input == "2":
              player1Roll = random.randint(combat_player1Min, combat_player1Max)
              print("\n")
              print("Player 1 hit " + enemyName + "for " + str(player1Roll) +" damage!")
              print("======================")
              if player1Roll < 2:
                print("Player 1 tries maiming " + enemyName + "with their " +combat_player1Weapon +", but it doesn't seem to do much. Perhaps they should have just stayed at home and took a nap.")
              else:
                print("Player 1 strikes out at the " + enemyName +"with their mighty " + combat_player1Weapon +", and pummels the foul creature, dealing great pain to their foe.")
                enemyHurt1 = random.randint(1, 2)
                if enemyHurt1 == 1:
                  print(enemyHurtDesc1)
                else:
                  print(enemyHurtDesc2)
  
              fightHealth = fightHealth - player1Roll
              if fightHealth <= 0:
                print("------------------------")
                print("You defeated the " + enemyName + "!")
                print("------------------------")
                print(enemyDeath)
  
                if player2Health == 0 and player1Health != 0:
                  print("Their foe slain, Player 1 appraoches their companion, and whisper a short spell of rejuvination. Their partner rises from the grave, feeling slightly sick but otherwise well. Player 2's health is set to 5.")
                  player1Health = player1Health + 5
  
                else:
                  pass
                player1Loop = False
              else:
                player1Loop = False
                pass
  
            else:
              print("Invalid input, please try again.")
  
      if fightHealth <= 0:
        fightLoop = False
        break
  
      player2Loop = True
  
      if player2Health <= 0:
        player2Loop = False
      else:
        while player2Loop:
          print("=================")
          print("[PLAYER 2'S TURN]")
          print("=================")
          print("HP: " + str(player2Health))
          print("\n")
          print("YOU CAN: [1] OPEN INVENTORY [2] FIGHT")
          print("\n")
          try:
            player2Input = str(input("What would you like to do?: "))
          except ValueError:
            print("Invalid input, please try again.")
          else:
            if player2Input == "1":
              print("Player 1 opens their inventory.")
              if player2Heal:
                print("HP POTION: ACTIVE")
              else:
                print("HP POTION: EMPTY")
  
              if keyItem:
                print("KEY ITEM: ACTIVE")
              else:
                print("KEY ITEM: EMPTY")
  
              if player2Heal == False and keyItem == False:
                print("You can't use anything right now.")
              else:
                try:
                  player2InvInput = int(input("SELECT AN ITEM: [1] HEALTH [2] KEY ITEM: "))
                except ValueError:
                  print("Invalid input, please try again.")
                else:
                  if player2InvInput == 1:
                    if player2Heal == True:
                      useHeal2 = input(
                        "Would you like to use this item? [y/n]: ")
                      if useHeal2 == "y":
                        if player2Health == player2MaxHP:
                          print("You are already at Maximum Health.")
                        else:
                          player2Health = player2Health + 5
                          if player2Health >= player2MaxHP:
                            player2Health == player2MaxHP
                          print(
                            "You have used a health potion. Your current HP is: "
                            + str(player1Health))
                      else:
                        pass
                    else:
                      print("You do not have anything in this slot at the moment.")
                      pass
  
                  elif player2InvInput == 2:
                    if keyItem == True:
                      print("Key Item is already in use.")
  
                    else:
                      pass
  
                  else:
                    pass
  
              print("You close your inventory.")
  
            elif player2Input == "2":
              player2Roll = random.randint(combat_player2Min, combat_player2Max)
              print("\n")
              print("Player 2 hit " + enemyName + "for " + str(player2Roll) + " damage!")
              print("=================")
              if player2Roll < 2:
                print("Player 2 tries maiming " + enemyName + "with their " +combat_player2Weapon + ", but it doesn't seem to do much. Perhaps they should have just stayed at home and took a nap.")
              else:
                print("Player 2 strikes out at the " + enemyName +"with their mighty " + combat_player2Weapon +", and pummels the foul creature, dealing great pain to their foe.")
                enemyHurt1 = random.randint(1, 2)
                if enemyHurt1 == 1:
                  print(enemyHurtDesc1)
                else:
                  print(enemyHurtDesc2)
  
              fightHealth = fightHealth - player2Roll
              if fightHealth <= 0:
                print("------------------------")
                print("You defeated " + enemyName + "!")
                print("------------------------")
                print(enemyDeath)
  
                if player1Health == 0 and player2Health != 0:
                  print("Their foe slain, Player 2 appraoches their companion, and whisper a short spell of rejuvination. Their partner rises from the grave, feeling slightly sick but otherwise well. Player 1's health is set to 5.")
                  player1Health = player1Health + 5
  
                else:
                  pass
                player2Loop = False
              else:
                player2Loop = False
                pass
  
            else:
              print("Invalid input, please try again.")
  
      if fightHealth <= 0:
        fightLoop = False
        break
  
    if player1Health <= 0 and player2Health <= 0:
      print("==================================================================")
      print("                     [YOU BOTH DIED!]                             ")
      print("==================================================================")
    else:
      print("==================================================================")
      print("                     [ENEMY DEFEATED!]                            ")
      print("==================================================================")
  
    return player1Health
    return player2Health
  def looting():
    global player1Heal
    global player2Heal
    global keyItem
  
    lootRandom = random.randint(1, 10)
    lootChance = True
    while lootChance:
      if lootRandom <= 3:
        print("You found an HP Potion! Who would you like to give it to?")
        print("=== [1] Player 1 [2] Player 2 ===")
        try:
          hpChoice = int(input())
        except ValueError:
          print("Invalid input, please try again.")
        else:
          if hpChoice == 1:
            print("Player 1 has been given the HP potion.")
            player1Heal = True
            lootChance = False
  
          elif hpChoice == 2:
            print("Player 2 has been given the HP potion.")
            player2Heal = True
            lootChance = False
  
          else:
            print("Invalid input. Please try again.")
      else:
        print("You look around, but find nothing to take.")
        lootChance = False
  
    return player1Heal
    return player2Heal
    return keyItem
  
  
  def courtyardStart0():
  
    global player1Health
    global player2Health
    global enemyStats
    global player1Min
    global player1Max
    global player2Min
    global player2Max
    global player1Weapon
    global player2Weapon
  
    print("You are standing in a moldy, ancient courtyard. It is cold and the sun is setting over the mountainous horizon. To the north atop a cliff lies a vampiric like castle - leading to it is a narrow pathway up and a rickety bridge in front of you. To the south and east lies thick, brambled forest. To the west is a dimly lit entrance to the local village. \n")
    courtyardLoop = True
    while courtyardLoop:
      print("What would you like to do? ")
      CourtyardInput = input()
  
      north = ["north"]
      west = ["west"]
      for word in CourtyardInput.split():
        if word in north:
          northBridge1()
          courtyardLoop = False
        elif word in west:
          westGate4()
          courtyardLoop = False
  
  
  def northBridge1():
  
    global player1Health
    global player2Health
    global enemyStats
    global player1Min
    global player1Max
    global player2Min
    global player2Max
    global player1Weapon
    global player2Weapon
    global player1Heal
    global player2Heal
    global keyItem
  
    print(
      "\n You head north towards the old bridge. The drop below seems to have no end, and the smell of the decaying wood is putrid, so much so it feels unnatural -  other, more malicious forces are definitely at work here. A few crates are situated to your left, and a broken down cart to the right. The way is blocked from all sides except for heading straight north again, where the perilous path up towards the castle lies."
    )
    northBridgeEnemyRoll = random.randint(1, 10)
    if northBridgeEnemyRoll in range(1, 4 + 1):
      combatFunction(enemyStats, player1Min, player1Max, player2Min, player2Max,
                     player1Weapon, player2Weapon)
      print(
        "After the fight is over, you both take a while to take in your surroundings again."
      )
  
    roomLoop = True
    while roomLoop:
      print(
        "There are crates situated to the left of you, and a broken down cart to your right. The way is blocked on all sides except for the north, which leads over the bridge and towards the castle atop the hill."
      )
      print("==========================")
      print("What would you like to do?")
      northBridgeInput = input()
  
      cart = ["cart"]
      north = ["north"]
      crates = ["crate", "crates"]
  
      for word in northBridgeInput.split():
        if word in north:
          castleGate1()
          roomLoop = False
        elif word in cart:
          looting()
          print(
            "You look around further at the broken down cart. The wood has splintered greatly and the wheels seemingly torn off from their axels by a great force. Whatever did this is not something to treat as weak... nor as an ally."
          )
          print(
            "You move back from the crates and contemplate your options again.")
        elif word in crates:
          looting()
          print(
            "After looking for provisions, you notice a strange mark on the side of the crates - a seared brand depicting a bleeding sun peering down at a vast mountain. You don't know what it means, but it doesn't look very friendly..."
          )
          print(
            "You move away from the cart, being careful not to trip over the decaying bodies of the poor horses that onced pulled it, and start to consider your options again."
          )
  
  
  def castleGate1():
    global player1Health
    global player2Health
    global enemyStats
    global player1Min
    global player1Max
    global player2Min
    global player2Max
    global player1Weapon
    global player2Weapon
    global player1Heal
    global player2Heal
    global keyItem
  
    print(
      "\n You arrive at the grand gates of the castle. Spires and columns rise up from the rocky floor beneath you as the gates glow a faint red, before opening themselves violently, the metal bashing against the stone brick that creates the walls either side of the entrance way. It seems that the only way forward is through the gates and into the main hall of the castle - but looking closer, you notice that a small crack in the wall can be seen between the rocky mountainside cliff to the east, and a small shack sat atop a lone cliff edge to the west..."
    )
    castleGateEnemyRoll = random.randint(1, 10)
    if castleGateEnemyRoll in range(1, 4 + 1):
      combatFunction(enemyStats, player1Min, player1Max, player2Min, player2Max,
                     player1Weapon, player2Weapon)
      print(
        "After the fight is over, you both take a while to take in your surroundings again."
      )
  
    roomLoop = True
    while roomLoop:
      print(
        "\n The castle gates have opened and you can head north to enter the main hall - however, you also notice a small shack to the west atop the cliff edge, and a mysterious crack in the mountainside wall to the east..."
      )
      print("==========================")
      print("What would you like to do?")
  
      castleGateInput = input()
  
      north = ["north", "ahead", "forward"]
      west = ["shack", "west", "cliff", "cliffs"]
      east = ["crack", "mountainside", "east"]
  
      for word in castleGateInput.split():
        if word in north:
          mainHall1()
          roomLoop = False
        elif word in west:
          westShack5()
          roomLoop = False
        elif word in east:
          mountainCrack3()
          roomLoop = False
  
  
  def mainHall1():
  
    global player1Health
    global player2Health
    global enemyStats
    global player1Min
    global player1Max
    global player2Min
    global player2Max
    global player1Weapon
    global player2Weapon
    global player1Heal
    global player2Heal
    global keyItem
  
    print("\n You stand in the great main hall of the castle. A large glowing chest sits in the centre, glimmering in the dim light. The brick in the walls are black and aged, and a faint laugh can be heard cackling in the dark. You see great steps leading to a chamber north of you - however, there is also a door to the east that seems to beckon you both, as though it wants to show you something...")
    mainHallRoll = random.randint(1, 10)
    if mainHallRoll in range(1, 4 + 1):
      combatFunction(enemyStats, player1Min, player1Max, player2Min, player2Max, player1Weapon, player2Weapon)
      print("After the fight is over, you both take a while to take in your surroundings again.")
      
    roomLoop = True
    while roomLoop:
      print("\n You are in the main hall. In the centre of the room lies a gleaming chest. To the north lies a grand chamber, and to the east a strange room is beckoning you over to investigate.")
      print("==========================")
      print("What would you like to do?")
      mainHallInput = input()
  
      north = ["north", "ahead","forward"]
      east = ["east", "right"]
      chest = ["chest", "box"]
  
      for word in mainHallInput.split():
        if word in north:
          northChamber1()
          roomLoop = False
        elif word in east:
          eastChamber2()
          roomLoop = False
        elif word in chest:
          looting()
          print("The chest is ornate and shining, a strange departure from everything else you have seen on your travels. The gold glistens perfectly, as if it were alive - as if it were calling out to you to look closer...")      
          print("You step away from the chests, trying to resist the temptation to haul it along with you for retirement purposes, as you consider your options again.")
  
  
  def northChamber1():
      
    global player1Health
    global player2Health
    global enemyStats
    global player1Min
    global player1Max
    global player2Min
    global player2Max
    global player1Weapon
    global player2Weapon
    global player1Heal
    global player2Heal
    global keyItem
    
    print("\n Entering the north chamber, a myriad of banners and drapes fall from the lofty ceiling, depicting the great Vampiric King Orglond the Vile. The ground begins to shake as a crack in the north wall opens up, a great throne room lying ahead. There is no escaping this fate... you are destined to end the king's vile reign - this is why you journeyed north, and to the north, and to the north again... However, you also see a pile of bodies, drained of life and soul - perhaps they have some items of use before your final battle begins...")
    northChamberRoll = random.randint(1, 10)
    if northChamberRoll in range(1, 4 + 1):
      combatFunction(enemyStats, player1Min, player1Max, player2Min, player2Max, player1Weapon, player2Weapon)
      print("After the fight is over, you both take a while to take in your surroundings again.")
  
    roomLoop = True
    while roomLoop:
      print("\n You are in the north chamber. To the north lies your epic battle with Vampiric King Orglond the Vile. You can move ahead now and face him, or loot the bodies in front of you for some supplies before the final showdown...")
      print("==========================")
      print("What would you like to do?")
      northChamberInput = input()
  
      north = ["north", "forward", "ahead"]
      bodies = ["bodies", "pile", "body"]
      
      for word in northChamberInput.split():   
        if word in north:
          throneRoom1END()
          roomLoop = False
        elif word in bodies:
          looting()
          print("Amongst the bodies you also notice something strange - a golden key, a big red jewel beset into its core. It seems important...")
          keyItem = True
          print("== You have picked up a Key Item: Gilded Key of Orglond == ")
          print("You step back from the bodies, partly to go fight the vampire king, but mostly because of the smell, and decide what you want to do.")
  
  
  def throneRoom1END():
    global ending1
    global endCounter
    global player1Health
    global player2Health
    global enemyStats
    global player1Min
    global player1Max
    global player2Min
    global player2Max
    global player1Weapon
    global player2Weapon
    global player1Heal
    global player2Heal
    global keyItem
    
    print("You stand in the throne room of the castle. Before you stands the Vampiric King Orglond the Vile, Lord of the Night.")
    print("'You think you can defeat me, mortals?' Orglond sneers, unsheathing his great blade from its scabbard.")
    print("'I will show you... the true meaning... of PAIN!!'")
    print("It seems as though there is no other option - a fight to the death it will be. [type 'fight' to begin the boss battle.]")
    
    roomLoop = True
    while roomLoop:
      print("==========================")
      print("What would you like to do?")
      throneRoomInput = input()
  
      fight = ["fight", "battle", "combat"]
      north = ["north", "ahead","forward"]
      
      for word in throneRoomInput.split():   
        if word in fight:
          bossFunction(player1Min, player1Max, player2Min, player2Max, player1Weapon, player2Weapon, 1)
          if player1Health <= 0 and player2Health <= 0:
            roomLoop = False
          else:
            print("The horrific King defeated, the pair of you look up as the sun begins to shine through the blood red stained glass window placed in the ceiling. You have both saved the castle- and perhaps the world - from certain doom.")
            print("========================================================")
            print("============== ENDING 1: END OF A REIGN ================")
            print("========================================================")

            if ending1 == False:
              endCounter = endCounter + 1
              ending1 = True
              
            roomLoop = False 
        elif word in north:
          northOfNorth1END()
          roomLoop = False
        
  def northOfNorth1END():
    global ending2
    global endCounter
    
    print("Orglond the Vile stands before you - but heading north is more important. You push past him as he looks on in shock as you break down the north wall of the throne room, and into the snow riddled mountains beyond.")
    print("You walk north first, then a bit more north. Then after camping down for a little while, you walk north some more. You have been walking north for so long, ever since you stepped foot in these lands you have no idea of what else to do.")
    print("At last you reach the north of the north - A place more northerly than any other northern point of the northern world. You both stand there, proud of your accomplishments - perhaps the real heading north was the friends we made along the way.")
    print("========================================================")
    print("===== ENDING 1 (and a bit): THE NORTH OF THE NORTH =====")
    print("========================================================")

    if ending2 == False:
      endCounter = endCounter + 1
      ending2 = True

    

  def eastChamber2():
    
    global player1Health
    global player2Health
    global enemyStats
    global player1Min
    global player1Max
    global player2Min
    global player2Max
    global player1Weapon
    global player2Weapon
    global player1Heal
    global player2Heal
    global keyItem
  
    print("\n Walking through the door, you enter a room filled with mirrors. There is a piles of boxes sat in the far left corner, and in the far right an ominious book beckons you closer...")
    print("You can either check the boxes and books for supplies, touch the strange book, or go back to where you were.")
    eastChamberRoll = random.randint(1, 10)
    if eastChamberRoll in range(1, 4 + 1):
      combatFunction(enemyStats, player1Min, player1Max, player2Min, player2Max, player1Weapon, player2Weapon)
      print("After the fight is over, you both take a while to take in your surroundings again.")
      
    roomLoop = True
    while roomLoop:
      print("\n You are in the east chamber. You can either check the boxes and books for supplies, touch the strange book, or go back to where you were.")
      print("==========================")
      print("What would you like to do?")
      eastChamberInput = input()
  
      back = ["back", "behind", "return"]
      book = ["book"]
      boxes = ["chest", "boxes", "box"]
  
      for word in eastChamberInput.split():
        if word in back:
          mainHall1()
          roomLoop = False
        elif word in book:
          dungeons2END()
          roomLoop = False
        elif word in boxes:
          looting()
          print("You check the boxes, noting a horrible smell emanating from them. Pushing a couple aside, you notice a large pile of blood and bones - it seems someone tried to hide something (or from the looks of it, someone) away from the world.")
          print("You both step back from the horrific sight, you both consider your options.")
    
  def dungeons2END():
    global ending3
    global ending4
    global endCounter
    print("You find yourself in a dank, dark dungeon cell. There is nothing here, no doors, no bars... only 4 stone walls and no escape.")
    print("You contemplate your lives, your choices... perhaps if you guys had started a plumbing company instead of fighting evil you might not have been rotting in this cell for all eternity.")
    print("It's probably best if you just give up now.")
    giveUpLoop = True
    while giveUpLoop:
      giveUpInput = input("Give up? [y/n]: ")
      if giveUpInput == "y":
        print("========================================================")
        print("============ ENDING 2: Give Up and Give In =============")
        print("========================================================")
        if ending3 == False:
          endCounter = endCounter + 1
          ending3 = True
        giveUpLoop = False
      elif giveUpInput == "n":
        print("You can't give up now... not yet. You both scratch at the bottom of the stone floor, clawing your way through, desperate to escape. You find a small pebble - perhaps this could be a good tool?")
        pebbleInput = input("Use the pebble? [y/n]: ")
        pebbleLoop = True
        while pebbleLoop:
          if pebbleInput == "y":
            deeperDungeon2END()
            pebbleLoop = False
          elif pebbleInput == "n":
            print("You decide that the pebble and thus the whole ordeal is useless. Rejecting the pebble is as if to reject life - a point of no return.")
            print("========================================================")
            print("============ ENDING 2.5: Pebble Rejection ==============")
            print("========================================================")

            if ending4 == False:
              endCounter = endCounter + 1
              ending4 = True
            pebbleInput = False
          else:
            print("Invalid input, please try again.")
        giveUpLoop = False
  
      else:
        print("Invalid Input, please try again.")
  
    
  def deeperDungeon2END():
    global ending5
    global endCounter
    print("After days... months... years - you both finally break the stony floor and into the new world below.")
    print("You hold the trusty pebble in the air as light slowly starts to fill the room, your hearts rising in elation as you are finally free to see, at last...")
    print("..... \n ..... \n ..... \n ..... \n ..... \n ..... \n")
    print("A dungeon.")
    print("Another dungeon.")
    print("Maybe it would have been better to just give up while you were ahead.")
    print("========================================================")
    print("============= ENDING 3: Escape is Futile ===============")
    print("========================================================")
    if ending5 == False:
      endCounter = endCounter + 1
      ending5 = True
    
  def mountainCrack3():
    global player1Health
    global player2Health
    global enemyStats
    global player1Min
    global player1Max
    global player2Min
    global player2Max
    global player1Weapon
    global player2Weapon
    global player1Heal
    global player2Heal
    global keyItem
  
    print("\n Entering through the crack, you arrive in a dimly lit cavern. There is large amounts of fishing equipment everywhere, including some nets that look filled to the brim with...something. to the east a shining cave of wonders seems to await. However, as you make your way over there, you notice to the south a large hole leading down to what looks like an underwater lake...")
    mountainCrackRoll = random.randint(1, 10)
    if mountainCrackRoll in range(1, 4 + 1):
      combatFunction(enemyStats, player1Min, player1Max, player2Min, player2Max, player1Weapon, player2Weapon)
      print("After the fight is over, you both take a while to take in your surroundings again.")

    roomLoop = True
    while roomLoop:
      print("\n You are in a dimly lit cavern. To the east is a glowing crystal cave, and to the south a large hole leading to an underground lake. There are also some fishing nets that look good to investigate as well.")
      print("==========================")
      print("What would you like to do?")
      mountainCrackInput = input()

      crystal = ["crystal", "cave"]
      lake = ["ocean", "lake", "underground", "hole"]
      nets = ["nets"]
    
      for word in mountainCrackInput.split():   
        if word in crystal:
          crystalCave3()
          roomLoop = False
        elif word in lake:
          fishingWorld3END()
          roomLoop = False
        elif word in nets:
          looting()
          print("The fishing nets are filled with seaweed and underwater grime and muck. A few fish sit lying at the bottom of the threaded string, cold and unmoving. The smell is just awful...")
          print("You move away from the nets and look at your surroundings.")
  def crystalCave3():
    global player1Health
    global player2Health
    global enemyStats
    global player1Min
    global player1Max
    global player2Min
    global player2Max
    global player1Weapon
    global player2Weapon
    global player1Heal
    global player2Heal
    global keyItem
  
    print("\n You both stand in the cave, thousands of crystals sparkling and mesmerizing your eyes. They seem to sing to one another, almost as though they can talk... there is a box situated in the centre of the room, and looking to the south a massive pit with a large spiral staircase seems to descend down into the darkness...")
    crystalCaveRoll = random.randint(1, 10)
    if crystalCaveRoll in range(1, 4 + 1):
      combatFunction(enemyStats, player1Min, player1Max, player2Min, player2Max, player1Weapon, player2Weapon)
      print("After the fight is over, you both take a while to take in your surroundings again.")

    roomLoop = True
    while roomLoop:
      print("\n You are in a giant crystal cave. In the centre of the room lies a strange box, and to the south a spiral staircase leads down a massive pit into some unknown place.")
      print("==========================")
      print("What would you like to do?")
      crystalCaveInput = input()

      box = ["box", "centre", "crate"]
      pit = ["staircase", "spiral", "pit", "south"]
    
      for word in crystalCaveInput.split():   
        if word in pit:
          pitOfEternity3()
          roomLoop = False 
        elif word in box:
          looting()
          print("You open the box and find a large crystal sat inside. As you both go to pick it up, the crystal begins to pulsate red, and the walls of the cave follow suit. It seems this place is more alive than it seems - best leave the thing alone.")
          print("You move carefully away from the box and look at your surroundings again.")
  def fishingWorld3END():
    global ending13
    global endCounter 
    global player1Health
    global player2Health
    global enemyStats
    global player1Min
    global player1Max
    global player2Min
    global player2Max
    global player1Weapon
    global player2Weapon
    global player1Heal
    global player2Heal
    global keyItem
    
    print("You both enter the underground lake, the waters stretching out into a dark, sheltered horizon, as you slam face first into the waters. For a while, all is calm... until suddenly, a massive, 50ft long tail emerges from the depths, and a behemoth goldfish with large, forrific teeth bears down at you.")
    print("'You f-f-fools!' the goldfish jeers at you both. 'Now YOU are the little fish - and I will have my BIG catch!'")
    print("The fish slams its tail repeatedly in the water, creating waves and storms all around you as the caverns you fell from disappear from sight under the dark clouds forming around this monstrosity. If anything is going to be the big catch, you're going to make sure its them!")
    print("It seems as though there is no other option - a fight to the death it will be. [type 'fight' to begin the boss battle.]")
    
    roomLoop = True
    while roomLoop:
      print("==========================")
      print("What would you like to do?")
      fishingWorldInput = input()
  
      fight = ["fight", "battle", "combat"]
      
      for word in fishingWorldInput.split():   
        if word in fight:
          bossFunction(player1Min, player1Max, player2Min, player2Max, player1Weapon, player2Weapon, 4)
          if player1Health <= 0 and player2Health <= 0:
            roomLoop = False
          else:
            print("The big catch has finally been caught, and with it the threat to your lives is over - now, time to figure a way out of here...")
            print("========================================================")
            print("============= ENDING 9: A FISHY SITUATION ==============")
            print("========================================================")

            if ending13 == False:
              endCounter = endCounter + 1
              ending13 = True
              
            roomLoop = False 
  def pitOfEternity3():
    global player1Health
    global player2Health
    global enemyStats
    global player1Min
    global player1Max
    global player2Min
    global player2Max
    global player1Weapon
    global player2Weapon
    global player1Heal
    global player2Heal
    global keyItem
  
    print("\n Descending down the staircase, the world becomes dimmer and dimmer until at last all you can see is the blinding darkness in front of you, as you both aimlessly wander further and further down. Finally, a firefly scatters across in front of you, revealing another hole to the south that seems to descend into some form of rainbow coloured landscape beyond.")
    pitOfEternityRoll = random.randint(1, 10)
    if pitOfEternityRoll in range(1, 4 + 1):
      combatFunction(enemyStats, player1Min, player1Max, player2Min, player2Max, player1Weapon, player2Weapon)
      print("After the fight is over, you both take a while to take in your surroundings again.")

    roomLoop = True
    while roomLoop:
      print("\n All is darkness, save for the firefly flittering around your heads, and the hole south that leads down into some rainbow coloured world below.")
      print("==========================")
      print("What would you like to do?")
      pitOfEternityInput = input()

      hole = ["rainbow", "hole", "pit", "south"]
      
    
      for word in pitOfEternityInput.split():   
        if word in hole:
          hollowEarth3END()
          roomLoop = False 
  
  def hollowEarth3END():
    global endCounter
    global ending6

    print("You fall through the hole, as the pair of you hurtle into an endless pit of colours and light. The walls of the cavern stretch out more and more, until at last all that remains is light, a hollow world moving on forever. Creatures far beyond your comprehension seem to look out at you, curious as to why such pitiful mortals have dared ventured here. Though you both are stuck in this purgatory forever, at least the sight is something to behold.")
    print("========================================================")
    print("=========== ENDING 4: WHAT EVEN IS THE WORLD? ==========")
    print("========================================================")

    if ending6 == False:
      endCounter = endCounter + 1
      ending6 = True

  def westGate4():
    global player1Health
    global player2Health
    global enemyStats
    global player1Min
    global player1Max
    global player2Min
    global player2Max
    global player1Weapon
    global player2Weapon
    global player1Heal
    global player2Heal
    global keyItem
  
    print("\n Heading west, you walk through the gates and approach the borders of the strange town beyond in the far west. As you begin to make your way over there however, you see a stone lying on an ancient pedestal to the south - it seems to want to draw you in closer for some reason...")
    westGateRoll = random.randint(1, 10)
    if westGateRoll in range(1, 4 + 1):
      combatFunction(enemyStats, player1Min, player1Max, player2Min, player2Max, player1Weapon, player2Weapon)
      print("After the fight is over, you both take a while to take in your surroundings again.")

    roomLoop = True
    while roomLoop:
      print("\n To the far west lies the strange town beyond. You can make your way over there now, or instead check out the stone sitting on the pedestal to the south.")
      print("==========================")
      print("What would you like to do?")
      westGateInput = input()

      west = ["town", "west"]
      south = ["stone","south", "pedestal"]
    
      for word in westGateInput.split():   
        if word in west:
          westTown4()
          roomLoop = False 
        elif word in south:
          abyssRealm4END()
          roomLoop = False

  def abyssRealm4END():
    global endCounter
    global ending7

    print("Touching the stone, you both see the world shake around you, as the trees begin to levitate and the stars begin to fizzle out in the night sky. The world turns to darkness, and before long you realise that you have been transported to another plane of existence - a place full of neverending hallways and corridors, wrapped in a grey mist. It's a little creepy... you should probably try and get used to it.")
    print("========================================================")
    print("========= ENDING 5: THE SHADOW REALM IS REAL! ==========")
    print("========================================================")

    if ending7 == False:
      endCounter = endCounter + 1
      ending7 = True

  def westTown4():
    global player1Health
    global player2Health
    global enemyStats
    global player1Min
    global player1Max
    global player2Min
    global player2Max
    global player1Weapon
    global player2Weapon
    global player1Heal
    global player2Heal
    global keyItem
  
    print("\n You arrive into the town square to an ominous silence - you appear to have been too late, as the townsfolk lie dead along the streets. You notice that a large trail of blood seems to be leading down into an old abandoned temple to the south - however,  before you venture there, it might be worth taking a look around. The inferno lighting up the large pile of bodies would probably hold something. ")
    westTownRoll = random.randint(1, 10)
    if westTownRoll in range(1, 4 + 1):
      combatFunction(enemyStats, player1Min, player1Max, player2Min, player2Max, player1Weapon, player2Weapon)
      print("After the fight is over, you both take a while to take in your surroundings again.")

    roomLoop = True
    while roomLoop:
      print("\n You are in the town square. To the south is a trail of blood leading to an old temple. In the square the mayor's body lies dead on the steps, and a large pile of bodies are laid out in a raging inferno.")
      print("==========================")
      print("What would you like to do?")
      westTownInput = input()

      south = ["temple", "south", "old"]
      pile = ["bodies", "pile", "burning", "corpses"]
      mayor = ["mayor"]
    
      for word in westTownInput.split():   
        if word in south:
          oldTemple4()
          roomLoop = False
        elif word in pile:
          looting()
          print("Looking through the pile of bodies, you notice that both townsfolk and ornately dress vampiric creatures lay side by side with one another in the burning flames. Were they fighting each other? Or fighting together against something else?")
          print("You both step away from the inferno and take a look at your surroundings.")
        elif word in mayor:
          looting()
          print("The mayor's dead body seemed far more exorbitantly dressed than the other corpses in the village. You notice to his right, that a large chest of jewels lay there - it looks as though the mayor had attempted to flee with his riches - but it seems money can't buy you luck.")
          print("Amongst the gold coins and jewels lies too a purple crystal bottle, with a cork slammed shut into the top - its nothing like you have ever seen before...")
          keyItem = True
          print("== You have picked up a Key Item: Waters of Life == ")
          print("You move away from the mayor and his treasures, as tempting as it is to take them, and look at your surroundings.")
          
  def oldTemple4():
    global player1Health
    global player2Health
    global enemyStats
    global player1Min
    global player1Max
    global player2Min
    global player2Max
    global player1Weapon
    global player2Weapon
    global player1Heal
    global player2Heal
    global keyItem
  
    print("\n You find yourself in the epicentre of the great stone temple. The place seems to be hundreds, if not thousands of years old - moss grows on the walls, and water gushes through broken cracks, filling up the pit of water below the walkway you stand on. In the distance, you can hear the sound of a creature - evidently the one that attacked the town from the blood stains leading towards its lair in the south. However, to the west lies a further, deeper chamber, with ominous chanting echoing throughout the ancient building - perhaps they may know something? Before you make a choice, you also notice an oddly dressed skeleton in the corner of this room. Maybe it has something useful?")
    oldTempleRoll = random.randint(1, 10)
    if oldTempleRoll in range(1, 4 + 1):
      combatFunction(enemyStats, player1Min, player1Max, player2Min, player2Max, player1Weapon, player2Weapon)
      print("After the fight is over, you both take a while to take in your surroundings again.")

    roomLoop = True
    while roomLoop:
      print("\n You are in the centre of the ancient temple. To the south lies the lair of the great goliath that destroyed the town, and to the west lies a deeper chamber in the building, with ominous chanting echoing from it. There is also a skeleton in the corner that looks like it may have something of value...")
      print("==========================")
      print("What would you like to do?")
      oldTempleInput = input()

      altar = ["west", "chant", "chanting", "chants", "ominous", "echo"]
      lord = ["south", "creature", "goliath", "lair"]
      skeleton = ["skeleton", "corner"]
    
      for word in oldTempleInput.split():   
        if word in altar:
          sacredAltar4()
          roomLoop = False 
        elif word in lord:
          lordOfStone4END()
          roomLoop = False 
        elif word in skeleton:
          looting()
          print("The skeleton is clearly hundreds of years old, though the clothing its dressed in is still largely intact. A worn leather bag wraps across its left shoulder, and a strange pointy hat sits atop the skull. The bag contains a few copper coins and some old stone etchings. It looks like this person's adventuring met a meager and grisly end...")
          print("You step back from the bones and take in your surroundings again.")
  def lordOfStone4END():
    global ending8
    global endCounter 
    global player1Health
    global player2Health
    global enemyStats
    global player1Min
    global player1Max
    global player2Min
    global player2Max
    global player1Weapon
    global player2Weapon
    global player1Heal
    global player2Heal
    global keyItem
    
    print("You both enter the lair of the great Lord of Stone, quivering at the thought of what horror this monster may take. You look as a large shadow at the end of the room rises from out the darkness, and reveals itself to be...")
    print("...A pile of rocks. Just a big pile of rocks. Guess they don't call it the Lord of Stone for nothing.")
    print("'...' It doesn't really say much, but it seems pretty adamant on two things - You both not leaving, and you both being dead. Bummer.")
    print("It seems as though there is no other option - a fight to the death it will be. [type 'fight' to begin the boss battle.]")
    
    roomLoop = True
    while roomLoop:
      print("==========================")
      print("What would you like to do?")
      lordOfStoneInput = input()
  
      fight = ["fight", "battle", "combat"]
      
      for word in lordOfStoneInput.split():   
        if word in fight:
          bossFunction(player1Min, player1Max, player2Min, player2Max, player1Weapon, player2Weapon, 2)
          if player1Health <= 0 and player2Health <= 0:
            roomLoop = False
          else:
            print("The Lord Of Stone defeated and the townspeople almost saved (if they weren't already all dead), you both stand in the old temple for a moment and wonder how much a sentient bag of rocks would be worth - maybe it would be a good idea to collect some of this stuff for later...")
            print("========================================================")
            print("============= ENDING 5.25: BREAKING BRICK ==============")
            print("========================================================")

            if ending8 == False:
              endCounter = endCounter + 1
              ending8 = True
              
            roomLoop = False 
  def sacredAltar4():
    global player1Health
    global player2Health
    global enemyStats
    global player1Min
    global player1Max
    global player2Min
    global player2Max
    global player1Weapon
    global player2Weapon
    global player1Heal
    global player2Heal
    global keyItem
    
    roomLoop = True
    while roomLoop:
      print("\n You both enter the chamber to see a group of robed people standing around a stone altar. Light shines on the slab from a crack in the temple ceiling, almost inviting you over. The group stops chanting and turn to look at you, with one individual in particular walking over to greet you.")
      print("'Welcome, heroes! You are here at a most opportune moment. We require a sacrifice to the gods in order to appease them, and in return they shall rid this world of evil forever! It would seem that with brave souls such as yours, you both would make far more than suitable candidates for the role. Would you help us, and become true champions?'")
      print("You both stand there and contemplate the choice. On the one hand, if these people are telling the truth then sacrificing yourselves would truly be the greatest heroic act of all - on the other hand, there is always the narrow exit out of the chamber to the north for a quick getaway...")
      print("==========================")
      print("What would you like to do?")
      sacredAltarInput = input()

      sacrifice = ["sacrifice", "altar", "accept"]
      escape = ["escape", "north", "leave", "exit", "getaway"]
      
    
      for word in sacredAltarInput.split():   
        if word in sacrifice:
          sacrifice4END()
          roomLoop = False 
        elif word in escape:
          endlessDunes4()
          roomLoop = False 
        
  def sacrifice4END():
    global endCounter
    global ending9

    print("You both decide to lay down upon the altar and accept your fates. Besides, there are worse ways to go out... at least you'll die knowing you did something good for the world... or maybe they'll just eat you afterwards. It's a 50/50 chance either way.")
    print("========================================================")
    print("=========== ENDING 5.5: FOR THE GREATER GOOD ===========")
    print("========================================================")

    if ending9 == False:
      endCounter = endCounter + 1
      ending9 = True
  def endlessDunes4():
    global player1Health
    global player2Health
    global enemyStats
    global player1Min
    global player1Max
    global player2Min
    global player2Max
    global player1Weapon
    global player2Weapon
    global player1Heal
    global player2Heal
    global keyItem
  
    print("\n You manage to slip through the narrow exit, barely avoiding the desperate grasps of the robed figures in the temple... but looking out into your new surroundings, you see that maybe it had been better to stay there. There is nothing but desert, moving onward forever. There is nothing to see here except a strange looking cactus, nor anywhere to go but north.")
    endlessDunesRoll = random.randint(1, 10)
    if endlessDunesRoll in range(1, 4 + 1):
      combatFunction(enemyStats, player1Min, player1Max, player2Min, player2Max, player1Weapon, player2Weapon)
      print("After the fight is over, you both take a while to take in your surroundings again.")

    roomLoop = True
    while roomLoop:
      print("\n You are in an endless desert, with nothing but a strange cactus to look at and only north to head towards")
      print("==========================")
      print("What would you like to do?")
      endlessDunesInput = input()

      north = ["north", "forward", "ahead"]
      cactus = ["cactus", "strange"]
    
      for word in endlessDunesInput.split():   
        if word in north:
          procedural4END()
          roomLoop = False 
        elif word in cactus:
          print("It's a strange looking cactus.")
          
  def procedural4END():
    global endCounter
    global ending10

    print("You both wander the desert for all eternity. The dunes and the sand seem to stretch forever, and you both could have sworn that you have walked past that strange looking cactus about 10 times by now... If you both didn't know any better, you would have sworn that the desert was just being procedurally generated, like some sort of video game - not that you two in this medieval fantasy world know what video games are of course... right?")
    print("========================================================")
    print("=========== ENDING 6: IS THIS THE REAL LIFE? ===========")
    print("========================================================")

    if ending10 == False:
      endCounter = endCounter + 1
      ending10 = True
  def westShack5():
    global player1Health
    global player2Health
    global enemyStats
    global player1Min
    global player1Max
    global player2Min
    global player2Max
    global player1Weapon
    global player2Weapon
    global player1Heal
    global player2Heal
    global keyItem
  
    print("\n You enter the shack. Inside lies another door on the west facing wall. It looks a bit odd, and some sand seems to be blowing into the shack from under the door itself... But before you go off exploring, you both stand in the shack and realise - is this all worth it? Do we really want to go around, adventuring and risking our lives? It starts to make you both a bit upset. It's as if, all you want to do, is sit down and fall into despair...")
    westShackRoll = random.randint(1, 10)
    if westShackRoll in range(1, 4 + 1):
      combatFunction(enemyStats, player1Min, player1Max, player2Min, player2Max, player1Weapon, player2Weapon)
      print("After the fight is over, you both take a while to take in your surroundings again.")

    roomLoop = True
    while roomLoop:
      print("\n You are in the shack. To the west lies a strange door, but before walking through you both decide to have an existential crisis and contemplate sitting on the floor and crying for a bit instead - maybe you'll feel a bit better...")
      print("==========================")
      print("What would you like to do?")
      westShackInput = input()

      door = ["door", "open", "forward", "west"]
      despair = ["cry", "despair", "weep", "crying"]
    
      for word in westShackInput.split():   
        if word in door:
          shackField5()
          roomLoop = False
        elif word in despair:
          despairShack5END()
          roomLoop = False
  
  
  def despairShack5END():
    global endCounter
    global ending11

    print("You both kneel to the floor and begin to weep. You realise that you never really wanted to be heroes or adventurers at all - maybe working in a furniture shop would be much better? At least the only wounds you might get there are some splinters from time to time. Time for you both to head on home to get some good rest and a nice meal...")
    print("========================================================")
    print("====== ENDING 7: IT CAN ONLY GET BETTER FROM HERE ======")
    print("========================================================")

    if ending11 == False:
      endCounter = endCounter + 1
      ending11 = True
    
  def shackField5():
    global player1Health
    global player2Health
    global enemyStats
    global player1Min
    global player1Max
    global player2Min
    global player2Max
    global player1Weapon
    global player2Weapon
    global player1Heal
    global player2Heal
    global keyItem
  
    print("\n You open the door and both fall into a great desert - it seems that there was more to this shack than meets the eye. You both look up as the door closes itself about 20ft above you, suspended in the air, before it disappears in an instant, never to be seen again. Looking around, hundreds if not thousands of shacks lie across a great, open expanse of flat nothingness. The only things other than the shacks near you is a toolbox and a sign that says: 'WAY TO THE WEST: SPLINTER PLAINS'.")
    shackFieldRoll = random.randint(1, 10)
    if shackFieldRoll in range(1, 4 + 1):
      combatFunction(enemyStats, player1Min, player1Max, player2Min, player2Max, player1Weapon, player2Weapon)
      print("After the fight is over, you both take a while to take in your surroundings again.")

    roomLoop = True
    while roomLoop:
      print("\n You are in some sort of shack dimension. There is only the desert and the shacks. However, there are two things of note: A sign saying: 'WAY TO THE WEST: SPLINTER PLAINS' and a toolbox.")
      print("==========================")
      print("What would you like to do?")
      shackFieldInput = input()

      splinter = ["west", "plains", "expanse", "splinter"]
      toolbox = ["toolbox", "box"]
      
    
      for word in shackFieldInput.split():   
        if word in splinter:
          splinterPlains5()
          roomLoop = False
        elif word in toolbox:
          looting()
          print("The toolbox is rusted, the hinges on the top lid shattered to pieces presumably many years ago. While there is nothing of great note, you do take time to admire the neatness of whoever once owned this box - not a tool was out of place, nor missing in the slightest... very good job indeed.")
          print("You step away from the toolbox and think about what to do next.")
        
  def splinterPlains5():
    global player1Health
    global player2Health
    global enemyStats
    global player1Min
    global player1Max
    global player2Min
    global player2Max
    global player1Weapon
    global player2Weapon
    global player1Heal
    global player2Heal
    global keyItem
  
    print("\n As you continue west, the shacks begin to look more battered and dishevelled, until you at last arrive in a vast expanse of land, filled with nothing but an old, wise looking shack, an array of wooden spikes and sharp bits, and the entrance to a combat arena of sorts to the west. At the entrance, an armoured warrior sits dead, a large splinter stabbed straight through his left leg.")
    splinterPlainsRoll = random.randint(1, 10)
    if splinterPlainsRoll in range(1, 4 + 1):
      combatFunction(enemyStats, player1Min, player1Max, player2Min, player2Max, player1Weapon, player2Weapon)
      print("After the fight is over, you both take a while to take in your surroundings again.")

    roomLoop = True
    while roomLoop:
      print("\n You are in a vast expanse of land. There is an old, wise looking shack near you, as well as a dead armored warrior sat near the entrance of a large combat arena.")
      print("==========================")
      print("What would you like to do?")
      splinterPlainsInput = input()

      west = ["west", "arena", "fighting", "combat", "fight"]
      old = ["old", "shack", "wise"]
      warrior = ["warrior", "armor", "armored", "armour", "armoured"]
    
      for word in splinterPlainsInput.split():   
        if word in west:
          shacktronic5END()
          roomLoop = False
        elif word in old:
          looting()
          print("The old wise shack doesn't seem to be inhabited any longer - its insides have long rotted away, and the back wall has a large, cannon-sized hole in the middle. Poor shack... may it rest easy.")
          print("You move away from the tear-jerking scene and take a look again at your surroundings.")
        elif word in warrior:
          looting()
          print("You search the armoured warrior and find nothing of great interest... except! A strange book has been tucked away under the dead man's chestplate... It seems to be a... manual of some kind? Could be useful...")
          keyItem = True
          print("== You have picked up a Key Item: Shack O'tronic Assembly Manual == ")
          print("You step away from the warrior, paying your respects as you do, and then take a look again at your surroundings.")
  def shacktronic5END():
    global ending12
    global endCounter 
    global player1Health
    global player2Health
    global enemyStats
    global player1Min
    global player1Max
    global player2Min
    global player2Max
    global player1Weapon
    global player2Weapon
    global player1Heal
    global player2Heal
    global keyItem
    
    print("You enter the combat arena, a crowd cheering you on as an announcer speaks. 'O-Hoh, what's this? New challengers appear! Can they defeat the infernal Shack O'Tronic and become our new champions? Or will the mighty machine be victorious once more?'")
    print("A gigantic, shack-shaped robot charges out at you both, saw blades on both metal arms and wooden beams that extend outwards to reveal sharp pikes, ready for frivolous stabbing.")
    print("It seems as though there is no other option - a fight to the death it will be. [type 'fight' to begin the boss battle.]")
    
    roomLoop = True
    while roomLoop:
      print("==========================")
      print("What would you like to do?")
      shacktronicInput = input()
  
      fight = ["fight", "battle", "combat"]
      
      for word in shacktronicInput.split():   
        if word in fight:
          bossFunction(player1Min, player1Max, player2Min, player2Max, player1Weapon, player2Weapon, 3)
          if player1Health <= 0 and player2Health <= 0:
            roomLoop = False
          else:
            print("The Shack O'Tronic defeated, the crowd cheers on as you both are raised into the air, being crowned as the new champions of ShackLand - maybe this trip wasn't so bad after all...")
            print("========================================================")
            print("============= ENDING 8: BEAT THE MACHINE ===============")
            print("========================================================")

            if ending12 == False:
              endCounter = endCounter + 1
              ending12 = True
              
            roomLoop = False 

    
  courtyardStart0()
  
  print("Would you like to play again? [y/n]")
  playAgainInput = input()
  
  if playAgainInput == "y":
    wholeGameLoop = True
  
  else:
    print("Are you sure you want to quit? (Any Achievement progress will be gone forever!)")
    playWarning = input("[y/n]: ")
    if playWarning == "y":   
      print("Thank you for playing!")
      wholeGameLoop = False

    else:
      wholeGameLoop = True
  