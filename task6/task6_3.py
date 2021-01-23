# task6_3
# Create 2 collections storing company employees, get number of employees working in both companies,
# get collection of employees with some name from both of groups, input several names
# and find if they work in one of companies, print results
company_1 = {'Levon', 'Atom', 'Njdeh', 'Martin', 'Abel', 'Robert', 'Arina', 'Sevak', 'Hrayr', 'Hayk', 'Anahit'}
company_2 = {'Armen', 'Armine', 'Martin', 'Abel', 'Karen', 'Arina', 'Sevak', 'Hrachya', 'Haykuhi', 'Anahit'}
print('number of employees working in both companies is ', len(company_1) + len(company_2), '\n')
col_1 = company_1 & company_2
print('collection of employees with some name from both of groups', col_1, '\n')
col_2 = company_1 | company_2
col_3 = company_1 - company_2
col_4 = company_2 - company_1
n = 0
while n < 12:
    name = input('input names \n')
    if name in col_2:
        print(name, 'kampanianeric mekum ashxatum e')
    else:
        print(name, 'voch mi company-um el chka')
    if name in col_1:
        print(name, 'erkusi mej el ka')
    if name in col_3:
        print(name, "ashxatum e 1-in company-um")
    if name in col_4:
        print(name, 'Ashxatum e erkrord company-um')

    n += 1
