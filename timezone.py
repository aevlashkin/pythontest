def list_time():
    print('введите часы')
    first_hour = int(input())
    counter = 0
    while True:
        current_hour = first_hour + counter
        current_hour-= (24 if current_hour > 24 else 0)
        yield next_time(current_hour, 0, 'IRK (UTC +8)')
        yield next_time(current_hour, 5, 'MSK (UTC +3)')
        yield next_time(current_hour, 11, 'NUU (UTC -3)')
        counter+=1

def next_time(hour, delta, town):
    result = hour + (0 if hour >= delta else 24) - delta
    
    add_zero = ' ' if result > 9 else ' 0'
    
    return (town + add_zero + str(result) + ':00;')

time = list_time()
for i in range(24):
    print(next(time), next(time), next(time), sep=' ')
