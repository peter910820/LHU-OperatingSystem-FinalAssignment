q = 0
information = []

def FCFS(information):
    charta = ''
    chartb = ''
    timer = 0
    waitTime = 0
    responseTime = 0
    for x in information:
        charta += f'|   {(x[0])}   '
        chartb += str(timer)
        waitTime += timer - int(x[2])
        responseTime += int(x[1]) 
        chartb = typesetting(chartb,timer)
        timer += int(x[1])
    charta +=  '|'  
    chartb +=  str(timer)    
    print(charta)
    print(chartb)  
    print(f'平均回覆時間為: {(waitTime+responseTime)/5}')
    print(f'平均等待時間為: {waitTime/5}')
    return information

def SJF(information):
    charta = ''
    chartb = ''
    timer = 0
    waitTime = responseTime = 0
    tmp = []
    tmp2 = information
    n = p = z = 0
    for i in information:
        z += int(i[1])
    while p == 0:
        if timer >= z:
            p = 1
            break
        if n == 1:
            charta += f'|   {(tmp[0][0])}   '
            waitTime += timer - int(tmp[0][2])
            responseTime += int(tmp[0][1]) 
            chartb += str(timer)
            chartb = typesetting(chartb,timer)
            timer += int(tmp[0][1])
            tmp.clear()
        else:    
            charta += f'|   {information[0][0]}   '
            responseTime += int(information[0][1]) 
            chartb += str(timer)
            chartb = typesetting(chartb,timer)
            timer += int(information[0][1])
        for k in information:
            if k[0] in charta:
                tmp2.remove(k)
        for i in tmp2:
            if int(i[2])<=timer:
                tmp.append(i)
        tmp.sort(key=lambda s: int(s[1]))
        n = 1
    charta +=  '|'  
    chartb +=  str(timer) 
    print(charta)
    print(chartb) 
    print(f'平均回覆時間為: {(waitTime+responseTime)/5}')
    print(f'平均等待時間為: {waitTime/5}')
    return information

def SRT(information):
    charta = ''
    chartb = ''
    timer2 = 0
    responseTime = cpuTime = 0
    processNow = information[0]
    tmp = []
    noPreempt = 0
    noReduce = 0
    for cpu in information:
        cpuTime += int(cpu[1])
    for timer in range(0,cpuTime):
        #print(processNow,timer,timer2,tmp,sep=',')
        if timer == cpuTime:
            break
        if int(processNow[1]) == timer2:
            timer2 = 0
            tmp.remove(processNow)
            responseTime += timer - int(processNow[2])
            noReduce = 1
        if noReduce == 0:
            for newIn in information:
                if int(newIn[2]) == timer:
                    if tmp:
                        tmp.append(newIn)
                        index = information.index(processNow)
                        information[index][1] = str(int(information[index][1]) - timer2)
                        processNow = information[index]
                        timer2 = 0
                        if int(information[index][1]) == 0:
                            responseTime += timer - int(information[index][2])
                            tmp.remove(information[index])
                            print(information[2])


                        tmp.sort(key = lambda s: int(s[1])) #sort
                        if len(tmp) > 1:
                            if newIn[0] == tmp[1][0]:
                                if int(newIn[1]) < int(tmp[0][1]): #Preempt
                                    noPreempt = 1 #jump out to reset the noPreempt key
                                    charta += f'|   {(newIn[0])}   '
                                    chartb += str(timer)
                                    chartb = typesetting(chartb,timer)
                                    processNow = newIn
                            else:
                                if int(newIn[1]) < int(tmp[1][1]): #Preempt
                                    noPreempt = 1 #jump out to reset the noPreempt key
                                    charta += f'|   {(newIn[0])}   '
                                    chartb += str(timer)
                                    chartb = typesetting(chartb,timer)
                                    processNow = newIn
                        else:
                            if int(newIn[1]) < int(tmp[0][1]): #Preempt
                                noPreempt = 1 #jump out to reset the noPreempt key
                                charta += f'|   {(newIn[0])}   '
                                chartb += str(timer)
                                chartb = typesetting(chartb,timer)
                                processNow = newIn

                        if noPreempt == 0:
                            charta += f'|   {(processNow[0])}   '
                            chartb += str(timer)
                            chartb = typesetting(chartb,timer)
                        elif noPreempt == 1:
                            noPreempt = 0
                    else:
                        charta += f'|   {(newIn[0])}   '
                        chartb += str(timer)
                        chartb = typesetting(chartb,timer)
                        processNow = newIn
                        tmp.append(newIn)

        else: 
            for newIn in information:
                if int(newIn[2]) == timer:
                    tmp.append(newIn)
                    tmp.sort(key = lambda s: int(s[1])) #sort
            processNow = tmp[0]
            charta += f'|   {(processNow[0])}   '
            chartb += str(timer)
            chartb = typesetting(chartb,timer)
            noReduce = 0

        timer2 += 1
        

    charta +=  '|' 
    chartb +=  str(timer+1) 
    if tmp:
        responseTime += timer + 1 - int(tmp[0][2])
    print(charta)
    print(chartb)
    print(f'平均回覆時間為: {responseTime/5}')
    print(f'平均等待時間為: {(responseTime-cpuTime)/5}')
    return 0

def priority(information):
    cputime = 0
    charta = ''
    chartb = ''
    waitTime = responseTime = 0
    queue = []
    for i in information:
        cputime += int(i[1])
    for t in range(0,cputime):
        if queue:
            for a in information:
                if int(a[2]) == t:
                    queue.append(a)
                    # print(f'->{queue},{t}')
            if int(queue[0][1]) == 0:
                queue.remove(queue[0])
                queue.sort(key=lambda s: int(s[3]))
            if queue[0][0] not in charta:
                waitTime += t - int(queue[0][2])
                charta += f'|   {(queue[0][0])}   '
                chartb += str(t)
                chartb = typesetting(chartb,t)
        else:
            charta += f'|   {(information[0][0])}   '
            chartb += str(t)
            chartb = typesetting(chartb,t)
            queue.append(information[0])
        queue[0][1] = str(int(queue[0][1])-1)

    charta += f'|'
    chartb +=  str(t+1) 
    print(charta)
    print(chartb)
    print(f'平均回覆時間為: {(waitTime+cputime)/5}')
    print(f'平均等待時間為: {waitTime/5}')

def rr(information,sp):
    charta = ''
    chartb = ''
    k = 0
    cpuTime = 0
    turnaroundTime = 0
    timestamps = 0
    queue = []
    cpu = []
    for r in information:
        cpuTime += int(r[1])
        cpu.append([r[0],r[2]])
    for t in range(0,cpuTime):
        if queue:
            for i in information:
                if int(i[2]) == t:
                    queue.append(i)
            if int(queue[0][1]) == 0:
                for c in cpu:
                    if c[0] == queue[0][0]:
                        turnaroundTime += t - int(c[1])
                        cpu.remove(c)
                        break
                queue.remove(queue[0])
                timestamps = 0
                charta += f'|   {(queue[0][0])}   '
                chartb += str(t)
                chartb = typesetting(chartb,t)
                k = 1
            if timestamps == sp:
                tmp = queue[0]
                queue.remove(tmp)
                queue.append(tmp)
                timestamps = 0
                if k == 0:
                    charta += f'|   {(queue[0][0])}   '
                    chartb += str(t)
                    chartb = typesetting(chartb,t)
            k = 0
        
        else:
            queue.append(information[0])
            charta += f'|   {(queue[0][0])}   '
            chartb += str(t)
            chartb = typesetting(chartb,t)
        queue[0][1] = str(int(queue[0][1]) -1)
        timestamps += 1
    turnaroundTime += (t+1) - int(cpu[0][1])
    charta += '|'
    chartb += str(t+1)
    print(charta)
    print(chartb)
    print(f'平均回覆時間為: {(turnaroundTime)/5}')
    print(f'平均等待時間為: {(turnaroundTime-cpuTime)/5}')

def typesetting(chartb,timer):
    if timer>99:
        chartb +=  '     '
    elif timer>9:
        chartb +=  '      '
    else:
        chartb +=  '       '
    return chartb


mode = int(input(str('請選擇模式:(1:FCFS,2:SRT,3:優先權可搶,4:RR): ')))
while q == 0:
    if mode == 3:
        process = input(str('請輸入行程名稱,CPU週期,到達時間以及優先度(之間請用逗號分開，結束輸入請打q): '))
    else:
        process = input(str('請輸入行程名稱,CPU週期以及到達時間(之間請用逗號分開，結束輸入請打q): '))
    if process == 'q':
        if mode == 4:
            sp = int(input(str('請輸入時間切片: ')))
        q = 1
        break
    if mode == 3 or mode == 4:
        information.append(process.split(',',3))
        information.sort(key=lambda s: int(s[2]))
    else:
        information.append(process.split(',',2))
        information.sort(key=lambda s: int(s[2]))  #def s(e): return int(e[-1])

match mode:
    case 1:
        FCFS(information)
    case 2:
        SRT(information)
    case 3:
        priority(information)
    case 4:
        rr(information,sp)

