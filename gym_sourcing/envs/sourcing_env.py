import gym
from gym import error, spaces, utils
import numpy as np


class SourcingEnv(gym.Env):
      metadata = {'render.modes': ['human']}

      Supplier_1_Probability = 0.2
      Supplier_2_Probability = 0.3
      Supplier_3_Probability = 0.5
      Supplier_4_Probability = 0.7
      Supplier_5_Probability = 0.8
      Supplier_1_Price = 20
      Supplier_2_Price = 30
      Supplier_3_Price = 40
      Supplier_4_Price = 70
      Supplier_5_Price = 150
      Number_of_articles = 5

      def takeAction(self,action):
          rand_number =  np.random.uniform(0,1)
          if action == 0:
              if self.current_money >= self.Supplier_1_Price:
                self.current_money = self.current_money - self.Supplier_1_Price
                if rand_number < self.Supplier_1_Probability:
                    self.current_articles = self.current_articles + self.Number_of_articles
                    return True
          if action == 1:
              if self.current_money >= self.Supplier_2_Price:
                self.current_money = self.current_money - self.Supplier_2_Price
                if rand_number < self.Supplier_2_Probability:
                    self.current_articles = self.current_articles + self.Number_of_articles
                    return True
          if action == 2:
              if self.current_money >= self.Supplier_3_Price:
                self.current_money = self.current_money - self.Supplier_3_Price
                if rand_number < self.Supplier_3_Probability:
                    self.current_articles = self.current_articles + self.Number_of_articles
                    return True
          if action == 3:
              if self.current_money >= self.Supplier_4_Price:
                self.current_money = self.current_money - self.Supplier_4_Price
                if rand_number < self.Supplier_4_Probability:
                    self.current_articles = self.current_articles + self.Number_of_articles
                    return True
          if action == 4:
              if self.current_money >= self.Supplier_5_Price:
                self.current_money = self.current_money - self.Supplier_5_Price
                if rand_number < self.Supplier_5_Probability:
                    self.current_articles = self.current_articles + self.Number_of_articles
                    return True
          return False

      def __init__(self):
        self.state = (1,)
        MAX_AMOUNT_OF_MONEY = 1000
        self.action_space = spaces.Discrete(5)
        self.observation_space = spaces.Discrete(60)
        self.reset()

      def step(self, action):
        self.done = self.current_money<20 or self.current_articles == 50
        assert self.action_space.contains(action), "%r (%s) invalid" % (action, type(action))
        state = self.state
        bought = self.takeAction(action)
        self.reward = (self.current_articles/50)**(0.9)
        return self.current_articles, self.reward, self.done, {}

      def reset(self):
        self.state = (0)
        self.current_money = self.MAX_AMOUNT_OF_MONEY
        self.current_articles = 0
        return 0

      def render(self):
        print(self.current_articles,self.current_money,self.done)

      def get_current_money(self):
        return int(self.current_money)




