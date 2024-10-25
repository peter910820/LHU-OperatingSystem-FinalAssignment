import pandas

class CpuQueueCalculation(object):

    def __init__(self, process, start, memory_size):
        self.self.process = process
        self.self.start = start
        self.self.memory_size = memory_size
        self.result = []
        self.output = {}

    def first_configuration(self):
        name = []
        n = 0
        self.output['記憶體區塊大小'] = self.process
        for p in self.process:
            for m in self.memory_size:
                if int(m) >= int(p):
                    self.result.append(self.start[self.memory_size.index(m)])
                    self.start[self.memory_size.index(m)] = str(int(self.start[self.memory_size.index(m)]) + int(p))
                    self.memory_size[self.memory_size.index(m)] = str(int(self.memory_size[self.memory_size.index(m)]) - int(p))
                    n += 1
                    name.append(f'J{n}')
                    break
                if self.memory_size.index(m) == len(self.memory_size)-1:
                    self.result.append('無')
                    n += 1
                    name.append(f'J{n}')

        self.output['記憶體位置'] = self.result
        self.output['工作編號'] = name
        self.output = pandas.DataFrame(data=self.output)
        self.output.to_excel('t.xlsx')

        pandas.read_excel("t.xlsx", index_col=0, engine='openpyxl')
        print('匯出完成')

    def optimal_configuration(self):
        tmp = []
        self.output['記憶體區塊大小'] = self.process
        for p in self.process:
            for m in self.memory_size:
                tmp.append(int(m)-int(p))
            
            print(tmp)
            p_tmp = tmp
            p_tmp.sort()
            print(p_tmp, tmp)
            for t in p_tmp:
                if t >= 0:
                    self.result.append(self.start[tmp.index(str(t))])
                    self.start[tmp.index(str(t))] = str(int(self.start[tmp.index(str(t))]) + int(p))
                    self.memory_size[tmp.index(str(t))] = str(int(self.memory_size[tmp.index(str(t))]) - int(p))
                    break
                if p_tmp.index(t) == len(p_tmp)-1:
                    self.result.append('無')
            p_tmp.clear()
            tmp.clear()
        print(self.result)

process = str(input("請按照順序輸入記憶體需求大小(不用加單位，之間用空白隔開): ")).split(" ")
start = str(input("請按照順序輸入開始位置(不用加單位，之間用空白隔開): ")).split(" ")
memory_size = str(input("請按照順序輸入記憶體區塊大小(不用加單位，之間用空白隔開): ")).split(" ")

f = CpuQueueCalculation(process, start, memory_size)
f.first_configuration()