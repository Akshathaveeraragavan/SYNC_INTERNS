#This is a chatbot program
#list for jokes
import random
jokes=['My wife said she wants more space. So , I said "No problem" and locked her outside my house' ,
       'A man tells his doctor,"Doc,help me.Im addicted to twitter".The doc replied,"Sorry,I dont follow you".'
       'What do you call a train carrying Bubblegum? \n "A chew-chew train"',
       'What did the air conditioner say when it met a celebrity?\n "Im your big fan!!!"',
       'Why did the farmer win an award? \n "Because, he was standing out in the field"',
       'What kind of tea is hard to swallow? \n "REALITY!"',
       'Why did the cracker went to the doctor? \n "It felt crummy!"']
#list for quotes
quotes=['Be there for others,but never yourself behind' , 'Life is hard but not impossibele' , 'All is well that ends well' ,'Silent tears holds the loudest pain' ,
        'Good things takes time ' , 'Every day may not be good , but there is something good in every day ' ]
#list for stories
stories=['TITLE: The Lion and The Mouse \n A lion was once sleeping in the jungle when a mouse started running up and down his body just for fun.\n This disturbed the lion’s sleep, and he woke up quite angry.\n He wasabout to eat the mouse when the mouse desperately requested the lion to set him free.\n “I promise you, I will be of great help to you someday if you save me.”\n The lion laughed at the mouse’s confidence and let him go.\n One day, a few hunters came into the forest and took the lion with them.\n They tied him up against a tree.\n The lion was struggling to get out and started to whimper.\n Soon, the mouse walked past and noticed the lion in trouble.\n Quickly, he ran and gnawed on the ropes to set the lion free.\n Both of them sped off into the jungle. \n MORAL OF THE STORY : A small act of kindness can go a long way!', 'TITLE: The Fox and The Stork \n One day, a selfish fox invited a stork for dinner.\n Stork was very happy with the invitation – she reached the fox’s home on time and knocked at the door with her long beak. \n The fox took her to the dinner table and served some soup in shallow bowls for both of them.\n As the bowl was too shallow for the stork, she couldn’t have soup at all.\n But, the fox licked up his soup quickly.\n The stork was angry and upset, but she didn’t show her anger and behaved politely.\n To teach a lesson to the fox, she then invited him for dinner the next day.\n She too served soup, but this time the soup was served in two tall narrow vases.\n The stork devoured the soup from her vase, but the fox couldn’t drink any of it because of his narrow neck.\n The fox realised his mistake and went home famished.\n Moral of the Story: A selfish act backfires sonner or later!.'
         'TITLE: The Proud Rose \n Once upon a time, there was a beautiful rose plant in a garden.\n One rose flower on the plant was proud of its beauty.\n However, it was disappointed that it was growing next to an ugly cactus.\n Every day, the rose would insult the cactus about its looks, but the cactus stayed quiet.\n All the other plants in the garden tried to stop the rose from bullying the cactus, but the rose was too swayed by its own beauty to listen to anyone.\n One summer, a well in the garden dried up and there was no water for the plants.\n The rose slowly began to wilt.\n The rose saw a sparrow dip its beak into the cactus for some water.\n The rose then felt ashamed for having made fun of the cactus all this time.\n But because it was in need of water, it went to ask the cactus if it could have some water.\n The kind cactus agreed, and they both got through summer as friends.\n MORAL OF THE STORY: Never judge someone by the way they look!'
         'TITLE: The Golden Touch of Midas \n Once upon a time, there was a Greek King, Midas.\n He was very rich and had lots of Gold.\n He had a daughter, who he loved a lot.\n One day, Midas found an angel in need of help.\n He helped her and in return she agreed to grant a wish.\nMidas wished that everything he touched would turn into gold.\n His wish was granted.\nOn his way home, he touched rocks and plants and they turned into gold.\nAs he reached home, in excitement he hugged his daughter, who turned into gold.\nMidas was devastated and he had learnt his lesson.\n Upon learning his lesson, Midas asked the angel to take his wish away.\nMORAL OF THE STORY: Greed is not good for you. Be content and satisfied to lead a happy and fulfilling life!'
         'TITLE: The Ant and The Grassphopper \n The ant and the grasshopper were best friends with very different personalities.\n The grasshopper would spend his days sleeping or playing his guitar while the ant would collect food and build his ant hill. \n Every now and then, the grasshopper would tell the ant to take a break.\n However, the ant would refuse and continue to complete his work.\n Soon winter came making the days and nights cold.\n One day the colony of ants were busy trying to dry some grains of corn.\n The grasshopper who was extremely weak and hungry came up to the ants and asked "Can you please give me a piece of corn?".\n The ant replied "We worked hard for this corn all summer while you relaxed, why should we give it to you?"\n The grasshopper was so busy singing and sleeping  that he didnt have enough food to last winter.\n The grasshopper realized his mistake.\n MORAL OF THE STORY: Make use of oppurtunity when you have it!'
         'TITLE: Be wise while counting \n One day in Akbar’s court someone asked the question, "How many crows are there in the city?".\n No one had the answer.\n Birbal quickly replied "Four thousand three hundred and twelve".\n He was asked how did he know this?\n Birbal send " Send your man out to count the crows.\n If it is lesser than this number then some crows are visiting their families elsewhere and if it is more than this number, then some crows from outside are visiting their families here.\n Akbar was very happy with the answer and showered Birbal with gifts for his wit.\n MORAL OF THE STORY: Sometimes, you should think out of the box!'] 
a='Chatbot'
b='User'
print(a,':Hi')
user=input('User:')
if user=='Hi' or user=='HI' or user=='hi' :
    print('Chatbot:How may I help you? \n JOKE/QUOTE/STORY/INFORMATION ON PROGRAMMING')
else:
    pass
user=input('User:')
if user=='JOKE' or user=="Joke" or user=='joke' :
    print("Chatbot: Sure, here is a joke to cheer you up!")
    print(random.choice(jokes))
    user=input('Chatbot: Do you want to hear another one? Y/N')
    while user=='Y' or user=="y":
        print("Chatbot: Sure, here is a joke to cheer you up!")
        print(random.choice(jokes))
        user=input('Chatbot: Do you want to hear another one? Y/N')
        if user=='Y' or user=="y":
            print(random.choice(jokes))
    else:
        print("Chatbot: OK,hope you enjoyed the joke")
        print('Chatbot:BYE')
        user=input('User:')
        if user=="Bye" or user=='BYE' or user=='bye':
            pass;
       #else:
            #print('Chatbot: Oops! Restart  me again to view more \n IM SORRY')
elif user=='QUOTE' or user=="quote" or user=="Quote" :
    print("Chatbot: Sure, here is a quote for you!")
    print(random.choice(quotes))
    user=input('Chatbot: Do you want to hear another one? Y/N')
    while user=='Y' or user=='y':
        print("Chatbot: Sure, here is a quote for you!")
        print(random.choice(quotes))
        user=input('Chatbot: Do you want to hear another one? Y/N')
        if user=='Y' or user=="y":
            print(random.choice(quotes))
    else:
        print("Chatbot: OK,hope you enjoyed the quote")
        print('Chatbot:BYE')
        user=input('User:')
        if user=="Bye" or user=='BYE' or user=='bye':
            pass;
        else:
            print('Chatbot: Oops! Restart  me again to view more \n IM SORRY')
elif user=="STORY" or user=="story" or user=="Story" :
    print("Chatbot: Sure, here is a story for you!")
    print(random.choice(stories))
    user=input('Chatbot: Do you want to hear another one? Y/N')
    while user=='Y' or user=="y":
        print("Chatbot: Sure, here is a story for you!")
        print(random.choice(jokes))
        user=input('Chatbot: Do you want to hear another one? Y/N')
        if user=='Y' or user=="y":
            print(random.choice(jokes))
    else:
        print("Chatbot: OK,hope you enjoyed the story")
        print('Chatbot:BYE')
        user=input('User:')
        if user=="Bye" or user=='BYE' or user=='bye':
            pass;
elif user=="INFORMATION ON PROGRAMMING" or user=="Information on programming" or user=="information on programming" :
    print("Chatbot: Sure , On what language would you like to read? \n C/C++/JAVA/JS/PYTHON/R/GO/RUBY/HTML/CSS/SQL")
    ch=input('User:')
    if ch=='C' or ch=='c':
        print('Chatbot: Sure , here you can read about C :https://www.geeksforgeeks.org/c-language-introduction/ \n Hope you found it useful')
    elif ch=='C++' or ch=='c++':
        print('Chatbot: Sure , here you can read about C++:https://www.programiz.com/cpp-programming \n Hope you found it useful')
    elif ch=='JAVA' or ch=='java' or ch=="Java":
        print('Chatbot: Sure , here you can read about JAVA :https://www.w3schools.com/java/java_intro.asp \n Hope you found it useful')
    elif ch=='JS' or ch=='js':
        print('Chatbot: Sure , here you can read about JS :https://www.w3schools.com/js/ \n Hope you found it useful')
    elif ch=='PYTHON' or ch=='python' or ch=='Python' :
        print('Chatbot: Sure , here you can read about PYTHON :https://www.python.org/\n Hope you found it useful ')
    elif ch=='R' or ch=='r':
        print('Chatbot: Sure , here you can read about R :https://www.r-project.org/about.html \n Hope you found it useful')
    elif ch=='GO' or ch=='go':
        print('Chatbot: Sure , here you can read about GO :https://go.dev/ \n Hope you found it useful')
    elif ch=='RUBY' or ch=='ruby' or ch=='Ruby':
        print('Chatbot: Sure , here you can read about RUBY :https://www.ruby-lang.org/en/ \n Hope you found it useful')
    elif ch=='HTML' or 'Html' or ch=='html':
        print('Chatbot: Sure , here you can read about HTML https://www.w3schools.com/html/html_intro.asp#:~:text=HTML%20stands%20for%20Hyper%20Text,how%20to%20display%20the%20content: \n Hope you found it useful')
    elif ch=='CSS' or ch=='css' or ch=='Css' :
        print('Chatbot: Sure , here you can read about CSS :https://www.w3schools.com/css/css_intro.asp \n Hope you found it useful')
    elif ch=='SQL' or ch=='sql' or ch=='Sql':
        print('Chatbot: Sure , here you can read about SQL :https://www.geeksforgeeks.org/structured-query-language/ \n Hope you found it useful')
else:
    user=input(('Chatbot:EXIT?'))
    if user=='EXIT' or user=='exit' or user=="Exit" :
        print('Chatbot: Bye!')

    
        
        
        
        

    
    
    
    
