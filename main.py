# Python code for JSON format converter

import json

class JSONConverter:
    @staticmethod
    def json_to_dict(json_data):
        try:
            return json.loads(json_data)
        except json.JSONDecodeError:
            return None

    @staticmethod
    def dict_to_json(data_dict):
        try:
            return json.dumps(data_dict, indent=4)
        except (TypeError, ValueError):
            return None

if __name__ == '__main__':
    # Example usage
    data = '{"key": "value"}'
    converter = JSONConverter()
    data_dict = converter.json_to_dict(data)
    print(data_dict)
    json_data = converter.dict_to_json(data_dict)
    print(json_data)
