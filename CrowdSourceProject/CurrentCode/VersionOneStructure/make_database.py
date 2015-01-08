import sqlite3 as sql

class Database():
    
    
    def __init__(self):
        
        self.questions = []
        self.choices = []
        
        self.conn = sql.connect('C:\sqlite3\Crowdsource_Project.sql')
        self.curr = self.conn.cursor()
        
        
    #weighting (user_id (pkey) INTEGER, weights DOUBLE, choice_1 INTEGER, choice_2 INTEGER, choice_3 INTEGER, choice_4 INTEGER, choice_5 INTEGER)
    def get_weights(self):
        #return self.curr.execute(select weights from weighting)
        pass
    def set_weights(self, id, value):
        pass
    def get_history(self):
        # return as dictionary {user_id: {weights: w, choice_1: c1,choice_2: c2, ...,}}
        pass

        
    #prompt_questions (prompts (pkey) STRING), fixed
    #database-end    
    def set_questions(self, questions = []):
        # add to database
        pass
    def get_questions(self):
        pass
        
    #user_end
    def get_displayed_questions(self):
        return self.questions
        
    #prompt_choices (choices (pkey) STRING, choice_value DOUBLE, number_chosen INTEGER, number_shown INTEGER)
    def update_choices(self, choices):
        # adds to database
        pass
    
    def get_choices(self, choice_id):
        #returns column of keys corresponding to the choice_id
        pass
        
    #user_end
    def get_displayed_choices(self):
        return self.choices

if __name__ == '__main__':
    Database()
    

    