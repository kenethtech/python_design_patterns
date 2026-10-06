

def generate_form(field_list=[], Check_list=[]):
    generated_fields = "\n".join(
        map(
            lambda x: '<label>{0}</label><br><input type="text" name="{0}"><br>'.format(x),
            field_list
        )
    )
    generated_fields += "\n".join(
        map(
            lambda x: '\n<label>{0}<br><input type="checkbox" id="{0}" value="{0}"><br>'.format(x),
            Check_list
        )
    )
    return "<form>{fields}</form>".format(fields=generated_fields)

#generate the html file with all the fields
def build_forms(field_list=[], checkboxes=[]):
    with open("form_file.html", "w") as form:
        form.write(
            "<DOCTYPE!>\n <html>\n <body>{}</body>\n </html>".format(generate_form(field_list=field_list, Check_list=checkboxes))
        )

if __name__ == "__main__":
    fields = ["name", "age", "sex", "email"]
    checked_fields = ["Male", "Female"]
    try:
        build_forms(field_list=fields, checkboxes=checked_fields)
        print("Fields generated succefully")
    except:
        print("Failed to generate the required fields")
        