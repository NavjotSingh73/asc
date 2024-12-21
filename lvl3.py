#Admin Task
print('admin operation')
services=[]
costs=[]
flag=True
while flag:
    services.append(input("Enter service: "))
    costs.append(float(input('Enter its cost: ')))
    k=input("Enter y to add more services: ")
    flag = k=='y'

patient_info=[]
patient_info.append(input("Patient Name: "))
patient_info.append(int(input("Patient Age: ")))
patient_info.append(input("Patient Gender: "))
patient_info.append(int(input("Patient contact info: ")))


# services=["1.General Consultation","2.Blood test","3. Covid Test","4.X-ray","5.CT scan","6. MRI"]
# costs=[1000,2000,3000,4000,5000,6000]
print("available services: \n")
for i in range(len(services)):
    print(f"{services[i]} :  ${costs[i]}")


selected_services=[]
cost_selected=[]
patient_selected=[]
patient_selected = list(map(int, input("Enter required services separated by spaces: ").split()))
for i in patient_selected:
    selected_services.append(services[i-1])
    cost_selected.append(costs[i-1])


print("selected services: ",selected_services)
print("costs of selected services",cost_selected)

subtotal=sum(cost_selected)
if patient_info[1]>=60: subtotal-=subtotal*0.1
if subtotal>5000: subtotal-=subtotal*0.05
gst=0.18*subtotal
# print("total cost of selected services",subtotal)
grand_total=subtotal+gst
# print("grand total cost of selected services", grand_total)

print('-'*40)
print('HealWell Care Hospital\npatient Invoice')
print('-'*40)
print('Patient Information: ')
print("Patient Name: ",patient_info[0])
print("Age: ",patient_info[1])
print("Gender: ",patient_info[2])
print("Contact info: ",patient_info[3])
print('\n')
print('Services availed: ')
for i in range(len(selected_services)):
    print(f'{selected_services[i]} : {cost_selected[i]}')

print('subtotal: ',subtotal)
print('GST 18%: ',gst)
print('Grand Total: ',grand_total)
# print('\n')
print('Thankyou for choosing HealWell care Hospital!! ')
print('-'*40)
