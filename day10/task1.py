def format_name(fname, lname):
    '''Hey i am writing a docnote here
    wadizup with yall?'''

    formated_fname = fname.title()
    formated_lname  = lname.title()

    return f"{formated_fname} {formated_lname}"
formatted_name = format_name("abbey", "jackson")
print(formatted_name)
