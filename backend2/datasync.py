# algorithm:
# 1. pick one of the datacenters with most ids and call it master
# 2. sync it with all of the others
# 3. sync the rest of the datacenters with the master

class CommandLineInterface(object):
    def read_input(self):
        lines = []
        n = int(raw_input())
        for i in range(n):
            line = raw_input()
            lines.append(line)
        return lines

    def get_datacenters_from_input(self, lines):
        data_centers = []

        for line in lines:
            if not line.strip():
                data_center = set()
            else:
                data_center = set(line.split(' '))

            data_centers.append(data_center)

        return data_centers

class DataSync(object):

    def sync(self, data_centers):
        result = ""
        master = []
        master_id = 0
        for (index,center) in enumerate(data_centers):
            if len(center) > len(master):
                master = center
                master_id = index

        for (index,center) in enumerate(data_centers):
            diff = center - master
            for item in diff:
                result += str(item) + ' ' + str(index + 1) + ' ' + str(master_id + 1) + '\n'
                master.add(item)

        for (index,center) in enumerate(data_centers):
            diff = master - center
            for item in diff:
                result += str(item) + ' ' + str(master_id + 1) + ' ' + str(index + 1) + '\n'

                center.add(item)

        result += 'done'
        return result



if __name__ == '__main__':
    cli = CommandLineInterface()
    datasync = DataSync()

    lines = cli.read_input()
    datacenters = cli.get_datacenters_from_input(lines)
    print datasync.sync(datacenters)
