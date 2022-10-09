x = int(input())
y = str(x).count('0')
print(y)
count = 0
for i in str(x):
    if i == 0:
        count += 1

print(count)



x2 = int(input())
count2 = 0
for i2 in str(x2)[::-1]:
    if i2 == '0':
        count2 += 1
    else:
        break

print(count2)



my_list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list_2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
my_result = my_list_1[::2] + my_list_2[1::2]
print(my_result)



my_listt = [1, 2, 3, 4]
new_listt = my_listt[1:] + [my_listt[0]]
print(new_listt)



my_listt1 = [1, 2, 3, 4]
list_value = my_listt1.pop(0)
my_listt1.append(list_value)
print(my_listt1)



my_string = "43 больше чем 34 но меньше чем 56"
my_str_list = my_string.split()
counter = 0

for item in my_str_list:
    if item.isdigit():
        counter += int(item)

print(counter)



my_str = "My long string"
l_limit, r_limit = "o", "g"
l_index = my_str.find(l_limit) + 1
r_index = my_str.rfind(r_limit)
sub_str = my_str[l_index: r_index]

sub_str = my_str[my_str.find(l_limit) + 1: my_str.rfind(r_limit)]

print(sub_str)



from textwrap import wrap

s = 'asnafjnafjnsad'
print(wrap(s if len(s) % 2 == 0 else s + '_', 2))



a_list = [2, 4, 1, 5, 3, 9, 0, 7]
count = 0
for e in range(1, len(a_list) - 2):
    if a_list[e - 1] < a_list[e] and a_list[e] > a_list[e + 1]:
        count += 1

print(count)



my_str = 'qqweqeasd'
lst = []
[lst.append(i) for i in my_str if my_str.count(i) == 1]
print(lst)



str1_ = "hi brother"
str2_ = "hi sister"
lisst = []
lisst = str1_ + str2_
print(list(set(str1_ + str2_)))