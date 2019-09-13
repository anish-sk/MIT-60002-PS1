
###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time
import copy

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    # TODO: Your code here
    cow_weights={}
    f=open(filename,'r')
    for line in f:
        name,weight=line.split(',')
        weight=weight.rstrip()        
        cow_weights[name]=int(weight)
    f.close()
    return cow_weights

# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here\
    cows_copy={}
    for keys in cows:
        cows_copy[keys]=cows[keys]
    trips=[]    
    while(len(cows)):
        cows_copy1=sorted(cows, key=cows.get, reverse=True)        
        #print(cows_copy1)
        avail_wt=limit
        trip=[]
        #cows_copy1=cows_copy.copy()
        for i in cows_copy1:
            if cows[i] <= avail_wt:
                avail_wt-=cows[i]
                trip.append(i)
                del cows[i]
        trips.append(trip)
    for keys in cows_copy:
        cows[keys]=cows_copy[keys]
    return trips 


# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    for partition in get_partitions(cows.keys()):
        flag=0
        for i in partition:
            l=[]
            for k in i:
                l.append(cows[k])
            if sum(l) > limit:
                flag = 1
        if flag == 0:
            return partition

# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    cows=load_cows("ps1_cow_data_2.txt")
    start=time.time()
    l=greedy_cow_transport(cows,10)
    end=time.time()
    print("Number of trips by greedy is "+str(len(l))+" time taken by greedy"+str(end-start))
    start=time.time()
    l=brute_force_cow_transport(cows,10)
    end=time.time()
    print("Number of trips by brute force is "+str(len(l))+" time taken by brute"+str(end-start))
    

if __name__ == '__main__':
    compare_cow_transport_algorithms()
#print(brute_force_cow_transport(cows,10))
#print(greedy_cow_transport(cows,10))