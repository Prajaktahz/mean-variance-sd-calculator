import numpy as np
import math 

def calculate(list):
    list_size = len(list)
    #print(list_size)
    if (list_size == 9) :
      list_sum = sum(list)
      list_mean = list_sum/9
      list_max = max(list)
      list_min = min(list)
      list_variance = np.var(list)
      #print(list_variance)
      l = list[0:3]
      m = list[3:6]
      n = list[6:9]
      matrix = np.array([l,m,n])
      #print(matrix)
      calculatedValues = {
        'mean': getCalculations(matrix, list_mean, "mean"),
        'variance' : getCalculations(matrix, list_variance, "variance"),
        'standard deviation': getCalculations(matrix, list_variance, "standardDeviation"),
        'max': getCalculations(matrix, list_max, "max"),
        'min': getCalculations(matrix, list_min, "min"),
        'sum' : getCalculations(matrix, list_sum, "sum"),
      }
      return calculatedValues
    else:
      raise ValueError("List must contain nine numbers.")

def getCalculations(matrix, list_val, type):
  if(type == "mean"):
    return getFinalResult(np.mean(matrix, axis = 0), np.mean(matrix, axis = 1), list_val)
  elif(type == "variance"):
    return getFinalResult(np.var(matrix, axis = 0), np.var(matrix, axis = 1), list_val)
  elif(type == "standardDeviation"):
    return getFinalResult(np.std(matrix, axis = 0), np.std(matrix, axis = 1), math.sqrt(list_val))
  elif(type == "sum"):
      return getFinalResult(np.sum(matrix, axis = 0), np.sum(matrix, axis = 1), list_val)
  elif(type == "max"):
      return getFinalResult(np.max(matrix, axis = 0), np.max(matrix, axis = 1), list_val)
  elif(type == "min"):
    return getFinalResult(np.min(matrix, axis = 0),np.min(matrix, axis = 1),list_val)

def getFinalResult(val0, val1, list_val):
  res = []
  res.append(list(val0))
  res.append(list(val1))
  res.append(list_val)
  return res