#20161795 고가해(顧家楷)
import cvxpy as cp

x1 = cp.Variable()
x2 = cp.Variable()

constraints = [2 * x1 + x2 <= 4,
               3 * x1 + 4 * x2 <= 12,
               x1 >= 0,
               x2 >= 0]

prob = cp.Problem(cp.Maximize(x1 + x2), constraints)
prob.solve()

print("status:", prob.status)
print("optimal value", prob.value)
print("optimal var", x1.value, x2.value)
