from _ml import MLAgent, train, save, load, train_and_plot
from _core import is_winner, opponent, start
 
start()


# class MyAgent(MLAgent):
#     def evaluate(self, board):
#         if is_winner(board, self.symbol):
#             reward = 1
#         elif is_winner(board, opponent[self.symbol]):
#             reward = -1
#         else:
#             reward = 0
#         return reward
    
 
# my_agent = MyAgent()

# train(my_agent, 3000)

# #save(my_agent, 'MyAgent_3000')

# #my_agent=load('MyAgent_3000')

# # zet de onderstaande regel aan aan om de agent te stoppen met leren en alleen de beste zetten te gebruiken
# #my_agent.learning = False

# start(player_x=my_agent)