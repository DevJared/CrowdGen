'''
Created on Dec 20, 2014

@author: COMP
'''
import math
from array import *
from _random import Random
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
        self.totalCluster1=0 #Number who were chosen in this cluster
        self.totalCluster2=0 #Number who were chosen in this cluster
        self.UserCluster1=[1,3.9,1,4] # 1,3 1Array Of Choices Double - Where length is equal to the total number of choices
        self.UserCluster2=[1,3.9,1,4] #Array Of Choices Double
        self.summedDistanceAcrossUsers_UserCluster1=-1.0 #The summed distance across all users to user cluster1
        self.summedDistanceAcrossUsers_UserCluster2=-1.0 #The summer distance across all users to user cluster2
        
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
    
    def getCluster(self,id):
        if id==1: return self.UserCluster1
        if id==2: return self.UserCluster2
        raise Exception("ERROR AT  getCLUSTER")
    
    def instantiateClusters(self,list_of_users):
        copyArry=[]
          
        
        cluster1=self.UserCluster1
        cluster2=self.UserCluster2
        rand=Random()
        for j in range(len(cluster1)):
            
            val=rand.random()*len(list_of_users)
            cluster1[j]=list_of_users[int(val)][j]
              
              
        for j in range(len(cluster2)):
            
            val=rand.random()*len(list_of_users)
            cluster2[j]=list_of_users[int(val)][j]    
            
    
    def normClusters(self):
        pass
    
    
    #updates representation of what users are closer to
    def updateClusters(self,all_user_dict,user_choice_table,scalar):
        #assume all_user_dict would hold user_choice table - User_choice _Table is now just a giant vector [[1,2,3,4],[1,2,3,4],etc]
        #I hate doing it this way, so bad, so be it
        cluster1Group=[]
        cluster2Group=[]
        self.summedDistanceAcrossUsers_UserCluster1=0.0
        self.summedDistanceAcrossUsers_UserCluster2=0.0 
        for i in user_choice_table:
            userDec=self.compareUser(None, i)
            
            self.summedDistanceAcrossUsers_UserCluster1+=userDec["Clusters"][0][1]
            self.summedDistanceAcrossUsers_UserCluster2+=userDec["Clusters"][1][1]
            
            if userDec["Best"][2]=="cluster1":
                cluster1Group.append(i)
            else: cluster2Group.append(i)
        
        cluster1_new_Mean=[0.0 for i in range(len(self.UserCluster1))]
        cluster2_new_Mean=[0.0 for i in range(len(self.UserCluster2))]
        
        #Get average for cluster
        for i in cluster1Group:
            #for the length of each array in this cluster group
            for j in range(len(i)):
                cluster1_new_Mean[j]+=i[j]
        
        for j in range(len(cluster1_new_Mean)):
            
            if len(cluster1Group)==0:
                cluster1_new_Mean[j]=0.0 #This should be addressed, unknown is equivalent to not chosen
            else:cluster1_new_Mean[j]=cluster1_new_Mean[j]/float(len(cluster1Group))
         
        for i in cluster2Group:
            #for the length of each array in this cluster group
            for j in range(len(i)):
                cluster2_new_Mean[j]+=i[j]      
                
        
        for j in range(len(cluster2_new_Mean)):
            
            if len(cluster2Group)==0:
                cluster2_new_Mean[j]=0.0 #This should be addressed, unknown is equivalent to not chosen
            else:cluster2_new_Mean[j]=cluster2_new_Mean[j]/float(len(cluster2Group))
        #user dict: History of users choices - calculates the score of a choices and returns it
       
        #record who was chosen for each group 
        self.totalCluster1=len(cluster1Group)
        self.totalCluster2=len(cluster2Group)
        
        if len(cluster2Group)!=0: self.UserCluster2=cluster2_new_Mean
        if len(cluster1Group)!=0: self.UserCluster1=cluster1_new_Mean
            
    
    #Comapre a user to a cluster - Returns Distance summed Across Cluster
    #user_vector is a value that would normally not be stored
    def compareUser(self,user_dict,user_vector):
        best=9999999.0 #Best is shortest distance
        clust1Distance=self.compareVectors(user_vector, self.UserCluster1, None)
        clust2Distance=self.compareVectors(user_vector, self.UserCluster2, None)
        
        normDistance=clust1Distance+clust2Distance
        if normDistance==0.0: normDistance=1.0
        
        clust1Distance=clust1Distance#/normDistance No norm Distance - IF I uSE NORM DISTNACE IT IS NORMALIZING HOW GOOD ONE CLUSTER IS OVER
        clust2Distance=clust2Distance# /normDistance
        
        cl1=(self.UserCluster1,clust1Distance,"cluster1")
        cl2=(self.UserCluster2,clust2Distance,"cluster2")
        best=None
        #if even distance, select randomly
        if clust1Distance==clust2Distance:
            r=Random()
            chance=r.random()
            if chance > .5: best=cl1
            else: best=cl2
        elif clust1Distance>clust2Distance:
            best=cl2
        else: best=cl1
        # dict={"Best":()}
        dict={"Best":best,"Clusters":[cl1,cl2]}
        return dict
    
    #compares distance to two vectors
    def compareVectors(self,user,vector,measurement_function=None):
        if type(user)!=type([]): raise Exception("PROBLEM IN COMPARE VECTORs")
        if type(vector)!=type([]): raise Exception("PROBLEM IN COMPARE VECTORs")
        if(len(user)!=len(vector)): raise Exception("PROBLEM IN COMPARE VECTORs") 
        
        size=len(user)
        
        diff_vec=[0 for i in range(size) ]
        distance=0.0 #distance between two vectors
        
        i=0
        while i < size:
            diff_vec[i]= vector[i]-user[i]
            i+=1        
        
        
        if measurement_function==None:
            for i in diff_vec:
                distance+=math.pow(i,2)
        else:
            distance= measurement_function(diff_vec)
        
        return distance
    
#Used to choose what responses to present to users to have the option choose
class Response_Updater():
     
     def __init__(self):
        
        pass
     
     def calculate_All_User_Weights_Initialize(self,number_of_users):
         weight=1.0/float(number_of_users)
         arry=[]
         for i in range(number_of_users):
             pair={"id":i,"score":weight,"pair":(i,weight)}
             arry.append(pair)
          
         return arry
            
     
     def calculate_All_User_Weights(self, User_Learning_Object, all_user_data_matrix):
         
         arry=[]
         #Assumes i is a key value in matrix
         id_counter=0
         for i in all_user_data_matrix:
             
             score=self.calculate_User_Weight_Clusters(User_Learning_Object, i)
             id=id_counter
             pair= {"id":id,"score":score,"pair":(id,score)}
             arry.append(pair)
             id_counter+=1
         return arry
     
     #cacluates the score of each cluster and combines the two, norms the values as well
     def calculate_User_Weight_Clusters(self,User_Learning_Object,user_vector):
         
         vals= User_Learning_Object.compareUser(None, user_vector)
         
         #These should be above 0, or it has not been run yet
         normCluster1=User_Learning_Object.summedDistanceAcrossUsers_UserCluster1
         normCluster2=User_Learning_Object.summedDistanceAcrossUsers_UserCluster2
         
         valueCluster1=vals["Clusters"][0][1]
         valueCluster2=vals["Clusters"][1][1]
         
         scoreCluster1=0.0
         scoreCluster2=0.0
         
         if normCluster1<0.0 and normCluster2<0.0: 
             raise Exception("ERROR IN CALCULATE USER WEIGHT CLUSTERS - NEED TO RUN AT LEAST ONE UPDATE IN USER_LEARNING_OBJECT BEFORE CALUCATING WEIGHTS")
         
         if normCluster1>=0.0:
            # scoreCluster1=1-(valueCluster1/normCluster1)
            scoreCluster1=valueCluster1
         
         if normCluster2>=0.0:
           # scoreCluster2=1-(valueCluster2/normCluster2)   
           scoreCluster2=valueCluster2   
         
         norm= User_Learning_Object.totalCluster1+User_Learning_Object.totalCluster2
         
         
         
         cluster1Weight=float(User_Learning_Object.totalCluster1)/float(norm)
         
         cluster2Weight=float(User_Learning_Object.totalCluster2)/float(norm)
         
         score= (((scoreCluster1*cluster1Weight)+(scoreCluster2*cluster2Weight))/2.0)

         return score
         #cluster is a vector
         #all users is a vector of the poitns of a given user
         #user is a vector for a specific user
         
         #get distance from every user to cluster
         #norm
         #1-Norm For every user to get their weight
         
                                       #1-distnace
    #calculates the current 'goodness' of a response
    #Extension is goodness across clusters
     def assign_Response_Score(self,choice_number,choice_history_of_every_user,choice_history):
         
        
        # total_appear=choice_history[3] #how many times it has appeared
        # total_chosen=choice_history[4] #how many times has it been chosen
         #norm_arry_ids = lists_id for each vote
         #OverAll Weighting
         
         
         score=0.0
         for choice_history in choice_history_of_every_user:
             i=choice_history_of_every_user[choice_history] #get the dict of each user
             print i
             totalChoices=0.0
             #get summed occurrences for a given user
          
             
             
                 #i is a user
             weight=i['weight'] #Wieght how 'important' is a user
             
             numberTimesChosen=i[choice_number]
              
             score+=numberTimesChosen*weight #How many times a score is chosen times how well it is weighted
             
        
         return score
         
         
             
         #Profile Closeness Value - User Weights
         #number of people who have chosen it, and how many people showed up
         # number_times_chosen, number_times_viewed
         pass
     
    
     def select_Responses_to_Present(self,number_of_users,prompt_choices_table):
        
        responses = {}
        rand=Random()
        for m in xrange(number_of_users):
            user_values = []
            for i in xrange(len(prompt_choices_table)):
                val = (prompt_choices_table[i][2])
                user_values.append(val)
            total_value = sum(user_values) 
            normalization = [k/total_value for k in user_values]
            print "probabilities"
            print normalization
            
            indices = range(len(prompt_choices_table))
            new_responses = []
            
            #print normalization
            #first draw
           
            ball1 = rand.random()

            allowed1 = []
            
            for i in xrange(len(prompt_choices_table)):
                 if sum(normalization[:i+1])-ball1 >= 0: 
                     allowed1.append(i)  
            new_choice1 = min(allowed1)
            new_responses.append(new_choice1)
            

            normalization.pop(new_choice1) #remove element and then renormalize
            indices.pop(new_choice1) #remove the index
            
            total_value2 = sum(normalization)  
            normalization2 = [(k/total_value2) for k in normalization]

            #second draw
            ball2 = rand.random()
            allowed2 = []
            for i in xrange(len(prompt_choices_table)-1):
                 if sum(normalization2[:i+1])-ball2 >= 0: 
                     allowed2.append(i)  
            temp_choice2 = min(allowed2)
            new_choice2 = indices.pop(temp_choice2) #get the element from index at spot temp_choice2
            new_responses.append(new_choice2) 
            
            responses.update({m:new_responses})
        return responses
         
         #.7 0 1 0 
         #.25 .25 .25 .25
         #1 0 0 0
         #1 0 0 0
         #1 .25 .25 .25
         #.5 .25 .5 .25
         #value = Weight * number/number shown
         #normalize(value)
         #Sample Based on Value - NUMPY
         #numpy random multinominal 
         #Return choice
         #
#class Main Logic
#UserLearning
#Sampling_Response
        