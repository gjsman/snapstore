from flask import Flask, Response, request, send_from_directory
import sys

FILES = 'files'


app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello basic snap store!'


@app.route('/api/v1/search')
def search():
    ''' note in 2.0.9 snapd still uses search for package details
    before install as well as for find '''
    name = request.args.get('q')
    # hackity hack hack: find passes q=package_name:"foo"
    if 'package_name' in name:
        name = name.split(':')[1].replace('"', '')

    # TODO: sanitize names
    # TODO: replace download URLs in metadata
    try:
        with open(FILES + '/' + name + '.meta', 'r') as meta:
            return Response(meta.read(), mimetype='application/hal+json')
    except Exception as e:
        return Response('{}', mimetype='application/hal+json')


@app.route('/anon/download-snap/<name>')
def anon_download(name):
    # TODO: sanitize names
    return send_from_directory(FILES, name)


@app.route('/download-snap/<name>')
def download(name):
    # TODO: sanitize names
    return send_from_directory(FILES, name)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
