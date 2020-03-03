from pydrive_api import PyDriveApi


def lambda_handler(event, context):
    py_drive_api = PyDriveApi()
    return py_drive_api.read_file(event['filename'])


if __name__ == '__main__':
    print(lambda_handler({"filename":"DES_TXN_TYPES.csv"}, None))
