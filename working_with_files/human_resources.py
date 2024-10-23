with open('hr_system.txt') as staff_info:
    
    for staff in staff_info:
        staff_details = staff.strip()

        staff_details = staff_details.split(' ')
        # print(staff_details)

        staff_name = staff_details[0]
        staff_ID = int(staff_details[1])
        staff_job_title = staff_details[2]
        staff_salary = float(staff_details[3])

        staff_salary = staff_salary / 24

        if staff_job_title.lower() == 'engineer':
            staff_salary += 1000

        print(f'Name: {staff_name} (ID: {staff_ID}),  {staff_job_title} - ${staff_salary: .2f}')