import pulp

# Create a model
model = pulp.LpProblem('Maximize_Production', pulp.LpMaximize)

lemonade = pulp.LpVariable('Lemonade', lowBound = 0, cat = 'Integer')
fruit_juice = pulp.LpVariable('Fruit_juise', lowBound = 0, cat = 'Integer')

# Objective function:
model += lemonade + fruit_juice, 'Total_Production'

# Resourse limitation 
model += 2 * lemonade + 1 *fruit_juice <= 100, 'Water_limit'
model += 1 * lemonade <= 50, 'Sugar_limit'
model += 1 * lemonade <= 30, 'Lemon_juise_limit'
model += 2 * fruit_juice <= 40, 'Fruit_puree_limit'

# Solution for the model
model.solve()

# Testing 
print(f'Статус роз\'язку задачі: {pulp.LpStatus[model.status]}')
print(f'Кількість лимонаду на виробництві: {lemonade.varValue}')
print(f'Кількість фруктового соку на виробництві: {fruit_juice.varValue}')
print(f'Максимальна продуктивність: {pulp.value(model.objective)}')