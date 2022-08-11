str = "no climate change"

new_str = ''
for char in str :
    if char not in ('no'):
       new_str += char

print('orig: ', str)
print('new: ', new_str)