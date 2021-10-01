#https://www.hackerrank.com/challenges/py-the-captains-room/problem
members_in_group = int(input())
room_numbers = list(map(int, input().split()))
captain_room = set()
group_room = set()

for rooms in room_numbers:
	if rooms in captain_room:
		group_room.add(rooms)
	else:
		captain_room.add(rooms)

print(*captain_room.difference(group_room))
	