# functions with outputs

def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


print(format_name("angeLa", "YU"))


# multiple returns

def format_name2(f_name, l_name):
    if f_name =="" or l_name =="":
        return "You did npt provide valid inputs"

    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

print(format_name2(input("enter first name",input("enter last name"))))





