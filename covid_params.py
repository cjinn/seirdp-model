# Python Libraries
import statistics

# Constants (Do not change this!)
NUM_DAYS_IN_YEAR = 365

# Population
POPULATION = 10000
DAYS_TOTAL = 100

SOCIAL_DISTANCE_RESPONSE_FACTOR = 0.5 # Factor that states how the population is willing to comply to social distancing
POPULATION_PROPORTION_AGE_RANGE = {
    "0-1": 0.01, 
    "2-29": 0.19,
    "30-59": 0.3,
    "60-89": 0.3,
    "89+": 0.2
}
BIRTH_RATE_ANNUAL = 15/1000
NATURAL_DEATH_RATE_ANNUAL = 7/1000 # Death due to non-disease-related causes
IMMIGRATION_RATE = 1 # Immigration rate
EMIGRATION_RATE = 1 # Emigration rate

# Disease-specific
r0 = 2.3 # https://en.wikipedia.org/wiki/Basic_reproduction_number
r1 = 1.8  # reproduction number after quarantine measures - https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3539694
          # it seems likely that measures will become more restrictive if r1 is not small enough
TIME_PRESYMPTOMATIC = 2.5
KILL_RATE = 0.1 # Probability that the disease kills
FATALITY_RATE_AGE = {
  "0-1": 0.50,
  "2-29": 0.01,
  "30-59": 0.05,
  "60-89": 0.20,
  "89+": 0.30
}
FATALITY_RATE_AVERAGE = sum(POPULATION_PROPORTION_AGE_RANGE[ii]*FATALITY_RATE_AGE[ii] 
  for ii in list(POPULATION_PROPORTION_AGE_RANGE.keys()))

SIGMA = 1.0 / (5.2 - TIME_PRESYMPTOMATIC)  # The rate at which an exposed person becomes infectious.  symptom onset - presympomatic
GAMMA = 1.0 / (2.0 * (4.6 - 1.0 / SIGMA))  # The rate an infectious is not recovers and moves into the resistant phase. Note that for the model it only means he does not infect anybody any more.

# Disease Response
HOSPITAL_ICU_TIME = 12 # Days in ICU
HOSPITAL_ICU_LOAD = 100 # Max Number of ICU beds before overloaded
SOCIAL_DISTANCE_THRESHOLD_POPULATION = 200 # Threshold for infected population for social distancing to take into effect
SOCIAL_DISTANCE_DAY = 57 # Day Social Distancing happened
