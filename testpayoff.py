#mock a f-pair with predefined length.

import random


print("This simulates f-pairs, L2-L3.")

f_his = []

f = 178

perturbation_pos_f = random.sample(range(6, f), round(f * 0.05))
perturbation_pos_f = sorted(perturbation_pos_f)
print(perturbation_pos_f)

def calculate_strategy_f(memoryA, memoryB):
    t1 = [0,0,0]
    t2 = [0,0,0]
    for i in range(len(memoryA)):
        t1[i] = memoryB[i][0]
        t2[i] = memoryA[i][1]
    dis1 = [t2.count(2)/3, t2.count(3)/3, t2.count(4)/3]
    #print(dis1)
    dis2 = [t1.count(1)/3, t1.count(2)/3, t1.count(3)/3]
    #print(dis2)
    payoff1_A = 0.1 * dis1[0] + 0.1 * dis1[1] + 0.1 * dis1[2]
    payoff2_A = 1.2 * dis1[0] + 0.2 * dis1[1] + 0.2 * dis1[2]
    payoff3_A = 0 * dis1[0] + 1 * dis1[1] + 0 * dis1[2]
    if payoff1_A > payoff2_A and payoff1_A > payoff3_A:
        n = 1
    if payoff2_A >= payoff1_A and payoff2_A >= payoff3_A: #>= implements the tie-breaker
        n = 2
    if payoff3_A > payoff1_A and payoff3_A > payoff2_A:
        n = 3

    payoff2_B = 0 * dis2[0] + 1 * dis2[1] + 0 * dis2[2]
    payoff3_B = 0.2 * dis2[0] + 0.2 * dis2[1] + 1.2 * dis2[2]
    payoff4_B = 0.1 * dis2[0] + 0.1 * dis2[1] + 0.1 * dis2[2]
    if payoff2_B > payoff3_B and payoff2_B > payoff4_B:
        m = 2
    if payoff3_B >= payoff2_B and payoff3_B >= payoff4_B:
        m = 3
    if payoff4_B > payoff2_B and payoff4_B > payoff3_B:
        m = 4

    return [n,m]

# testing a little bit
#memoryA = [[1, 2], [1, 2], [1, 3]]
#memoryB = [[1, 4], [1, 4], [1, 4]]

#print(calculate_strategy_f(memoryA, memoryB))

def random_pick_f():
    n = random.randint(1,3)
    m = random.randint(2,4)
    return [n,m]

f_his = []

temp = [[0 for col in range(2)] for row in range(5)]

for i in range(5):
    temp[i][0] = random.randint(1, 3)
    temp[i][1] = random.randint(2, 4)

for item in temp:
    f_his.append(item)

#print(b_his)

memoryA = []
memoryB = []

#form history iteratively
for i in range(5, 178):
    memoryA = random.sample(f_his,3)
    memoryB = random.sample(f_his,3)
    if i not in perturbation_pos_f:
        k = calculate_strategy_f(memoryA, memoryB)
        f_his.append(k)
    else:
        k = random_pick_f()
        f_his.append(k)

if len(f_his)!= 178:
    print('ERROR')
else:
    print(f_his)
