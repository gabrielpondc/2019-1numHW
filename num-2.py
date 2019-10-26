#20161795 고가해(顧家楷）
import cvxpy as cp
import numpy as np

# Generate data.
np.random.seed(1)
A = np.random.randn(10, 20)
b = np.random.randn(10)
x = cp.Variable(20)
constraints = [x >= 0]
# Define and solve the CVXPY problem.
cost = cp.sum_squares(A*x + b)
prob = cp.Problem(cp.Minimize(cost), constraints)
prob.solve()
# Print result.
print("\nThe optimal value is", prob.value)
print("The optimal x is")
print(x.value)
print("The norm of the residual is ", cp.norm(A*x + b, p=2).value)
