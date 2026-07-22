def meaningful_lines(lines):
    result = []

    for line in lines:
        cleaned = line.strip()

        if cleaned != "" and not cleaned.startswith("#"):
            result.append(cleaned)

    return result

def parse_setting(line):
    if "=" not in line:
        raise ValueError("Input not in acceptable format"
                         "(i.e. 'Hello World' -> 'Hello = World')")
    split_list = line.split("=", 1)
    stripped = []

    for item in split_list:
        strip_str = item.strip()
        if strip_str == "":
            raise ValueError("Setting key or value"
                             "must not be empty")
        stripped.append(strip_str)

    parsed = tuple(stripped)
    return parsed

def parse_config(lines):
    config = {}
    cleaned_lines = meaningful_lines(lines) 

    for line in cleaned_lines:
        key, value = parse_setting(line) 
        if key in config:
            raise ValueError("Key is a duplicate and"
                             "will not be parsed")
        config[key] = value 

    return config

def load_config(path):
    with open(path, "r", encoding="utf-8") as f:
        parsed_content = parse_config(f)
        return parsed_content
