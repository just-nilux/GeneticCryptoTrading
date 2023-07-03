import random


class Agent():
    def __init__(self, actions):
        self.fitting = 0
        self.priceHistory = []
        self.last_action = 0  # only -1 or 1
        self.possibleActions = random.choices([True, False], k=actions)
        self.actionsBeforeAct = 0
        self.config = dict()
        self.weight = []
        for i in range(actions):
            self.config[str(i)] = {"activate":False}
        for i in range(actions):
            if self.possibleActions[i]:
                self.generate_action(i)
        for i in range(actions):
            self.weight.append(random.uniform(-1, 1))

    def get_score(self) -> float:
        return self.fitting

    def remove_history(self):
        self.priceHistory = []
        self.last_action = 0

    def determine_action(self,candle) -> int:
        # either return -1 sell;0 do nothing;+1 buy
        return 1

    def swap_action(self, i, action):
        self.config[str(i)] = action

    def swap_weight(self, i, new_weigh):
        self.config[str(i)] = new_weigh

    def cf_tf_cd(self,i):
        self.config[str(i)]["candle"] = random.choices(["High", "Low", "Close", "Open"])
        self.config[str(i)]["timeframe"] = random.choices([1, 5, 10, 30, 60, 120, 240, 480, 1440, 43200, 10080])
        self.config[str(i)]["activate"] = True

    def generate_action(self, i):
        # 0     moving average ( trendfolowing)
        # 1     exponential moving average
        # 2     Volume moving average
        # 3     Average volume line
        # 4     SAR
        # 5     moving average cross
        # 6     exponential moving average cross
        # 7     Volume moving average cross
        # 8     Average volume line cross
        # 9     MACD
        # 10    RSI
        # 11    Stochastic RSI
        # 12    Volume diff
        # 13    Bollinger Bands
        # 14    Moving flow index
        # 15    KDJ index
        # 16    On balance volume
        # 17    Commodity Channel Index
        # 18    Wm%R
        # 19    Directional Movement Index
        # 20    MTM - Momentum Index
        # 21    Ease of Movement Value
        self.cf_tf_cd(i)
        if i == 0:
            self.config["0"]["length"] = random.randint(2,500)

        elif i == 1:
            self.config["1"]["length"] = random.randint(2,500)


        elif i == 2:
            self.config["2"]["length"] = random.randint(2, 500)

        