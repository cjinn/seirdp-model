SEIRDP Model
=======

Stages
-----------
This dynamic, heuristic, epidermic model consist of six stages:
1. Susceptible - Population that is susceptible to a disease
2. Exposed - Population that is exposed to the disease but do not show symptoms yet
3. Infectious - Population that is infectious and spreads the disease to others
4. Recovered - Population that has recovered and can no longer spread the disease
5. Dead - Population dead by the disease
6. Passed away - Population that died from causes not related to the disease

Variables for Object SEIRDP
-----------
* r0 - Basic Reproduction Number (Before countermeasures are in place)
* r1 - Basic Reproduction Number (After countermeasures are in place)
* gamma - The rate an infectious is not recovers and moves into the resistant phase. Note that for the model it only means he does not infect anybody any more.
* sigma - The rate at which an exposed person becomes infectious
* optimalKillRate - Rate of killing an infectious person
* fatalityRateAvg - Average fatality rate of the disease
* birthRateDaily - Birth Rate per day. Set this to 0 if you don't want your model to use it
* natDeathRateDaily - "Natural" Death Rate per day. Set this to 0 if you don't want your model to use it
* socDistResponseFactor - Population's response to countermeasures. Defaults at 1.0. Higher values gives weird results
* diseaseScalingFactor - How more deadly the disease is the greater the population of the infectious. Defaults at 0. Set this at 1 or higher to really try and kill everyone.


Variables for method solve()
-----------
* population - Population number. Note that population is closed.
* E0 - Initial amount of people infected with the disease.
* thrPop - Threshold of Infected, Dead and Recovered population to trigger countermeasures (social distancing, quarantine, etc). Set this very high to never trigger it.
* thrDay - Day that trigger countermeasures (social distancing, quarantine, etc) unless thrPop triggers it first. Set this higher than daysModel to never trigger it.
* daysModel - Number of days to simulate the model. 100 days provides good resolution for the figure.

Installation
=======
1. Install Python3
2. Run the command `pip3 install requirements.txt`

Demo
-----------
1. Run the command `python3 seirdp.py`

References
=======
* https://github.com/coronafighter/coronaSEIR/blob/master/main_coronaSEIR.py
* https://towardsdatascience.com/infectious-disease-modelling-beyond-the-basic-sir-model-216369c584c4
* https://www.idmod.org/docs/hiv/model-seir.html
