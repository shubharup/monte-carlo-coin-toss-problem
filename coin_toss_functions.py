import numpy as np

def uniform(n, m):
  return np.random.randint(1, n+1, size = m)

# generate toss-triplet

# def toss_gen():
#   toss = {}
  
#   for j in [1,2,3]:
#     toss[j] = int(uniform(2,1)[0]) 
    
#   return(toss)

def all_tosses_gen(iterations):
  return(uniform(2, 3*iterations))

# heads is 1, tails is 2

def toss_score(toss):
  first_heads = None
  toss_score = -1

  for j in toss.keys():
    if toss[j] == 1:
      first_heads = j
      break

  if first_heads != None:
    toss_score = first_heads

  return(toss_score)

def count_heads(toss):
  count = 0

  for j in toss.keys():
    if toss[j] == 1:
      count += 1

  return(count)


def monte_carlo_estimate(rounds, all_tosses = None):
    
    all_tosses = all_tosses_gen(rounds)

    no = 0

    for t in range(rounds):

        toss_triplet = {1: all_tosses[3*t], 2: all_tosses[3*t + 1], 3: all_tosses[3*t + 2]}

        if (count_heads(toss_triplet) < 3) and (toss_score(toss_triplet) <= 1):
            no = no + 1

    mc_probability = no / rounds
    return(mc_probability)