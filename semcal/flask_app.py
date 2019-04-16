import time
import json

import requests

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return f'This is python.semcal.org. time.time() returned {time.time()}'


# todo: should this be <package>[==<version>] or <package>[/<version>] ?  The latter is more REST-like.
@app.route('/<package>')
def sem_to_cal(package):
    # http://pypi.python.org/pypi/<package_name>/json
    double_equals = "=="
    base_package = package.split(double_equals)[0]
    url = f"https://pypi.python.org/pypi/{base_package}/json"
    request_response = requests.get(url)
    print(url)
    if request_response.status_code != 200:
        cal_response = f"{package} not found"  # todo: set response error code
    else:
        pypi_data = json.loads(request_response.text)
        if double_equals in package:
            version = package.split(double_equals)[1]
        else:
            version = pypi_data['info']['version']  # latest version
        release = pypi_data["releases"][version][0]  # can there be more than one?
        upload_time = release['upload_time']
        calver = upload_time[0:7].replace('-','.')
        cal_response = f"{version}:{calver}"
    return cal_response


if __name__ == '__main__':
    app.run()
