employee_list = [
    {
        "name": "Tony Stark",
        "emp_id": 3,
        "address": [
            {
                "line1": "fff",
                "line2": "hhh",
                "state": "WB",
                "Pincode": "700107"
            },
            {
                "line1": "fff",
                "line2": "hhh",
                "state": "WB",
                "Pincode": "700107"
            }
        ]
    },
    {
        "name": "Steve Rogers",
        "emp_id": 6,
        "address": [
            {
                "line1": "fff",
                "line2": "hhh",
                "state": "WB",
                "Pincode": "700117"
            },
            {
                "line1": "fff",
                "line2": "hhh",
                "state": "WB",
                "Pincode": "700127"
            }
        ]
    }
]
def get_employee_address_details(employee_list,key):
            emp_pin_list = []
            for emp in employee_list:
                emp_pin_list.append({"name": emp["name"]})
                print(emp_pin_list)
                print(get_employee_address_details.index(emp))
                emp_pin_list[employee_list.index(emp)][key]=[]

                for address in emp["address"]:
                    emp_pin_list[employee_list.index(emp)][key].append(address[key])
                    return emp_pin_list

                    
                


