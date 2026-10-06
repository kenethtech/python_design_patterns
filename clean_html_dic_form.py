

def generate_webforms(all_fields):
    generated_form_fields = []

    for field_form in all_fields:
        if field_form["type"] == "text":
            form_html = generate_text_fields(field_form)
        elif field_form["type"] == "checkbox":
            form_html = generate_checkbox(field_form)
        generated_form_fields.append(form_html)

    genarate_fields = "\n".join(generated_form_fields)

    return '<form>{field}</form>'.format(field=genarate_fields)

def generate_text_fields(text_fields):

    return '<label>{0}:<br><input type="{1}" name="{2}"><br>'.format(text_fields["label"], text_fields["type"], text_fields["name"])

def generate_checkbox(checkbox_field):

    return '<label>{2}:<br><input type="checkbox" name="{0}" value="{1}"><br>'.format(
        checkbox_field["name"],
        checkbox_field["value"],
        checkbox_field["label"]
    )

def build_forms(form_fields):
    with open("form_file1.html", "w") as file:
        file.write(
            '<html>\n<body>\n{}</body>\n</html>'.format(generate_webforms(form_fields))
        )


if __name__ == "__main__":
    fields = [
        {
            "type": "text",
            "name": "First_text",
            "label": "This is the first text field"
        },
        {
            "type": "checkbox",
            "name": "checkbox1",
            "value": "male",
            "label": "Male"
        }
    ]

    build_forms(fields)