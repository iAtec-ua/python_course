def get_file(file_name):
    with open("Car_Model_List.json") as file:
        return file.read()


def get_objects(json_objects):
    spec_symbols = ('{', '}', '[', ']', ',', ':')

    parts = []
    value = ""
    for symbol in json_objects:
        tmp_value = value.strip()
        if len(tmp_value) < 1 and symbol in spec_symbols:
            parts.append(symbol)
        else:
            value += symbol

        if symbol in spec_symbols:
            parts.append(symbol)
        else:
            value += symbol

        if len(tmp_value) >= 1:
            if symbol == "\"":
                parts.append(tmp_value[1:])
                value = ""
            elif symbol == ',' and "\"" not in value:
                parts.append(float(value[:-1]))
                value = ""
    return parts


def parse_objects(data):
    json_object = {}
    data = data[1:]
    if data[0] == '}':
        return json_object, data[1:]

    while True:
        key = data[0]

        if data[1] != ":":
            raise Exception('Expected colon after key')

        value, data = try_to_parse_object(data[2:])

        value = data[2]
        json_object[key] = value

        if data[3] == '}':
            return json_object, data[4:]
        elif data[3] != ',':
            raise Exception('Expected colon after key')

        data = data[1:]


def parse_array(data):
    json_array = []
    data = data[1:]

    if data[0] == ']':
        return json_objects, data[1:]

    while True:
        json, data = try_to_parse_object(data, True)
        json_array.append(json)

        if data[0] == ']':
            return json_array, data[1:]
        elif data[0] != ',':
            raise Exception('Expected colon after key')

        data = data[1:]


def try_to_parse_object(data, root = False):
    if data[0] and root not in ('{', '['):
        raise Exception("Incorrect structure")

    if data[0] == '[':
        return parse_array()
    elif data[0] == '{':
        return parse_objects()


def parse_json_string(json_string):
    data = get_objects(json_string)
    processed_object, data = try_to_parse_object(data)
    return processed_object


json_string = get_file("Car_Model_List.json")
data = get_objects(json_string)

json_objects, data = parse_objects(data)

print("")
print(data)
