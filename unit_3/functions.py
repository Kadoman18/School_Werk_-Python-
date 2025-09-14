def print_list(list):
        countdown = len(list) - 1
        while countdown >= 0:
                print(f'[ ] {list[countdown]}')
                countdown -= 1
                
def print_statement(list):
        count = len(list)
        camping_items = sorted(list)
        print(f'\nNumber of Items Needed: {count}\n\nList Items: ')
        print_list(list)
        print()