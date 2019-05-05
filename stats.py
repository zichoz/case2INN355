import pandas as pd
import math
def load_data_pandas(filename):
    DataFrame = pd.read_csv(filename)   #Creates a dataframe of the data read by the read_csv()
    return DataFrame

def mape(diff_time, act_time):
    sigma = 0
    n = len(diff_time)
    nans = 0
    for c, b in zip(diff_time, act_time):
        if math.isnan(c) or math.isnan(b) or (math.isnan(c) and math.isnan(b)):
            nans += 1
        if not math.isnan(b) and not math.isnan(c):
            sigma = sigma + abs((c / b))
    #n = n - nans
    m = (100 / n) * sigma
    return m

def mae(diff_time, act_time):
    sigma = 0
    n = len(diff_time)
    nans = 0
    for c in diff_time:
        if math.isnan(c):
            nans += 1
        if not math.isnan(c):
            sigma = sigma + (abs(c))
    #n = n - nans
    m = (1/n) * sigma
    return m


def mse(diff_time):
    sigma = 0
    n = len(diff_time)
    nans = 0
    for c in diff_time:
        if math.isnan(c):
           nans += 1
        if not math.isnan(c):
            sigma = sigma + (c ** 2)
    #n += n - nans
    m = (1/n) * sigma
    return m
def rmse(pred_time, diff_time):
    sigma = 0
    n = len(pred_time)
    print(n)
    for c, b in zip(pred_time, act_time):
        if not math.isnan(c) and not math.isnan(b):
            #print(sigma)
            calc = (c - b) ** 2
            sigma += calc
    rmse = math.sqrt(sigma/n)
    return rmse

df = load_data_pandas("hpforestnaaerdetnokkkk_VALIDATE.csv")
df = df.values.tolist()
diff_time = []
act_time =[]
pred_time = []



for x in df: #adding them to list
    act_time.append(x[0])
    pred_time.append(x[1])
    diff_time.append(x[2])


print("mape")
print(mape(diff_time, act_time))
print("mae")
print(mae(diff_time, act_time))
print("mse")
print(mse(diff_time))
print("rmse")
print(rmse(pred_time, act_time))
