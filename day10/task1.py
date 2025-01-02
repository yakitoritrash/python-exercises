def format_name(fname, lname):
    formated_fname = fname.title()
    formated_lname  = lname.title()

    return f"{formated_fname} {formated_lname}"
formatted_name = format_name("abbey", "jackson")
print(formatted_name)
