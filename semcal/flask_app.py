
import json

import requests

from flask import Flask, Response

app = Flask(__name__)

mime_type = 'text/plain'


@app.route('/')
def root_route():
    return Response(response='usage : python.semcal.org/<package>[==<version>]', mimetype=mime_type)


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
        releases = pypi_data["releases"]
        if version in releases:
            release = releases[version][0]  # can there be more than one?
            upload_time = release['upload_time']
            calver = upload_time[0:7].replace('-','.')
            cal_response = f"{version}:{calver}"
        else:
            cal_response = f"version {version} not found"
    return Response(response=cal_response, mimetype=mime_type, status=request_response.status_code)


if __name__ == '__main__':
    app.run()
