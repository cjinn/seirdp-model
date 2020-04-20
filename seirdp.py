## Libraries
# Python Libraries
import numpy as np
import scipy.integrate
import matplotlib.pyplot as plt
import math

# Local Libraries
import covid_params # Change the values here if you want to adjust one variable at a time

class seirdp():
  def __init__(self, r0, r1, gamma, sigma, baseAlpha, rho, socDistResponseFactor=1.0, diseaseScalingFactor=0.1):
    # Assign variables
    self.r0 = r0
    self.r1 = r1
    self.gamma = gamma
    self.sigma = sigma
    self.baseAlpha = baseAlpha
    self.rho = rho
    self.socDistResponseFactor = socDistResponseFactor
    self.diseaseScalingFactor = diseaseScalingFactor

    # Flags
    self.thresholdPrintFlag = False # When True, prints a statement of when countermeasures go into effect

  ## Model of SEIRDP
  def model(self, Y, x, N, r0, thrPop, thrDay, r1, gamma, sigma, rho):
    S, E, I, R, D = Y

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
    alpha = self.alphaGenerated(I, N)

    dS = - beta * S * I / N
    dE = beta * S * I / N - sigma * E
    dI = sigma * E - (1 - alpha) * gamma * I - alpha * rho * I
    dR = (1 - alpha)*gamma * I
    dD = alpha*rho*I
    return dS, dE, dI, dR, dD

  ## Modelling R0 from before and after countermeasures
  def logisticFunction(self, x, x0, k):
    return (self.r0 - self.r1)/(1 + math.exp(-k*(-x + x0))) + self.r1

  ## Fatality Rate bases the kill rate based on 
  def alphaGenerated(self, I, N):
    overworkedAlpha = self.diseaseScalingFactor * I / N # If the population is not able to cope, this comes into play
    return overworkedAlpha + self.baseAlpha

  ## Getting the populations of the different states
  def solve(self, population, E0, thrPop, thrDay, daysModel):
    X = np.arange(daysModel)  # time steps array
    N0 = population - E0, E0, 0, 0, 0  # S, E, I, R at initial step
    self.thresholdPrintFlag = True
    
    y_data_var = scipy.integrate.odeint(self.model, N0, X, args=(
      population, self.r0, thrPop, thrDay, self.r1, self.gamma, self.sigma, self.rho))
      
    S, E, I, R, D = y_data_var.T  # transpose and unpack
    return X, S, E, I, R, D  # note these are all arrays

## If this is the main python file...
if __name__ == "__main__":
  E0 = 1  # exposed at initial time step

  modelInstance = seirdp(covid_params.r0, covid_params.r1, covid_params.GAMMA, covid_params.SIGMA,
    covid_params.BASE_ALPHA, covid_params.RHO_AVERAGE, covid_params.SOCIAL_DISTANCE_RESPONSE_FACTOR)
  X, S, E, I, R, D = modelInstance.solve(covid_params.POPULATION, E0, covid_params.SOCIAL_DISTANCE_THRESHOLD_POPULATION, covid_params.SOCIAL_DISTANCE_DAY, covid_params.DAYS_MODEL)

  # Plot
  fig = plt.figure(dpi=75, figsize=(20,16))
  ax = fig.add_subplot(111)
  ax.plot(X, S, 'o', color='orange', label='Susceptible')
  ax.plot(X, E, 'y', alpha=0.5, lw=2, label='Exposed (realtime)')
  ax.plot(X, I, 'r--', alpha=0.5, lw=1, label='Infected (realtime)')
  ax.plot(X, R, 'o', color='blue', label='Recovered')
  ax.plot(X, D, 'o', color='red', label='Dead (Disease)')

  ax.set_xlabel('Time (days)')
  ax.set_ylabel('Population')
  ax.set_ylim(bottom=1.0)
  legend = ax.legend(title='SEIRDP model')

  # Print numbers
  print('Number of Susceptible at Day ' + str(covid_params.DAYS_MODEL) + ': ' + str(S[-1]))
  print('Number of Exposed at Day ' + str(covid_params.DAYS_MODEL) + ': ' + str(E[-1]))
  print('Number of Infected at Day ' + str(covid_params.DAYS_MODEL) + ': ' + str(I[-1]))
  print('Number of Recovered at Day ' + str(covid_params.DAYS_MODEL) + ': ' + str(R[-1]))
  print('Number of Dead at Day ' + str(covid_params.DAYS_MODEL) + ': ' + str(D[-1]))

  # Display plot
  plt.show()
