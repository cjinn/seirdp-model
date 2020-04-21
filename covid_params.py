# Python Libraries
import statistics

# Constants (Do not change this!)
NUM_DAYS_IN_YEAR = 365

## Population
POPULATION = 1000
DAYS_MODEL = 150

SOCIAL_DISTANCE_RESPONSE_FACTOR = 0.5 # Factor that states how the population is willing to comply to social distancing
POPULATION_PROPORTION_AGE_RANGE = {
  "0-14": 0.26, 
  "15-65": 0.65,
  "65+": 0.09
}

## Disease-specific
r0 = 2.0 # https://en.wikipedia.org/wiki/Basic_reproduction_number
r1 = 0.88  # reproduction number after quarantine measures
BASE_ALPHA = 0.07 # Probability that the disease kills a infected person on a good day
RHO_AGE_RANGE = { # Rate at which people die (1/6 = 6 days to kill a person)
  "0-14": 0.002,
  "15-65": 0.021,
  "65+": 0.264
}
RHO_AVERAGE = sum(POPULATION_PROPORTION_AGE_RANGE[ii]*RHO_AGE_RANGE[ii] 
  for ii in list(POPULATION_PROPORTION_AGE_RANGE.keys())) # Gets the average fatality rate across the different ages

SIGMA = 0.37  # The rate at which an exposed person becomes infectious.  symptom onset - presympomatic
GAMMA = 1.0 / (2.0 * (4.6 - 1.0 / SIGMA))  # The rate an infectious person recovers and moves into the recovered phase. Note that for the model it only means he does not infect anybody any more.

## Disease Response
# SOCIAL_DISTANCE_THRESHOLD_POPULATION = 0.0 # Threshold for infected population for social distancing to take into effect
SOCIAL_DISTANCE_DAY = 57 # Day Social Distancing happened
DISEASE_SCALING_FACTOR = 1.0
