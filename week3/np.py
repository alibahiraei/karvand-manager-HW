import numpy as np

# تمرین اول بخش اول
gym_data = np.array([
[28, 75, 175, 4],
[34, 68, 168, 3],
[45, 82, 180, 2],
[22, 58, 162, 5],
[38, 90, 0, 1],
[29, 65, 170, 0]
])
member_names = np.array(["Ali", "Sara", "Reza", "Neda", "Hassan",
"Maryam"])
gym_data[4:5,2:3]=[170]
gym_data[5:,3:]=[6]
#print(gym_data)
################################################
# تمرین اول بخش دوم
number_data=gym_data[:,1:]
#print(number_data)
########################################
#تمرین اول بخش سوم

wigeth=number_data[:,-3:-2]
height=number_data[:,-2:-1]/100
BMI_data=wigeth/height**2  
BMI_data=np.round(BMI_data,1)                                
#print("bmi",BMI_data) 
number_sessions=number_data[:,-1:]
#print(number_sessions)
score_data=number_sessions+(BMI_data*2)
number_new= np.column_stack((number_data,score_data))
#print(number_new)
########################################################
# تمرین اول بخش چهارم


new_members=np.column_stack((member_names,gym_data))
new_members=np.column_stack((new_members,score_data))
#print(new_members)
scores = new_members[:,5].astype(float)
index = np.argmax(scores)


#print("Highest score:", scores[index])
#print("Member:", new_members[index, 0])
##################################################
#تمرین اول بخش پنجم
mean_score=np.mean(number_sessions)
std_scors=np.std(number_sessions)
max_m=mean_score+std_scors
min_m=mean_score-std_scors
max_difference= np.where((number_sessions> max_m)|(number_sessions<min_m ))
print(max_difference)

print(F"max diffrence to members is {new_members[4,0]} and {new_members[5,0]}")
#####################################################################################
#تمرین دوم بخش اول



