bd_division_info = {}

bd_division_info["Barishal"] = {"districts": 6, "upazilas": 39, "unions": 334}
bd_division_info["Chattogram"] = {"districts": 11, "upazilas": 39, "unions": 334}
bd_division_info["Dhaka"] = {"districts": 13, "upazilas": 39, "unions": 334}
bd_division_info["Khulna"] = {"districts": 10, "upazilas": 39, "unions": 334}
bd_division_info["Mymensingh"] = {"districts": 4, "upazilas": 39, "unions": 334}
bd_division_info["Rajshahi"] = {"districts": 8, "upazilas": 39, "unions": 334}
bd_division_info["Rangpur"] = {"districts": 8, "upazilas": 39, "unions": 334}
bd_division_info["Sylhet"] = {"districts": 4, "upazilas":   39, "unions": 334}


# print(bd_division_info)  # Printing the entire dictionary


divisions = bd_division_info.keys()  # Getting all keys in the dictionary


for division in divisions:
    print("Division:", division, " and ","Upazilas:", 
          bd_division_info[division]["upazilas"])  # Accessing value via using key
   

