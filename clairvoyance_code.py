import heapq

n = int(input())
bunny_cards = []
tracker = [0]*(2*n+1)
for i in range(n):
    card = int(input())
    heapq.heappush(bunny_cards, card)
    tracker[card]+=1
bunny_cards = [heapq.heappop(bunny_cards) for i in range(n)]
#print(bunny_cards)

harry_cards = []
for i in range(1, 2*n+1): 
    if tracker[i]==0: 
        harry_cards.append(i)

max_b_points = 0
b_index = n-1
h_index = n-1
while b_index >= 0 and h_index >= 0: 
    if harry_cards[h_index] < bunny_cards[b_index]: 
        b_index-=1
    else: 
        max_b_points+=1
        b_index-=1
        h_index-=1
        
print(max_b_points)
