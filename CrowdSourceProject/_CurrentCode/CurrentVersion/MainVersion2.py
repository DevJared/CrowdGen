'''
Created on Dec 20, 2014

@author: COMP
'''
from ClassOutline import User_Learning, Response_Updater
from make_database import Database

if __name__ == '__main__':
    array=User_Learning()
    response=Response_Updater()

    database=Database()
    print "SUP YOU"

    storeUsers=[]
    
    CurrentQuestionPrompt=""
    options=["",""]
    #get actual option value in database
    
    #getQuestion
    question=database.get_questions()
    for prompt_statements in range(4):
        for users in range(5):
            pass
     
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
    print "SUP YO"
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
        