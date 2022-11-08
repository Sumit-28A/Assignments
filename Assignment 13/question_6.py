first_list = ["java","python","sql"]
second_list = ["c","cpp","nosql"]
third_list = ["javascript","php","html"]

for i in third_list:
    first_list.append(i)
    second_list.append(i)
print(first_list,second_list)