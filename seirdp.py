## Libraries
# Python Libraries
import numpy as np
import scipy.integrate
import matplotlib.pyplot as plt
import math

# Local Libraries
import covid_params # Change the values here if you want to adjust one variable at a time

DAYS_MODEL = 100

class seirdp():
  def __init__(self, r0, r1, gamma, sigma, optimalKillRate, fatalityRateAvg, birthRateDaily=0.0, natDeathRateDaily=0.0, socDistResponseFactor=1.0, diseaseScalingFactor=0.0):
    # Assign variables
    self.r0 = r0
    self.r1 = r1
    self.gamma = gamma
    self.sigma = sigma
    self.alphaOptimal = optimalKillRate
    self.pho = fatalityRateAvg
    self.birthRateDaily = birthRateDaily
    self.natDeathRateDaily = natDeathRateDaily
    self.socDistResponseFactor = socDistResponseFactor
    self.diseaseScalingFactor = diseaseScalingFactor

    # Flags
    self.thresholdPrintFlag = False # When True, prints a statement of when countermeasures go into effect

  ## Model of SEIRDP
  def model(self, Y, x, N, r0, thrPop, thrDay, r1, gamma, sigma, pho):
    S, E, I, R, D, P = Y

    # Disease population hits threshold. Begin social distancing
    if ((I + R + D) > thrPop and x < thrDay):
      thrDay = x

    # Assigning constants
    if (x >= thrDay):
        if self.thresholdPrintFlag:
          print("Countermeasures come into effect on day: " + str(x))
          self.thresholdPrintFlag = False

        beta = self.logisticFunction(x, thrDay, self.socDistResponseFactor) * gamma
    else:
      beta = r0*gamma
    alpha = self.fatalityRate(I, N)

    dS = - beta * S * I / N + self.birthRateDaily * N - self.natDeathRateDaily * S
    dE = beta * S * I / N - sigma * E + self.birthRateDaily * E
    dI = sigma * E - (1 - alpha)*gamma * I + self.birthRateDaily * I
    dR = (1 - alpha)*gamma * I - alpha*pho*I - self.natDeathRateDaily * R + self.birthRateDaily * N
    dD = alpha*pho*I
    dP = self.natDeathRateDaily* (S + R)
    return dS, dE, dI, dR, dD, dP

  ## Modelling R0 from before and after social distancing
  def logisticFunction(self, x, x0, k):
    return (self.r0 - self.r1)/(1 + math.exp(-k*(-x + x0))) + self.r1

  ## Fatality Rate is much higher when more people are infected
  def fatalityRate(self, I, N):
    return self.diseaseScalingFactor * I / N + self.alphaOptimal

  ## Getting the populations of the different states
  def solve(self, population, E0, thrPop, thrDay, daysModel):
    X = np.arange(daysModel)  # time steps array
    N0 = population - E0, E0, 0, 0, 0, 0  # S, E, I, R, D at initial step
    self.thresholdPrintFlag = True
    
    y_data_var = scipy.integrate.odeint(self.model, N0, X, args=(
      population, self.r0, thrPop, thrDay, self.r1, self.gamma, self.sigma, self.pho))
      
    S, E, I, R, D, P = y_data_var.T  # transpose and unpack
    return X, S, E, I, R, D, P  # note these are all arrays

## If this is the main python file...
if __name__ == "__main__":
  E0 = 1  # exposed at initial time step

  modelInstance = seirdp(covid_params.r0, covid_params.r1, covid_params.GAMMA, covid_params.SIGMA, covid_params.KILL_RATE, covid_params.FATALITY_RATE_AVERAGE,
    covid_params.BIRTH_RATE_ANNUAL/covid_params.NUM_DAYS_IN_YEAR, covid_params.NATURAL_DEATH_RATE_ANNUAL/covid_params.NUM_DAYS_IN_YEAR, covid_params.SOCIAL_DISTANCE_RESPONSE_FACTOR)
  X, S, E, I, R, D, P = modelInstance.solve(covid_params.POPULATION, E0, covid_params.SOCIAL_DISTANCE_THRESHOLD_POPULATION, covid_params.SOCIAL_DISTANCE_DAY, DAYS_MODEL)

  # Plot
  fig = plt.figure(dpi=75, figsize=(20,16))
  ax = fig.add_subplot(111)
  ax.plot(X, S, 'o', color='orange', label='Susceptible')
  ax.plot(X, E, 'y', alpha=0.5, lw=2, label='Exposed (realtime)')
  ax.plot(X, I, 'r--', alpha=0.5, lw=1, label='Infected (realtime)')
  ax.plot(X, R, 'o', color='red', label='Recovered')
  ax.plot(X, D, 'o', color='black', label='Dead (Disease)')
  ax.plot(X, P, 'o', color='grey', label='Pass Away')

  ax.set_xlabel('Time (days)')
  ax.set_ylabel('Population')
  ax.set_ylim(bottom=1.0)
  legend = ax.legend(title='SEIRDP model')

  # Display plot
  plt.show()

  # Print numbers
  print('Number of Susceptible at Day ' + str(DAYS_MODEL) + ': ' + str(S[-1]))
  print('Number of Exposed at Day ' + str(DAYS_MODEL) + ': ' + str(E[-1]))
  print('Number of Infected at Day ' + str(DAYS_MODEL) + ': ' + str(I[-1]))
  print('Number of Recovered at Day ' + str(DAYS_MODEL) + ': ' + str(R[-1]))
  print('Number of Dead due to Disease at Day ' + str(DAYS_MODEL) + ': ' + str(D[-1]))
  print('Number of Dead due to "natural causes" at Day ' + str(DAYS_MODEL) + ': ' +str( P[-1]))
