# To-do:
#   1. Write unit tests
#   2. I/O

# algorithm:
# 1. pick one of the datacenters with most ids and call it master
# 2. sync it with all of the others
# 3. sync the rest of the datacenters with the master

def sync(data_centers):
    master = []
    master_id = 0
    for (index,center) in enumerate(data_centers):
        if len(center) > len(master):
            master = center
            master_id = index

    for (index,center) in enumerate(data_centers):
        diff = center - master
        for item in diff:
            print str(item) + ' ' + str(index+1) + ' '+ str(master_id+1)
            master.add(item)


    for (index,center) in enumerate(data_centers):
        diff = master - center
        for item in diff:
            print str(item) + ' ' + str(master_id+1) + ' '+ str(index+1)
            center.add(item)

    print 'done'

if __name__ == '__main__':
    # lines = [
    #     '1 3 4',
    #     '1 2 3',
    #     '1 3',
    #     '1 4 2'
    # ]
    # lines = [
    #     '1 2',
    #     '2 1'
    # ]

    lines = [
        '1 3 4 5 7',
        '1 3',
        '2',
        ''
    ]
    data_centers = []
    for line in lines:
        if not line.strip():
            data_center = set()
        else:
            data_center = set(line.split(' '))
        data_centers.append(data_center)

    sync(data_centers)
