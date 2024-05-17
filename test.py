import random

from master_mind_solver import MasterMindSolver

secret_key = [1,0,1,1,1]

m = MasterMindSolver(secret_key=secret_key) #note here the secret key will not be used for guessing it will be used for grading and giving score to the guess

prediction = m.predict_secret()

print(f"the secret key is: {secret_key}")
print(f"the solver's prediction is: {prediction}")
