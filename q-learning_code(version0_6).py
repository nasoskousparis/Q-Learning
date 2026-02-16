import random
import numpy as np
import matplotlib.pyplot as plt

#Δημιουργούμε μια κλάση για αντικείμενα τύπου grid που θα φτιάχνουν, γεμίζουν και μεταβάλλουν το gridworld
class grid():
    def __init__(self, xlim, ylim): #Αρχικοποιούμε το αντικείμενο με τις διαστάσεις του. Κάθε μεταβλητή με self μπροστά από αυτήν είναι attribute του αντικειμένου
        self.xlim=xlim
        self.ylim=ylim
        self.re=10 #Δηλώνουμε την τιμή της αμοιβής του στόχου 
        self.pu=-10 #Δηλώνουμε την τιμή της τιμωρίας των εμποδίων
        self.neu=-1 #Δηλώνουμε την τιμή των ουδέτερων στοιχείων
        gridworld = np.zeros((xlim, ylim)) #Αρχικοποίηση του πίνακα gridworld που θα δεχτεί της τιμές
        self.gridworld=gridworld
        gridworld += self.neu
        self.reward_state=0 #Αρχικοποίηση του στόχου
        while(True):        #Ορίζει ο χρήστης τον αριθμό των εμποδίων
            num_pu = int(input("How many obstacles: "))
            if(num_pu>1 and num_pu<ylim): 
                break
            else:
                print("Number must be between 2 and ",ylim-1, "\n")
        for a in range(num_pu):
            while(True):    #Δημιουργεί όσο εμπόδια έχει ορίσει ο χρήστης σε τυχαίες θέσεις
                cord_x = random.randint(0,xlim-1)
                cord_y = random.randint(0,ylim-1)
                if gridworld[cord_y, cord_x] != self.pu:
                    gridworld[cord_y, cord_x] = self.pu
                    break
        while(True):       #Δημιουργεί τον στόχο σε τυχαία θέση που δεν είναι εμπόδιο 
                cord_x = random.randint(0,xlim-1)
                cord_y = random.randint(0,ylim-1)
                if gridworld[cord_y, cord_x] != self.pu:
                    gridworld[cord_y, cord_x] = self.re
                    self.reward_state = self.ylim*cord_y + cord_x
                    break
        location = [0, 0]
        visualization(gridworld, location, self.re, self.pu,xlim,ylim) #μας δείχνει τον κόσμο σε αρχική κατάσταση 
        
    #Επιστρέφει τον agent στην αρχική του θέση (0,0)
    def reset(self):
        self.location = [0, 0]
        return 0
    
    #Εκτυπώνει το gridworld στο terminal και την τρέχουσα θέση του agent (χρησιμοποιήθηκε πριν την οπτικοποίηση)
    def print_gridworld(self):
        for a in self.gridworld:
            print(a)
        print(f"bot at {self.location[0]} {self.location[1]}")

    #Κάνει μια τυχαία κίνηση μέσα στα όρια του Gridworld (ώστε να μην βγαίνει εκτός του Gridworld)
    def random_move(self):
        while True:
            f = random.randint(0, 3)
            if f == 0 and self.location[0] > 0:
                self.location[0] -= 1
                return f
            elif f == 1 and self.location[0] < self.xlim-1:
                self.location[0] += 1
                return f
            elif f == 2 and self.location[1] > 0:
                self.location[1] -= 1
                return f
            elif f == 3 and self.location[1] < self.ylim-1:
                self.location[1] += 1
                return f
              
    #Κάνει μια κίνηση που ορίζουμε εμείς (αν η κίνηση που πάει να γίνει δεν είναι επιτρεπτή δεν πραγματοποιείται)
    def perform_move(self, f):
        if f == 0 and self.location[0] > 0:
            self.location[0] -= 1
        elif f == 1 and self.location[0] < self.xlim-1:
            self.location[0] += 1
        elif f == 2 and self.location[1] > 0:
            self.location[1] -= 1
        elif f == 3 and self.location[1] < self.ylim-1:
            self.location[1] += 1

    #Χρησιμοποιείται για να μας δείξει σε ποιο state βρίσκεται ο agent
    def find_state(self):
        return self.location[0]*self.xlim + self.location[1]
    

#Function το οποίο παίρνει τα στοιχεία απο το αντικείμενο κλάσης grid και τα εμφανίζει 
def visualization(gridworld, location, re, pu, xlim,ylim,reward=0):
    plt.xlim(0, xlim)
    plt.ylim(0, ylim)
    plt.gca().invert_yaxis() #Βάζεθ να ξεκινάει το Υ από την πάνω πλευρά του πίνακα, για να είναι πιο ευανάγνωστο το γράφημα 
    plt.gca().set_aspect('equal')
    plt.title(f"Total reward: {reward}")
    for i in range(len(gridworld)):
        for j in range(len(gridworld[i])):
            if gridworld[i][j] == pu:   #Αν βλέπει ότι το κουτάκι έχει την τιμή εμποδίου, το κάνει κόκκινο 
                y_square = [i, i, i+1, i+1]
                x_square = [j, j+1, j+1, j]
                plt.fill(x_square, y_square, color='red', alpha=1)
            elif gridworld[i][j] == re:  #Αντίστοιχα αν βλέπει πως είναι ο στόχος το κάνει πράσινο
                y_square = [i, i, i+1, i+1]
                x_square = [j, j+1, j+1, j]
                plt.fill(x_square, y_square, color='green', alpha=1)
            else:                        #Αλλιώς είναι λευκό
                y_square = [i, i, i+1, i+1]
                x_square = [j, j+1, j+1, j]
                plt.fill(x_square, y_square, color='white', alpha=1) 
    y_square = [location[0], location[0], location[0]+1, location[0]+1]
    x_square = [location[1], location[1]+1, location[1]+1, location[1]]
    plt.fill(x_square, y_square, color='skyblue', alpha=1) #Κάνει την τρέχουσα θέση (θέση του agent) μπλε
    plt.pause(0.1)                      #Η παύση μεταξύ των κινήσεων



#Εδώ υλοποιείται ο αλγόριθμος Q-Learning, ορίζονται οι επαναλήψεις και καλείται η οπτικοποίηση 
def Q_learning(alpha, gamma, epsilon):
    for episode in range(1000):
        state = env.reset()
        done = False
        epsilon -= 0.0004 #Σε κάθε επανάληψη είναι 0.04% πιο πιθανό ο agent να επιλέξει την βέλτιστη γνωστή κίνηση 
        total_reward = 0 #Κρατάει το αριθμητικό αποτέλεσμα των κινήσεών του agent 
        while not done:
            if episode%99==0:  #Οπτικοποιεί την πρόοδο κάθε 99 επαναλήψεις 
                visualization(env.gridworld, env.location, env.re, env.pu, env.xlim,env.ylim,total_reward)
            if np.random.uniform(0, 1) < epsilon:   #Αν ο τυχαίος αριθμός ειναι μεγαλύτερος ή ίσος του ε τότε κάνει την βέλτιστη γνωστή κίνηση
                action = env.random_move()  #Κάνει τυχαία κίνηση (exploration)
            else:
                action = np.argmax(Q[state, :])  #Κάνει δράση (exploitation) - ((το μέγιστο σημαίνει οτι παίρνει την κίνηση απο το state αυτό με το λιγοστό punishment ))
                env.perform_move(action)

            new_state = env.find_state()  #Βλέπει την καινούρια  θέση του agent
            reward = env.gridworld[env.location[0]][env.location[1]]
            total_reward += reward #Ενημερώνει το ολικό reward            
            Q[state, action] = Q[state, action] + alpha * (reward + gamma * np.max(Q[new_state, :]) - Q[state, action])  #ενημερώνει  τον πίνακα Q σύμφωνα με τον αλγόριθμο που μας έχει δωθεί 
            state = new_state #Ενημερώνει την θέση του ρομποτ 
            if state == env.reward_state: #Αν έφτασε στο στόχο, πήγαινε στην επόμενη επανάληψη
                break
        print(episode, total_reward, epsilon) 


    #Από εδώ και κάτω έχουν τελειώσει οι βασικές επαναλήψεις και τρέχουμε απλά τον agent στο Gridworld μας ανάλογα με μια καινούρια τιμή ε που δίνει ο χρήστης, ώσπου να δώσει την τιμή 0, ώστε να ακολουθήσει την βέλτιστη διαδρομή και να τερματίσει 
    state = env.reset()
    total_reward = 0
    visualization(env.gridworld, env.location, env.re, env.pu, env.xlim, env.ylim, total_reward)
    epsilon = 1
    while epsilon!=0:
        epsilon=float(input("Give an 'epsilon' (0 to show the optimal path and end): "))  #Ζήτα ε μέχρι να πάρεις 0
        while True:
            visualization(env.gridworld, env.location, env.re, env.pu, env.xlim, env.ylim, total_reward)
            #ε-greedy επιλογή δράσης
            if np.random.uniform(0, 1) < epsilon:
                    action = env.random_move()  #Τυχαία δράση (exploration)
            else:
                action = np.argmax(Q[state, :])  #Καλύτερη δράση (exploitation)
                env.perform_move(action)

            new_state = env.find_state()
            reward = env.gridworld[env.location[0]][env.location[1]]
            total_reward += reward
            state = new_state
            if state == env.reward_state:
                break  
        state = env.reset()
    print(Q)


print("Start of Q-Learning in Gridworld\n")
#Οι διαστάσεις του Gridworld μας
while True:
    try:
        xdim = int(input("Please enter a number larger than 2 for the size of the gridworld: "))
        ydim = xdim
    except ValueError:
        print("Not a valid size, please make sure it's larger than 2.")
        continue
    if xdim > 2:
        break
    print("Not a valid size, please make sure it's larger than 2 and try again.")

plt.title("Line Plot with Grid") 
plt.xlim(0, xdim) #Θέτουμε τα όρια στην οπτικοποίηση 
plt.ylim(0, ydim)
plt.gca().invert_yaxis()
plt.gca().set_aspect('equal')

states = xdim*ydim  #Ένα state για κάθε κουτάκι 
actions = 4  #Έχουμε κίνηση σε 4 κατευθύνσεις
epsilon = 0.5 #Ρυθμός επιλογής τυχαίας κίνησης
Q = np.zeros((states, actions)) #Αρχικοποίηση του πίνακα Q  
env = grid(xdim,ydim) #Δημιουργία του Gridworld 
alpha = 0.99
gamma = 0.7
Q_learning(alpha, gamma, epsilon) #Τρέξιμο του αλγορίθμου Q-learning