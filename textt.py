import csv

with open ('subject.csv', 'r') as subject:
   subject=[row for row in csv.reader(subject)]
print(subject)


with open('location.csv', 'r') as location:
    location=[row for row in csv.reader(location)]
print(location)


#combine subject, location and classmark in a nested list
subject_location = subject

for i in subject_location: 
    for j in location: 
        if i[1] ==j[0]:
            i.append(j[1])
print(subject_location)

#create a function to prompt the user to select from 3 options 

def search():
    p =int(input('select from 1-3 (1 = subject, 2 = classs_mark, 3 = location): '))
    if p == 1:
       return subject()
    elif p == 2: 
         return class_mark()
    elif p == 3:
         return location()
    else:
        return 'no result for such entry, select between 1,2,3 only'
        
        
def subject():
    search = input('Enter a subject name or abbreviation: ')
    result = [item for item in subject_location if search.upper() in item[0]]
    return result
print(subject)
    
    
def class_mark():
    search_2 = input ('select a classmark: ')
    results = [item for item in subject_location if search_2.upper() in item [1]]
    return results 
#create a function to display the six locations as done above 

def location():
    search_3 =input('select from these six locations where 1 - Top Floor Front Left, 2 Top Floor Front Right, 3 - Top Floor Back Left, 4 - Top Floor Back Right 5 - Middle Floor 6 - Ground Floor: ')
    if int(search_3)  == 1:
        resultz = [item for item in subject_location if 'Top Floor Front Left' in item[2]]
        print('All Top Floor Front Left: ')
        return resultz 
    if int(search_3)  == 2:
        resultz = [item for item in subject_location if 'Top Floor Front Right' in item[2]]
        print('All Top Floor Front Right: ')
        return resultz 
    if int(search_3)  == 3:
        resultz = [item for item in subject_location if 'Top Floor Back Left' in item[2]]
        print('All Top Floor Back Left: ')
        return resultz
    if int(search_3)  == 4:
        resultz = [item for item in subject_location if 'Top Floor Back Right' in item[2]]
        print('All Top Floor Back Right: ')
        return resultz
    if int(search_3)  == 5:
        resultz = [item for item in subject_location if 'Middle Floor' in item[2]]
        print('All Middle Floor: ')
        return resultz
    if int(search_3)  == 6:
        resultz = [item for item in subject_location if 'Ground Floor' in item[2]]
        print('All Ground Floor: ')
        return resultz
    
   
