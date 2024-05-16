from master_mind_solver import MasterMindSolver


secret_key = [1,1,0,1,0,0,1,1]

m = MasterMindSolver(secret_key)

prediction = m.predict_secret()

print(prediction)








