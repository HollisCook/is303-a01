'''
Event Budget

Estimates the cost of a campus event

Event name, number of attendees, cost per person

Total cost = attendees * cost per person

inputs:
- Event name
- Number of attendees
- Cost per person

process:
- calculate the total cost
    - Total cost = attendees * cost per person

outputs:
- reveal total cost
'''

# input
print('\nPlease input the following information to estimate the cost of your campus event.')
event_name = input("\nEvent name: ")
attendee_number = int(input('Number of attendees: '))
cost_per_person = float(input('cost per person: '))

# process
Total_cost = attendee_number * cost_per_person

print(f'\n{event_name}')
print(f'- Number of Attendees: {attendee_number}')
print(f'- Cost Per Person: ${cost_per_person}')
print(f'- Total Cost: ${Total_cost:.2f}\n')