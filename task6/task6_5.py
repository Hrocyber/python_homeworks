# task6_5
# *Input a collection of employee names with their salary,
# calculate average salary in organisation, get the employee with highest salary,
# get the employee with lowest salary print results.
empl_salary = {'Hrayr': 1400, 'Armine': 745, 'Karen': 975, 'Milena': 820, 'Arman': 874, 'Ani': 640}
print('average salary in organisation is ')
print(sum(empl_salary.values()) / len(empl_salary), '$')
print('the employee with highest salary is ', max(empl_salary, key =empl_salary.get), max(empl_salary.values()))
print('he employee with lowest salary is', min(empl_salary.keys()), min(empl_salary.values()))
