
#generate html elements of a form
def generate_forms(field_list):
    generated_fields = "\n".join(
        map(
            lambda x: '<label>{0}</label>:<br><input type=text name="{0}"><br>'.format(x),
            field_list
        )
    )
    #return a form with the generated fields
    return "<form>{fields}</form>".format(fields=generated_fields)

if __name__ == "__main__":
    field = []
    while True:

        input_fields = str(input("Enter the fields you would like to be generated input 'q' if done: "))
        field.append(input_fields.lower())

        if input_fields == 'q':
            break

    print(generate_forms(field))