import json

class bag:

    reward = {}

    def __init__(self):
        pass

    def getReward(self, rewardName, rewardQuantity):
        if rewardName in self.reward:
            self.reward[rewardName] = self.reward[rewardName] + rewardQuantity
        else:
           self.reward[rewardName] = rewardQuantity


    def getAllRewards(self):
        print(json.dumps(self.reward))
