Disclaimer
=======
This SEIRD model is put together for a school project and for general interest. If you want an accurate model that models out COVID-19 and other pandemics for reasons other than general interest, please seek elsewhere. As of April 2020, this project is considered complete and archived.

SEIRD Model
=======

Stages
-----------
![Susceptible -> Exposed -> Infectious -> Dead/Recovered][https://github.com/cjinn/seirdp-model/blob/master/SEIRD.png]

This dynamic, heuristic, epidermic model consist of six stages:
1. Susceptible - Population that is susceptible to a disease
2. Exposed - Population that is exposed to the disease but do not show symptoms yet
3. Infectious - Population that is infectious and spreads the disease to others
4. Recovered - Population that has recovered and can no longer spread the disease
5. Dead - Population dead by the disease

This model consist of ordinary, differential equations that attempt to model any epidermic (such as COVID-19). The many parameters included in here are to help make different inferences on what parameters are important to a pandemic response.

Assumptions
-----------
* Population is a closed population (but it may grow or decline)
* Population is not immune to the disease; given the chance, everyone will become infectious and may die
* Many variables are reduced down into simple, numeric constant rates. Many do not change with time
* Model is heuristic and deterministic (no randomness)
* People who show symptoms and people are asymptomic but are still infectious are lumped together into 'Infectious' stage
* Population in 'Recovered' stage do not become susceptible to the disease
* There is no natural or induced immunity
* People who die stay dead and are no longer infectious

Routes
-----------
There are two main routes for everyone in the susceptible population to take:
* Susceptible -> Exposed -> Infectious -> Recovered
* Susceptible -> Exposed -> Infectious -> Dead

Running my Code
=======

Installation
-----------
1. Install Python3
2. Run the command `pip3 install -r requirements.txt`

Demo (Python Backend)
-----------
1. Run the command `python3 seird.py`

Demo (GUI)
-----------
1. Run the command `python3 userinterface.py`
2. Enter parameters as you see fit
3. Click 'Ok' and a plot should appear

Note that this demo runs off `covid_params.py`. These numbers are hypothetical numbers.

Parameters
-----------
There are many parameters when modelling a disease. This model attempts to account for many different scenarios. See `covid_params.py` to get a good feeling of what parameters are used.

Here is the list of parameters that you should change:
* `r0` - Basic Reproductive Number of the disease (unrestrictive)
* `rc` - Basic Reproductive Number of the disease when social distancing is implemented
* `gamma` - The rate an infectious person recovers and moves into the recovered phase. Note that this means they do not infect anybody any more.
* `sigma` - The rate at which an exposed person becomes infectious. This is defined as 1/(incubationPeriod)
* `baseAlpha` - Probability that the disease will kill a person
* `rho` - Rate at which people die (1/6 = 6 days to kill a person)
* `socDistResponseFactor` - Population's receptiveness to social distancing. Range at [0, 1]. Defaults at 1.0. The higher this number is, the likelihood the population responds positively to the countermeasures. 
* `diseaseScalingFactor` - How more deadly the disease is the greater the population of the infectious. Range at [0, 1]. Defaults at 0.0. The more overworked the system is, the higher this number gets.
* `population` - Population number. Note that population system is closed.
* `E0` - Initial seed amount of people infected with the disease.
* `thrDay` - Day that triggers social distancing. Set this higher than daysModel to never trigger it.
* `daysModel` - Number of days to simulate the model. 150 days provides good resolution for the figure.

References
=======
* https://towardsdatascience.com/infectious-disease-modelling-beyond-the-basic-sir-model-216369c584c4
* https://github.com/coronafighter/coronaSEIR/blob/master/main_coronaSEIR.py
