from random import randint
from random import choices

ticket=[n for n in range(10)] + [chr(a) for a in range(ord('a'),ord('f'))]
print(ticket)

my_ticket=[0,5,'b',4]
i=1
while True:
	i+=1
	lottery_ticket = choices(ticket, k=4)
	if lottery_ticket==my_ticket:
		break

print(i)
print(lottery_ticket)