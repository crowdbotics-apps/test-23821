from django import template

InputType = {'I': 'text', 'R': 'radio', 'C': 'radio'}
register = template.Library()


@register.simple_tag
def create_input(question):
    form_group_start = '<div class="form-group">'
    label = ''
    element = ''
    form_group_end = '</div>'
    question_type = question['type']
    title = question['question']
    value = question['value']
    question_id = str(question['id'])
    error = str(question['error'])
    required = ''
    if question['required']:
        required = 'required'
    info_label = ''
    if required != '':
        info_label = '<span class="required-field">*</span>'

    # create input element
    if question_type == 'I':
        label = '<label>' + title + info_label + '</label>'
        element = input_element(value, question_id, required)

    # create checkbox element
    elif question_type == 'C':
        form_group_start = '<div class="form-group form-checkbox">'
        label = '<label>' + title + info_label + '</label>'
        element = checkbox_element(question, question_id, value, required)

    # create select element
    elif question_type == 'S':
        label = '<label>' + title + info_label + '</label>'
        element = select_element(question, question_id, value, required)
    else:
        label = '<label>' + title + info_label + '</label>'
        element = '<textarea ''class="form-control"  name="' + question_id + '" ' + required + '>' + value + '</textarea>'
    field_error = ''
    if eval(error):
        field_error = '<p class="field-error">This field is required.</p>'

    html = form_group_start + label + element + field_error + form_group_end
    return html


def input_element(value, name, required):
    return '<input type="text" value="' + value + '" class="form-control"  ' \
                                                  'name="' + name + '" ' + required + '>'


def checkbox_element(question, question_id, value, required):
    checkbox = ''
    for option in question['option']:
        checked = ''
        checkbox_start = '<div  class ="custom-control custom-checkbox" >'
        option_id = question_id + '_' + str(option)
        if option == value:
            checked = 'checked'
        checkbox_value = '<input type = "radio" class ="custom-control-input"' \
                         ' id="id_' + option_id + '" ' + checked + ' value="' + \
                         str(option) + '" name="' + question_id + '" ' + required + ' >'
        checkbox_label = '<label for="id_' + option_id + '" class ="custom-control-label">' \
                         + option + '</label >'
        checkbox_end = '</div>'
        checkbox += checkbox_start + checkbox_value + checkbox_label + checkbox_end
    return checkbox


def select_element(question, question_id, value, required):
    select_start = '<select class ="form-control" name="' + question_id + '" ' + required + '>'
    select_option = ''
    for option in question['option']:
        selected = ''
        if option == value:
            selected = 'selected'
        select_option += '<option value=' + option + ' ' + selected + ' > ' + option + ' </option>'
    select_end = '</select>'
    return select_start + select_option + select_end
