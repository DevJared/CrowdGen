import sqlite3 as lite, os, random as rand, numpy as np, math




from ClassOutline import User_Learning, Response_Updater
import ClassOutline as CO
class Database():
    
    
    def __init__(self):
        
        self.questions = [(1,"My name is Jern, and I'm having the worst day of my life."), (2, "I lost all my money in the stock market. I'm thinking of shooting myself."), (3, "I'm being evicted from my house. Not sure I can take it anymore"), (4, "My wife left me.")]
        self.choices = [(1,"Don't feel so down!",0.25,4,5),(2,"The world isn't fair. Get your shit together.",0.25,2,2),(3,"You'll land on your feet.",0.25,1,5), (4,"There's more than one fish in the pond.",0.25,2,4)]
        
    
        os.chdir("C:\sqlite")
 
        self.conn = lite.connect('Crowdsource_Project.db')
        self.curr = self.conn.cursor()    
  

        #self.select_Responses_to_Present(self.get_history(),self.choices)
        
    
    #weighting (user_id (pkey) INTEGER, weights REAL, choice1 INTEGER, choice2 INTEGER, choice3 INTEGER, choice4 INTEGER, choice5 INTEGER)
    
    #return weights as list of form [(weight1,),(weight2,)...]
    def get_weights(self):
        self.curr.execute('select weights from weighting')
        weights = self.curr.fetchall()
        if not weights:  
            print "No Current Users"
        else:  
            return weights
        
    def set_weights(self, id, value):
        self.curr.execute('update weighting set weights =:value where user_id =:id', {'value':value,'id':id})
        self.conn.commit()
    
    #return history as dictionary. user_id -> {weight,choice1,choice2,choice3,choice4,choice5}
    def get_history(self):
        self.curr.execute('select * from weighting')  
        hist = self.curr.fetchall()
        if not hist:
            print "No Current Users"
        else:
            history = {}
            for row in hist:
                history.update({row[0]:{'weight': row[1], 'choice1': row[2],'choice2': row[3],'choice3': row[4],'choice4': row[5]}})
            return history
        
    #prompt_questions (prompt_id (pkey), prompt_text STRING) 
    def set_questions(self, new_questions = []):
        for i in new_questions:
            self.curr.execute('select count(*)+1 from prompt_questions')
            count = self.curr.fetchone()
            self.curr.execute('insert into prompt_questions values (?,?)', (count[0],i))
            self.questions.append((count[0],i))
        self.conn.commit()
    
    def get_questions(self):   
        self.curr.execute('select prompt_text from prompt_questions')
        prompts = self.curr.fetchall()
        if not prompts:
            print "No Prompts"
        else:
            return prompts
        
    #user_end
    def get_displayed_questions(self):
        return self.questions
        
    #prompt_choices (choice_id (pkey) STRING, choice_text TEXT, choice_value REAL, number_chosen INTEGER, number_shown INTEGER)
    
    def new_choice(self, choices = []):
        for i in choices:
            self.curr.execute('select count(*) from prompt_choices')
            count = self.curr.fetchone()
            #do we want last three parameters to be 0?
            self.curr.execute('insert into prompt_choices values (?,?,0,0,0)',(count[0],i))  
            self.choices.append((count[0],i,0,0,0))          
        self.conn.commit()
    
    def default_choices(self):
        self.curr.execute('update prompt_choices set choice_value = 0, number_chosen = 0, number_shown = 0 where choice_id = 0' )        
        self.curr.execute('update prompt_choices set choice_value = 0, number_chosen = 0, number_shown = 0 where choice_id = 1' )    
        self.curr.execute('update prompt_choices set choice_value = 0, number_chosen = 0, number_shown = 0 where choice_id = 2' )    
        self.curr.execute('update prompt_choices set choice_value = 0, number_chosen = 0, number_shown = 0 where choice_id = 3' )       
        self.conn.commit()
    
    def set_choice(self, id, val):
  
        self.curr.execute('update prompt_choices set choice_value = ? where choice_id = ?', (val,id))
        self.conn.commit()
        
    def set_weights_choice1(self, id, val):
  
        self.curr.execute('update weighting set choice1 = ? where user_id = ?', (val,id))
        self.conn.commit()
    
    def set_weights_choice2(self, id, val):
  
        self.curr.execute('update weighting set choice2 = ? where user_id = ?', (val,id))
        self.conn.commit()
    
    def set_weights_choice3(self, id, val):
  
        self.curr.execute('update weighting set choice3 = ? where user_id = ?', (val,id))
        self.conn.commit()
    
    def set_weights_choice4(self, id, val):
  
        self.curr.execute('update weighting set choice4 = ? where user_id = ?', (val,id))
        self.conn.commit()
            
            
   #all choices
    def get_choices(self):
        self.curr.execute('select * from prompt_choices')
        choices = self.curr.fetchall()
        if not choices:
            print "No Choices"
        else: return choices
    
    #return as tuple (choice,)
    def get_choice(self, id = None):
        if id == None:
            return self.get_choices()
        self.curr.execute('select choice_text from prompt_choices where choice_id = (?)',(id,))
        text = self.curr.fetchone()
        if not text:
            print "No Choices"
        else: return text
                               
    def close(self):
            self.conn.close()
                         
        
if __name__ == '__main__':
    reload(CO)
    clusterComponent=User_Learning()
    startingUsers_Fake= [[1,1,1,1],[1,0,1,2],[4,0,0,0],[1,2,2,1]]
    
    clusterComponent.instantiateClusters(startingUsers_Fake)
    response=Response_Updater()

    database=Database()


    storeUsers=[]
    
    CurrentQuestionPrompt=""
    options=["",""]
    #get actual option value in database
    
    #getQuestion=getQuestion = Random()
    iteration=0
    question=database.get_questions()
    for prompt_statements in xrange(4):
        Choices=database.get_choices()
    
        userScores=None
        if iteration==0:
            for i in xrange(5):
                database.set_weights_choice1(i,0)
                database.set_weights_choice2(i,0)
                database.set_weights_choice3(i,0)
                database.set_weights_choice4(i,0)
                database.set_weights(i,0)
                database.default_choices()
            clusterComponent.updateClusters(None,startingUsers_Fake,None)
            userScores=response.calculate_All_User_Weights_Initialize(5)
            for userDict in userScores:
                database.set_weights(userDict["id"],userDict["score"])
           
            for choice_prompt_id in xrange(4):
                score=1.0/4.0
                database.set_choice(choice_prompt_id, score)
        else:
             weights = database.get_history()
             user_matrix = []
             for i in xrange(5):
                    user_matrix.append([weights[i]['choice1'],weights[i]['choice2'],weights[i]['choice3'],weights[i]['choice4']])
             clusterComponent.updateClusters(None,user_matrix,None)
             users_weightings=response.calculate_All_User_Weights(clusterComponent, user_matrix)
             
             normValue=0.0
             #First calculate sum of all the values - to renorm to 1 NON-EUCLIDEAN
             for user_weight in users_weightings: normValue+=user_weight["score"]
             normInverse=0.0
             
             #Then make it so taht closer to 1.0 is btter - SO NEW NORM RELATIVE TO 1.0
             for user_weight in users_weightings:
                 identifier=user_weight["id"]
                 score=user_weight["score"]
                 normInverse+= 1.0-(score/normValue)
                 
             #Then get each value distance from 1.0 NORMED by  sum of values distance from 1.0 as opposed 0.0
             for user_weight in users_weightings:
                 identifier=user_weight["id"]
                 score=user_weight["score"]
                 score= (1.0-(score/normValue))/normInverse #(1.0-(score))/(5-normValue) #replace with z-score
                 database.set_weights(identifier,score)
             
             
             userHistory=database.get_history()
             for i in xrange(4):
                score=response.assign_Response_Score('choice'+str(i+1),userHistory,None)
                database.set_choice(i,score)
             response.select_Responses_to_Present(5,database.get_choices())
            
           # print userScores
         #get User Choices
        #Get all Users
        #Update test.updateClusters(None, all_users, None)
        #allUsers=response.calculate_All_User_Weights
        #UpdateDatabase for get Choices
        updated_choices=database.get_choices()
        choices_presented_to_user=response.select_Responses_to_Present(5,updated_choices)
        '''
        User 1: Douche Bag
        User 2: Don't Feel So Down Land ON Your feet
        User 3: Don't Feel So Down Lang On Your Feed
        User 4: More than one fish
        '''
        print choices_presented_to_user 
        for users in range(5):
            print "\n"+question[0][0] +"\n"
            print "\n Please select the response that will be helpful to this person:"
            prompt1_id=choices_presented_to_user[users][0]
            prompt2_id=choices_presented_to_user[users][1]
            prompt1_output=database.get_choice(int(prompt1_id))
            prompt2_output=database.get_choice(int(prompt2_id))
            associated_result={1:prompt1_id,2:prompt2_id}
            
            print "1. "+prompt1_output[0]
            print "2. "+prompt2_output[0]
            
            chosen_response=raw_input("Press your prefered choice: \n")
            chosen_response=associated_result[int(chosen_response)]
            
            current_value_in_db="choice"+str(chosen_response+1) #the selection in the database to get value
            
            #get the current number of times the given value was chosen in the db
            current_user_results=database.get_history()[users][current_value_in_db] #numeric amount of 'choice current_value_in_db' in database
            
            incremented_choice_for_user=current_user_results+1
            
            #a hash of the different prompt functino which relate to updated different values in the db
            hashFunctions_Prompts={"choice1":database.set_weights_choice1,"choice2":database.set_weights_choice2,"choice3":database.set_weights_choice3,"choice4":database.set_weights_choice4}
            
            #selects which choice prompt to incremenet
            set_weights=hashFunctions_Prompts[current_value_in_db]
            set_weights(users,incremented_choice_for_user)
            #set_weights_choice1
            
            print "USER RESULTS"
            print users
            print database.get_history()[users]
            print "next user"
            # raw_input("HOLD ON")
            #set_weights_choice4
            
           # vals=raw_input("KILL ME")
           # print vals
          #  print choices_presented_to_user
            
            #ChoicesResposnes=Get Choices Database
            #Select_Resposnes_To_Present(choicesResposnes)
            #print choices - Dict [Number IN DB, TO NUMBER OUTPUTTED IN PROMPT)
            #Get User Response
            #Get user ID
            #Update User Choices
            
            pass
        iteration+=1
    database.close()       
     #var Round
    #var Current_User_ID
    #var currently selected choice
    #var UserLearning
    #var ResponseUpdater
    #IN DB CREATE Question To ASK USER
    #IN DB CREATE OR LOAD CHOICES TO ASK USER
    #Initialize database for clusters, for choices...
    
    #Recalculate from DATABASE - CLUSTERS - RERUNS IT
    #
    
    #Current Choices TO Present
    #Prompt Question
    #Prompt Choices To Select
    #User Selects Chocie
    #Select Resposnes to present()
    #
    #After X ITERATIONS OF USERS 
    #Send User_Learning - Object - Update
    #Update User Information in DB
    #Send Update to choice selection
    #Update Scores of Choices to DB using Response_updater
    #
    #Do Another Prompt
    '''
    
    "SUP YO"
    test= User_Learning()
    response= Response_Updater()
    print "HUH"
    val= test.compareVectors([2,1], [0,10])
    print str(val)+" HUH"
    
    print test.compareUser(None, [1,2,3,5])
    
    
    
    for j in range(10):
        print j
        
    t=[1,2]
    
 
    all_users=[[1,4,1,4],[10,0,0,0],[1,4,1,4],[1,4,1,4]]
    
    for i in range(4):
        print i
        
        test.updateClusters(None, all_users, None)
        
        users=[{"id":1,"choices":[1,4,1,4]},{"id":2,"choices":[7,0,0,3]}]
        results=response.calculate_All_User_Weights(test, users)
        
        print results
        '''
        
    