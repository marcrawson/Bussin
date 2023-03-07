def getIdx0(idx0):
    weekday_vals = {"Monday": 1, "Tuesday": 1, "Wednesday": 1, "Thursday": 1,
                    "Friday": 1, "Saturday": 0.5, "Sunday": 0}
    result = -1
    result = weekday_vals[idx0]
    return result

def getIdx1(idx1):
    month_vals = {"January": 1, "February": 0.8, "March": 0.6,
                 "April": 0.4, "May": 0.2, "June": 0, "July": 0,
                 "August": 0.2, "September": 0.4, "October": 0.6,
                 "November": 0.8, "December": 1}
    result = -1
    result = month_vals[idx1]
    return result

def getIdx2(idx2):
    return 1

def getIdx3(idx3):
    if (idx3 == "yes"):
        return 1
    else:
        return 0

def getIdx4(idx4):
    idx4 = float(idx4)
    result = -1
    if idx4 < 5:
        result = 1
    elif idx4 < 15:
        result = 0.5
    else:
        result = 0
    return result

def getIdx5(idx5):
    precipitation_vals = {"None": 0, "Light": 0.5, "Heavy": 1}
    result = -1
    result = precipitation_vals[idx5]
    return result

def getIdx6(idx6):
    idx6 = float(idx6)
    result = -1
    if idx6 < 5:
        result = 1
    elif idx6 < 10:
        result = 0.5
    else:
        result = 0
    return result

def make24HR(time):
    result = ""
    time.strip()
    sep_time = time.split(" ")
    if sep_time[1] == "PM":
        time_nums = sep_time[0].split(":")
        result = str((int(time_nums[0]) + 12) % 24) + ":" + time_nums[1]
    else:
        result = sep_time[0]
    return result