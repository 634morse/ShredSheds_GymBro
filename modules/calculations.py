class Epley_Est_Calc:
    def __init__(self, weightmax, rep_range):
        start_str, end_str = rep_range.split('-')
        start = int(start_str)
        end = int(end_str)
        self.rep_range = (start_str, end_str)
        self.est_weights = {}
        return self.est_weights

        for rep in range(start, end + 1):
            self.est_weight = weightmax / (1 + 0.0333 * rep)
            self.est_weights[rep] = round(self.est_weight)


 
# weight = Epley_Est_Calc(235, "1-100")

# # print(weight.est_weights)
# print(weight.est_weights)
