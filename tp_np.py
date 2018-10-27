import math
import numpy as np

def eras_sieve(end):

    nums = [i for i in range(end)]  
    # ignore 0 and 1, but need to be present 
    # to count properly
    nums[0] = 0
    nums[1] = 0

    # only need to check primes up to sqrt(end)
    for i in range(int(math.ceil(math.sqrt(len(nums))))):

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
            continue
            #count = count + 1

        if nums[i] != 0 and nums[i-2] != 0:
            #print 'prime ', nums[i]
            count = count + 1
    return count

def gauss_approx(segments, base=math.e, exponent=1.0):

    # compute N/logN for each segment of size N
    return [i / round(math.log(i, base)**exponent,2) for i in segments]

def gauss_approx_np(segments, base=math.e, exponent=1.0):
    pass

def li_approx(segments, N, base=math.e, exponent=1.0, constant=1.0):

    # compute 1/logN for each integer in [2,N] 
    li_logs = [1 / round(math.log(i, base)**exponent,2) for i in range(2,N)]

    # approximate integral as a sum of all values up to N
    return [constant*sum(li_logs[:i]) for i in segments]

def li_approx_np(segments, N, base=math.e, exponent=1.0, constant=1.0):

    # compute 1/logN for each integer in [2,N] 
    # (base change explicitly computed because numpy only supports natural logarithm)
    li_logs = 1./np.around((np.log(np.arange(2,N))/np.log(base))**exponent, decimals=2)

    # approximate integral as a sum of all values up to N
    return [constant*np.sum(li_logs[:i]) for i in segments]    

# identify all primes below N
N = 10000000
primes = eras_sieve(N)
print len(primes)

# determine number of segments that grow exponentially up to N
base = 10
num_segments = int(round(math.log(N,base)))+1
segments = [base**i for i in range(1,num_segments)]

# count # of primes up to N
print 'pi(N)'
num_primes_aggr = [count_primes_2(primes[:i]) for i in segments]
print num_primes_aggr

# compute N/logN
print 'N/logN'
pnt = gauss_approx(segments)
print pnt

# compute Li(N)
print 'Li(N)'
li_logs_aggr = li_approx_np(segments, N)
print li_logs_aggr

# compute Li(N) by parts
print 'Li(N) parts'
# N/logN + 1!N/(logN)^2 + 2!N/(logN)^3 + ... + (m-1)!N/(logN)^m
pnt2 = [i / round(math.log(i),2) + i / round(math.log(i),2)**2 + 2*i / round(math.log(i),2)**3 for i in segments]
print pnt2

# Twin primes
print '####twin primes: ####'

print 'tp_pi(N)'
num_twin_primes_aggr = [count_twin_primes(primes[:i]) for i in segments]
print num_twin_primes_aggr

# N/logN
print '----tp_N/logN---'

# use log base that enables a faster descent than natural logarithm
print 'variable log base'
bases = [2, 1.1]
for twin_base in bases:
    twin_pnt = gauss_approx(segments, base=twin_base)
    print 'base: ', twin_base, twin_pnt

# use a power of log, as opposed to just log
print 'power of log'
exponents = [2, 1.9]
for twin_exponent in exponents:
    twin_pnt = gauss_approx(segments, exponent=twin_exponent)
    print 'exponent: ', twin_exponent, twin_pnt

print '---tp_Li(N)---'

print 'variable log base'
bases = [2, 1.1]
for twin_base in bases:

    li_logs_aggr = li_approx_np(segments, N, base=twin_base)
    print 'base: ', twin_base, li_logs_aggr

print 'power of log'

exponents = [2, 1.9, 1.85]
for twin_exponent in exponents:

    li_logs_aggr = li_approx_np(segments, N, exponent=twin_exponent)
    print 'exponent: ', twin_exponent, li_logs_aggr


print '---twin prime conjecture---'
c2 = 0.6601618
li_logs_aggr = li_approx_np(segments, N, exponent=2, constant=2*c2)
print 'twin prime conjecture: ', li_logs_aggr






