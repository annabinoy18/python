#Write a Python function frequency(l) that takes as input a list of integers and returns a pair of the form (minfreqlist,maxfreqlist) where
#minfreqlist is a list of numbers with minimum frequency in l, sorted in ascending order
#maxfreqlist is a list of numbers with maximum frequency in l, sorted in ascending order


#An airline has assigned each city that it serves a unique numeric code. It has collected information about all the direct flights it operates, represented as a list of pairs of the form (i,j), where i is the code of the starting city and j is the code of the destination.
#It now wants to compute all pairs of cities connected by one intermediate hope — city i is connected to city j by one intermediate hop if there are direct flights of the form (i,k) and (k,j) for some other city k. The airline is only interested in one hop flights between different cities — pairs of the form (i,i) are not useful.
#Write a Python function onehop(l) that takes as input a list of pairs representing direct flights, as described above, and returns a list of all pairs (i,j), where i != j, such that i and j are connected by one hop. Note that it may already be the case that there is a direct flight from i to j. So long as there is an intermediate k with a flight from i to k and from k to j, the list returned by the function should include (i,j). The input list may be in any order. The pairs in the output list should be in lexicographic (dictionary) order. Each pair should be listed exactly once.

def frequency(l):
    # Step 1: Calculate the frequency of each number
    freq_dict = {}
    for num in l:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1
    
    # Step 2: Find the minimum and maximum frequencies
    min_freq = min(freq_dict.values())
    max_freq = max(freq_dict.values())
    
    # Step 3: Create lists of numbers with minimum and maximum frequencies
    minfreqlist = [num for num, freq in freq_dict.items() if freq == min_freq]
    maxfreqlist = [num for num, freq in freq_dict.items() if freq == max_freq]
    
    # Step 4: Sort the lists in ascending order
    minfreqlist.sort()
    maxfreqlist.sort()
    
    # Step 5: Return the result as a pair
    return (minfreqlist, maxfreqlist)

def onehop(l):
    # Step 1: Initialize an empty set to collect all valid (i, j) pairs
    result = set()
    
    # Step 2: Iterate over each pair (i, j) and check for connections via an intermediate city k
    for i, j in l:
        for x, y in l:
            if j == x and i != y:  # Check if there's a valid connection via k
                result.add((i, y))  # Add the pair (i, y) to the result set
    
    # Step 3: Convert the set to a list and sort it in lexicographic order
    return sorted(result)




#solution by instructor
def frequency(l):
    count = {}
    for n in l:
        if n in count.keys():
            count[n] = count[n]+1
        else:
            count[n] = 1
    minlist = findmin(count)
    maxlist = findmax(count)
    return((minlist,maxlist))

def findmin(d):
    upperbound = 0
    for n in d.keys():
        if d[n] > upperbound:
            upperbound = d[n]

    minlist = []
    mincount = upperbound

    for n in d.keys():
        if d[n] < mincount:
            minlist = [n]
            mincount = d[n]
        elif d[n] == mincount:
            minlist.append(n)
    return(sorted(minlist))

            
def findmax(d):
    maxlist = []
    maxcount = 0

    for n in d.keys():
        if d[n] > maxcount:
            maxlist = [n]
            maxcount = d[n]
        elif d[n] == maxcount:
            maxlist.append(n)
    return(sorted(maxlist))

def onehop(l):
    direct = {}
    for (i,j) in l:
        if i in direct.keys():
            direct[i].append(j)
        else:
            direct[i] = [j]

    hopping = []

    for src in direct.keys():
        for dest in direct[src]:
            if dest in direct.keys():
                for remote in direct[dest]:
                    if src != remote:
                        hopping.append((src,remote))

    return(remdup(sorted(hopping)))
            
def remdup(l):
    if len(l) < 2:
        return(l)

    if l[0] != l[1]:
        return(l[0:1]+remdup(l[1:]))
    else:
        return(remdup(l[1:]))
