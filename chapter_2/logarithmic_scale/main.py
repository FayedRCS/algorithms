import math

def log_scale(data, base):
    #assumes there are only valid values in data, hence no exception handling   
    
    logarithms = []
    
    #iterate throught the data in list, return log of data with base number
    for i in data:
        log = math.log(i, base)
        logarithms.append(log)
    
    return logarithms





