from random import randint

students = [
    'Aniya',
    'Aabriti Khanal',
    'Ali Hussain', 
    'Catherine Uwakwe',    
    'Christopher Toussaint',
    'Dhamani',
    'Emily Kruger',    
    'E Elizabeth',
    'Eric Lozado',
    'Gaby Peralta',   
    'Geaninne Chacha',       
    'Herman',
    'Justin',
    'Jasmine Kaur',
    'Josh Magazine',    
    'Kimberly Mark',
    'Marcos',    
    'Maria the Great and Powerful',
    'Marie Krou',
    'Mía Supreme Graham',
    'Madison Williams',    
    'Manuel Polanco',
    'Mamadou Bah',    
    'Mercedes Urena',
    'Omar Mendez',
    'Olivia Mofus',
    'RJ Maldonado',    
    'Raincoat Rick',
    'Sergio',   
    'Vandell Vatel',    
    'Yazmeene Louis',    
]

def randomly_pair_students(students, group_size):
    groups = []
    current_group = []
    
    while len(students) > 0:
        rand_num = randint(0, len(students)-1)
        rand_student = students[rand_num]
        
        current_group.append(rand_student)
        
        students.remove(rand_student)
        
        if len(current_group) == group_size:
            groups.append(current_group)
            current_group = []
            
    if len(current_group) > 0:
        groups.append(current_group)
        
    return groups
    
all_groups = randomly_pair_students(students, 2)

for idx, group in enumerate(all_groups):
    team = 'team {}: '.format(idx+1)
    for student in group:
        team += ' {},'.format(student)
    print(team)