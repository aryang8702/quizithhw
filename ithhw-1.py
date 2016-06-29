print('\t\t\tWelcome to the Ultimate Computer Quiz')
input('This quiz takes you through 30 questions and tells you your level in IT. Press enter to take the quiz.')
print('''\nGeneral Instructions:
1) This quiz contains 30 questions.
2) Section-A contains 10 Multiple choice questions.
3) Section-B contains 10 Give one word questions.
4) Section-C contains 10 Fill in the blanks.
5) Each question of Section-A carries 1 mark each.
6) Each question of Section-B and Section-C carries 2 marks.
7) Wrong answer in Section-c carries (-1) marks.
8) For Secttion-A, option number is to be avoided and only the answer is to be written.
9) For Section-B and Section-C, only the answer must be given. Dont copy the question.
10) You can leave a question by pressing the Enter key.
11) All answers are to be given in lowercase.
12) You will be told your marks at the end of the quiz.''')
input('Press enter to start with the questions.')
points = 0
print('\n\t\t\t Section-A')
print('Q1) Which one of the given is a google product using which you can convert your tv into a smart tv?')
print('''1) Chromebook
2) ChromeOS
3) Chromecast
4) Chrometv''')
answera1 = input()
if answera1 == 'chromecast':
    points += 1
print('Q2) Which of the following is the smallest type of computer?')
print('''1) Desktop
2) Laptop
3) Bootable pendrives
4) Stick PC''')
answera2 = input()
if answera2 == 'stick pc':
    points += 1
print('Q3) Which one of the following is not an essential part for a gaming pc?')
print('''1) Gaming mouse
2) More than 4 GB of RAM
3) Large screen
4) Good graphics processor''')
answera3 = input()
if answera3 == 'large screen':
    points += 1
print('Q4) What is the latest operating system released by microsoft?')
print('''1) Windows 8.1
2) Windows 8.2
3) Windows 9
4) Windows 10''')
answera4 = input()
if answera4 == 'windows 10':
    points += 1
print('Q5) Which one of them is not related to Android\'s latest os project?')
print('''1) Android N
2) Android 7.0
3) Android New
4) Both 1 and 2''')
answera5 = input()
if answera5 == 'android new':
    points += 1
print('Q6) What speed does the new USB 3.1 Type C support?')
print('''1) 512 mbps
2) 5 gbps
3) 2 gbps
4) 10 gbps''')
answera6 = input()
if answera6 == '10 gbps':
    points += 1
print('Q7) Can laptops be wirelessly charged?')
print('''1) Yes
2) No
3) Not right now as it is being developed
4) Cant say''')
answera7 = input()
if answera7 == 'yes':
    points += 1
print('Q8) What technology helps us to run multiple operating systems inside a single os?')
print('''1) os technology
2) multiwindow technology
3) computerization
4) virtualization''')
answera8 = input()
if answera8 == 'virtualization':
    points += 1
print('Q9) What is the maximum number of antennas in a router?')
print('''1) 4
2) 8
3) 6
4) 2''')
answera9 = input()
if answera9 == '6':
    points += 1
print('Q10) Name the fastest consumer processor ever made.')
print('''1) Core i7+
2) Cherry Trail
3) Core i7
4) Core i7 extreme''')
answera10 = input()
if answera10 == 'core i7 extreme':
    points += 1
print('\n\t\t\t Section-B')
print('Q1) Which chip is used in Intel Compute Stick?(Mention only the type, eg: xeon etc.)')
answerb1 = input()
if answerb1 == 'atom':
    points += 2
print('Q2) Name the most famous android emulators.')
answerb2 = input()
if answerb2 == 'bluestacks':
    points += 2
elif answerb2 == 'andy':
    points += 2
elif answerb2 == 'andyroid':
    points += 2
elif answerb2 == 'bluestacks emulator':
    points += 2
elif answerb2 == 'andy emulator':
    points += 2
print('Q3) Name the first VR Headset to be developed.')
answerb3 = input()
if answerb3 == 'oculus rift':
    points += 2
print('Q4) Developed in 2014, by hendo, this thing makes it\'s appearance in Back to the future series.')
answerb4 = input()
if answerb4 == 'hoverboard':
    points += 2
print('Q5) What type of glasses were devloped by google?')
answerb5 = input()
if answerb5 == 'google glass':
    points += 2
print('Q6) Which software is installed in google\'s driverless cars?')
answerb6 = input()
if answerb6 == 'google chauffeur':
    points += 2
elif answerb6 == 'chauffeur':
    points += 2
print('Q7) Apple:Siri::Microsoft:?. Whats \'?\'')
answerb7 = input()
if answerb7 == 'cortana':
    points += 2
print('Q8) which type of trains use powerful electromagnets?')
answerb8 = input()
if answerb8 == 'maglev':
    points += 2
elif answerb8 == 'maglev train':
    points += 2
elif answerb8 == 'maglev trains':
    points += 2
print('Q9) E-book readers use which kind of display?')
answerb9 = input()
if answerb9 == 'e ink display':
    points += 2
elif answerb9 == 'e-ink display':
    points += 2
elif answerb9 == 'e ink':
    points += 2
elif answerb9 == 'e-ink':
    points += 2
print('Q10) What\'s the colour of usb 3.1?')
answerb10 = input()
if answerb10 == 'blue':
    points += 2
elif answerb10 == 'teal':
    points += 2
print('\n\t\t\t Section-C')
print('Q1) ________ is a native hypervisor which can create virtual machines on x86-64 systems running Windows.')
answerc1 = input()
if answerc1 == 'hyper v':
    points += 2
elif answerc1 == 'hyper-v':
    points += 2
elif answerc1 == 'microsoft hyper v':
    points += 2
elif answerc1 == 'microsoft hyper-v':
    points += 2
elif answerc1 == '':
    points += 0
elif answerc1 == ' ':
    points += 0
else:
    points -= 1
print('Q2) Laptops with Intel’s RealSense 3D camera will be able to use ________ and use that capability to log users in to Windows.')
answerc2 = input()
if answerc2 == 'face recognization':
    points += 2
elif answerc2 == '':
    points += 0
elif answerc2 == ' ':
    point += 0
else:
    points -= 1
print('Q3) ________ is the latest and the fastest type of RAM.')
answerc3 = input()
if answerc3 == 'ddr4':
    points += 2
elif answerc3 == 'ddr4 sdram':
    points += 2
elif answerc3 == 'ddr4 ram':
    points += 2
elif answerc3 == '':
    points += 0
elif answerc3 == ' ':
    points += 0
else:
    points -= 1
print('Q4) ________ then relay information to a small device worn by the patient; the device wirelessly transmits it to a computer.')
answerc4 = input()
if answerc4 == 'smart contact lenses':
    points += 2
elif answerc4 == 'smart lenses':
    points += 2
elif answerc4 == '':
    points += 0
elif answerc4 == ' ':
    points += 0
else:
    points -= 1
print('Q5) ________ from Illinois-based Ambient Corporation provides an audible voice for those who have lost the ability to talk.')
answerc5 = input()
if answerc5 == 'speech restorer':
    points += 2
elif answerc5 == 'phonetic speech engine':
    points += 2
elif answerc5 == '':
    points += 0
elif answerc5 == ' ':
    points += 0
else:
    points -= 1
print('Q6) ________ uses electrical stimulators to exercise muscles and keep them strong during recovery from fractures.')
answerc6 = input()
if answerc6 == 'muscle stimulator':
    points += 2
elif answerc6 == 'myospare':
    points += 2
elif answerc6 == '':
    points += 0
elif answerc6 ==  ' ':
    points += 0
else:
    points -= 1
print('Q7) ________ is a device that stretches an amputee\'s skin near the prosthesis in ways that provide feedback about the limb\'s position and movement.')
answerc7 = input()
if answerc7 == 'prosthetic feedback':
    points += 2
elif answerc7 == '':
    points += 0
elif answerc7 == ' ':
    points += 0
else:
    points -= 1
print('Q8) As stroke patients walk on a treadmill, they see moving images that fool their brains into thinking they are walking slower than they are. This is a ________')
answerc8 = input()
if answerc8 == 'walking simulator':
    points += 2
elif answerc8 == '':
    points += 0
elif answerc8 == ' ':
    points += 0
else:
    points -= 1
print('Q9) A/An ________ is performed by casting an unperceived beam of low-energy infrared light into a person’s eye as they look through the scanner\'s eyepiece.')
answerc9 = input()
if answerc9 == 'retinal scan':
    points += 2
elif answerc9 == 'eye scan':
    points += 2
elif answerc9 == '':
    points += 0
elif answerc9 == ' ':
    points += 0
else:
    points -= 1
print('Q10) ________ is another name for 3D printing.')
answerc10 = input()
if answerc10 == 'additive manufacturing':
    points += 2
elif answerc10 == 'am':
    points += 2
elif answerc10 == '':
    points += 0
elif answerc10 == ' ':
    points += 0
else:
    points -= 1
print('You have completed the quiz. I hope you enjoyed it!')
percent = 2 * points
if points == 50:
    print('Perfect! You really are an IT Wizard! You scored 50 points out of 50. Know your percentage? It\'s 100%!')
elif points >= 45 and points < 50:
    print('Congratulations! You pass this test with a distinction. You scored ' + str(points) + ' points out of 50. Your percentage is ' + str(percent) + '.')
elif points >= 35 and points < 45:
    print('Great! You pass this test with a merit. You scored ' + str(points) + ' points out of 50. Your percentage is ' + str(percent) + '.')
elif points >= 25 and points < 35:
    print('Well done! You have passed this test. You scored ' + str(points) + ' points out of 50. Your percentage is ' + str(percent) + '.')
else:
    print('You need more practice! You have failed this test. You scored ' + str(points) + ' points out of 50. Your percentage is ' + str(percent) + '.')
input('Press enter to exit.')
