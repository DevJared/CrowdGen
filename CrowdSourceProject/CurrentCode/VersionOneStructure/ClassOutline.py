'''
Created on Dec 20, 2014

@author: COMP
'''

#

class Template():
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
'''
Used for making decisions, and interface with user
'''
class Main_Logic():
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
    pass
'''
Learning Weights Of A User
'''
class User_Learning():
    def __init__(self):
        self.totalCluster1=0
        self.totalCluster2=0
        self.UserCluster1=[0,0,0,0] # 1,3 1Array Of Choices Double - Where length is equal to the total number of choices
        self.UserCluster2=[0,0,0,0] #Array Of Choices Double
        
        '''
        User 1: [1,0,0,0,0]
        
        User1: [0,1,0,0,0]
        
        UserCluster1=[.1,.3.,.7,.2,.2] - User1
        UserCluster2=[.2,.3,.4,.2,.2] - User2
        
        UserCluster1=[0,1,0,0,0]
        UserCluster2=[.2,.3....]
        
        UserCluster2[1,0,0,0,0]
        
        UserCluster[0,0,0,0,0]
        UserCluster[1,0,0,0,0] user 1
        UserCluster[1,1,0,0,0] user 2
        UserCluster[2,1,0,0,0] user 3
        UserCluster[2,1,1,0,0] user 4
        
        
        
        UserCluster[.5,.25,.25,0,0]
        
        
        User 2 = 2
        
        '''
        
        pass
    pass
    
    #updates representation of what users are closer to
    def updateClusters(self,all_user_dict):
        #user dict: History of users choices - calculates the score of a choices and returns it
        pass
    
    #Comapre a user to a cluster - Returns Distance summed Across Cluster
    def compareUser(self,user_dict):
        return None
    
    
    
    
    
#Used to choose what responses to present to users to have the option choose
class Response_Updater():
    
     def __init__(self):
        
        
        pass
    
    #calculates the current 'goodness' of a response
    #Extension is goodness across clusters
     def assign_Response_Score(self,choice_number,choice_history_of_every_user):
         #Profile Closeness Value - User Weights
         #number of people who have chosen it, and how many people showed up
         pass
    
     def select_Responses_to_Present(self,user_dict,prompt_choices_table):
         #value = Weight * number/number shown
         #normalize(value)
         #Sample Based on Value - NUMPY
         #numpy random multinominal 
         #Return choice
         #
#class Main Logic
#UserLearning
#Sampling_Response
        