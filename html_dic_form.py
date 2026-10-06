
def generate_form(field_list):
    generated_lists = []

    for field in field_list:
        if field["type"] == "text":
            generated_lists.append(
                '<label>{0}:<br><input type="text" name="{1}"><br>'.format(field["label"], field["name"])
            )
        elif field["type"] == "checkbox":
            generated_lists.append(
                '<label><br><input type="checkbox" id="{0}" value="{1}">{2}<br>'.format(field["id"], field["value"], field["label"])
            )

    generated_field = "\n".join(generated_lists)

    return "<form>{fields}</form>".format(fields=generated_field)

def build_forms(field_list):
    with open("form_file.html", "w") as file:
        file.write(
            '<html><body>{}</body></html>'.format(generate_form(field_list=field_list))
        )

if __name__ == "__main__":
    field_list = [
        {
            "type": "text",
            "label": "This is a text label",
            "name": "Text field"
        },
        {
            "type": "checkbox",
            "id": "checkbox",
            "value": "checkboxes",
            "label": "Checkbox"
        }
    ]

    try:
        build_forms(field_list)
        print("Successfuly created the form and fields")

    except:
        print("Error creating fields")