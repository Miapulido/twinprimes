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

def count_primes(nums, start, end):
    
    count = 0
    if end > len(nums):
        raise "out of range"
        
    for i in range(start,end):
        if nums[i] != 0:
            count = count + 1
    return count

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

def is_prime(p):
    return p != 0

# identify all primes below this number
below = 10000000
primes = eras_sieve(below)
print len(primes)
# count them
print 'num primes 1', sum(map(is_prime,primes))
print 'num primes 2', count_primes(primes, 0, len(primes))
print 'num primes 3', count_primes_2(primes[0:len(primes)])
print 'num twin primes ', count_twin_primes(primes[0:len(primes)])

# count them in chilliads
chilliad = 1000

# method 1 (more verbose, better for debugging)
# for i in range(0,below,chilliad):
#    print 'range, ', i, i+chilliad
#    num = count_primes_2(primes[i:i+chilliad])
#    print 'chilliad: ', i, 'num_primes:', num

# for i in range(0,below,chilliad):
#     print 'range, ', i, i+chilliad
#     num = count_twin_primes(primes[i:i+chilliad])
#     print 'chilliad: ', i, 'num_primes:', num


# method 2
num_primes = [count_primes_2(primes[i:i+chilliad]) for i in range(0,below,chilliad)]
#print num_primes
num_twin_primes = [count_twin_primes(primes[i:i+chilliad]) for i in range(0,below,chilliad)]
#print num_twin_primes


# count number of primes across segments that increase exponentially,
base = 10
num_steps = int(round(math.log(below,base)))+1

print 'primes: '
num_primes_aggr = [count_primes_2(primes[:base**i]) for i in range(1,num_steps)]
print num_primes_aggr

# compute ratio between number of primes and segment size
def ratio(pair):
    return pair[0] / float(pair[1])

belows = [base**i for i in range(1,num_steps)]
ratios = map(lambda pair: ratio(pair), zip(num_primes_aggr,belows))
print ratios

# compute inverse of logarithm
logs = [1 / round(math.log(i),2) for i in belows]
print logs

# same thing for twin primes:
# - number of primes in segments with exponentially increasing size
# - ration between number of twin primes and segment size
# - compare ratio with inverse of log
print 'twin primes: '
num_twin_primes_aggr = [count_twin_primes(primes[:base**i]) for i in range(1,num_steps)]
print num_twin_primes_aggr
twin_ratios = map(lambda pair: ratio(pair), zip(num_twin_primes_aggr,belows))
print twin_ratios

twin_base = 1.1
twin_logs = [1 / round(math.log(i,twin_base),2) for i in belows]
print twin_logs

