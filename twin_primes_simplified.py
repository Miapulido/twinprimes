import math
import matplotlib.pyplot as plt

def eras_sieve(end):

    nums = [i for i in range(end)]  
    # ignore 0 and 1, but need to be present 
    # to count properly
    nums[0] = 0
    nums[1] = 0

    for i in range(len(nums)):

        # skip non-primes
        if nums[i] == 0:
            continue

        # current prime
        p = nums[i]

        for j in range(i+p, len(nums), p):

            #print i, p, nums[j]

            # skip non-primes
            if nums[j] == 0:
                continue

            # check if nums[j] has p as factor
            if nums[j] % p == 0:
                nums[j] = 0 

    return nums

def count_primes_2(nums):
    
    count = 0
        
    for i in range(len(nums)):
        #print 'num ', nums[i]
        if nums[i] != 0:
            #print 'prime ', nums[i]
            count = count + 1
    return count


def count_twin_primes(nums):
    
    count = 0
        
    for i in range(2, len(nums)):
        #print 'num ', nums[i]
        
        # handle special cases
        if nums[i] == 2 or nums[i] == 3:
            count = count + 1

        if nums[i] != 0 and nums[i-2] != 0:
            #print 'prime ', nums[i]
            count = count + 1
    return count

def ratio(pair):
    return pair[0] / float(pair[1])

def prod(pair):
    return pair[0] * float(pair[1])

# identify all primes below this number
below = 10000000
primes = eras_sieve(below)
print len(primes)

# count them
print 'num primes ', count_primes_2(primes[0:len(primes)])
print 'num twin primes ', count_twin_primes(primes[0:len(primes)])

# count number of primes across segments that increase exponentially
base = 10
num_steps = int(round(math.log(below,base)))+1

# Primes
print 'pi(N)'
# count # of primes up to N
num_primes_aggr = [count_primes_2(primes[:base**i]) for i in range(1,num_steps)]
print num_primes_aggr

print 'N/logN'
# N
belows = [base**i for i in range(1,num_steps)]
# 1/logN
logs = [1 / round(math.log(i),2) for i in belows]
# compute pnt
pnt = map(lambda pair: prod(pair), zip(belows,logs))
print pnt

print 'Li(N)'
# compute 1/logN for each integer [2,N] 
li_logs = [1 / round(math.log(i),2) for i in range(2,below)]
# approximate integral as a sum of all values up to N
li_logs_aggr = [sum(li_logs[:base**i]) for i in range(1,num_steps)]
print li_logs_aggr

# Twin primes
print 'twin primes: '

print 'tp_pi(N)'
num_twin_primes_aggr = [count_twin_primes(primes[:base**i]) for i in range(1,num_steps)]
print num_twin_primes_aggr

print 'tp_N/logN'
# use a base that enables a faster descent than natural logarithm
twin_base = 2.71828 #1.05
exponent = 1.9
# 1/logN
twin_logs = [1 / round(math.log(i, twin_base)**exponent,2) for i in belows]
# apply pnt for primes to twin primes
twin_pnt = map(lambda pair: prod(pair), zip(belows,twin_logs))
print twin_pnt

print 'tp_Li(N)'
# compute 1/logN for each integer [2,N] 
li_logs = [1 / round(math.log(i, twin_base)**exponent,2) for i in range(2,below)]
#li_logs = [1 / float(i) for i in range(1,below)]
#li_logs = [math.exp(-i) for i in range(below)]
# approximate integral as a sum of all values up to N
li_logs_aggr = [sum(li_logs[:base**i]) for i in range(1,num_steps)]
print li_logs_aggr





