# Python Libraries
import statistics

# Constants (Do not change this!)
NUM_DAYS_IN_YEAR = 365

## Population
POPULATION = 10000
DAYS_MODEL = 150

SOCIAL_DISTANCE_RESPONSE_FACTOR = 0.5 # Factor that states how the population is willing to comply to social distancing
POPULATION_PROPORTION_AGE_RANGE = {
    "0-1": 0.01, 
    "2-29": 0.19,
    "30-59": 0.3,
    "60-89": 0.3,
    "89+": 0.2
}

## Disease-specific
r0 = 2.5 # https://en.wikipedia.org/wiki/Basic_reproduction_number
r1 = 1.08  # reproduction number after quarantine measures
BASE_ALPHA = 0.07 # Probability that the disease kills an infected person on a good day
RHO_AGE_RANGE = { # Rate at which people die (1/6 = 6 days to kill a person)
  "0-1": 0.50,
  "2-29": 0.01,
  "30-59": 0.2,
  "60-89": 0.4,
  "89+": 0.6
}
RHO_AVERAGE = sum(POPULATION_PROPORTION_AGE_RANGE[ii]*RHO_AGE_RANGE[ii] 
  for ii in list(POPULATION_PROPORTION_AGE_RANGE.keys())) # Gets the average fatality rate across the different ages

TIME_PRESYMPTOMATIC = 2.5 # Not sure where this came from
SIGMA = 1.0 / (5.2 - TIME_PRESYMPTOMATIC)  # The rate at which an exposed person becomes infectious.  symptom onset - presympomatic
GAMMA = 1.0 / (2.0 * (4.6 - 1.0 / SIGMA))  # The rate an infectious person recovers and moves into the recovered phase. Note that for the model it only means he does not infect anybody any more.

## Disease Response
SOCIAL_DISTANCE_THRESHOLD_POPULATION = 200 # Threshold for infected population for social distancing to take into effect
SOCIAL_DISTANCE_DAY = 57 # Day Social Distancing happened
