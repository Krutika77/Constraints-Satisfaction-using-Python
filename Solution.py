import constraint

problem = constraint.Problem()

name = ["Beany", "Cheetah", "Thor", "Suzie"]
breed = ["Boxer", "Collie", "Shepherd", "Terrier"]
best = ["Plank", "Poles", "Tire", "Tunnel"]
ranking = ["1", "2", "3", "4"]

variables = name + breed + best + ranking

problem.addVariables(variables, [1,2,3,4])

problem.addConstraint(constraint.AllDifferentConstraint(), name)
problem.addConstraint(constraint.AllDifferentConstraint(), breed)
problem.addConstraint(constraint.AllDifferentConstraint(), best)
problem.addConstraint(constraint.AllDifferentConstraint(), ranking)

# 1. Only the winning dog has the same initial letter in name and breed.
problem.addConstraint(lambda a, b : a == b, ("Cheetah", "Collie")) # Cheetah is a Collie
problem.addConstraint(lambda a, b : a != b, ("Beany", "Boxer")) # Beany is not a Boxer
problem.addConstraint(lambda a, b : a != b, ("Thor", "Terrier")) # Thor is not a Terrier
problem.addConstraint(lambda a, b : a != b, ("Suzie", "Shepherd")) # Suzie is not a Shepherd

# 3. Between Cheetah and the dog who loves the poles, one was 1st and the other 3rd
problem.addConstraint(lambda a, b : a == b, ("Poles", "3")) # The dog who loves poles came third
problem.addConstraint(lambda a, b : a == b, ("Cheetah", "1")) # Cheetah came 1st

# 5. Cheetah either loves the tunnel or she came 4th.
problem.addConstraint(lambda a, b : a == b, ("Cheetah", "Tunnel")) # Since Cheetah came 1st, he must love the tunnel

 # 2. The Boxer ranked 1 position after the Shepherd.
problem.addConstraint(lambda a, b : b-a == 1, ("Shepherd", "Boxer"))
problem.addConstraint(lambda a, b : a != b, ("Boxer", "1")) # Boxer cannot be 1st
problem.addConstraint(lambda a, b : a != b, ("Shepherd", "4")) # Shepherd cannot be 4th

# 2. Shepherd doesn't like Tunnel and Tire
problem.addConstraint(lambda a, b : a != b, ("Shepherd", "Tunnel")) 
problem.addConstraint(lambda a, b : a != b, ("Shepherd", "Tire"))

# 2. Boxer doesn't like Tunnel and Tire
problem.addConstraint(lambda a, b : a != b, ("Boxer", "Tunnel"))
problem.addConstraint(lambda a, b : a != b, ("Boxer", "Tire"))

# 4. Thor doesn't like the plank and didn't come 2nd.
problem.addConstraint(lambda a, b : a != b, ("Thor", "Plank"))
problem.addConstraint(lambda a, b : a != b, ("Thor", "2"))

# 6. The dog who loves the plank came 1 position after the dog who loves the poles.
problem.addConstraint(lambda a, b : b-a == 1, ("Poles", "Plank"))
problem.addConstraint(lambda a, b : a != b, ("Plank", "1")) # The dog who loves plank cannot be 1st
problem.addConstraint(lambda a, b : a != b, ("Poles", "4")) # The dog who loves poles cannot be 4th

solution = problem.getSolutions()[0]

for i in range(1,5):
    for s in solution:
        if solution[s] == i:
            print(s)
    print("\n")