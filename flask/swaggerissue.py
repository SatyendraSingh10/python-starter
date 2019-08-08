import os
from flask import (
    Flask, send_from_directory,
    request, jsonify
)

app = Flask(__name__)

app_folder = os.path.abspath(os.path.join(os.path.join(os.path.join(os.path.dirname(__file__),
                                                                    os.path.pardir),
                                                       os.path.pardir)))
swagger_folder = os.path.join(app_folder, 'swagger')


class ApiGwAppConstants(object):
    APP_CENTRAL = 'central'

    @classmethod
    def apps(cls):
        return [
            cls.APP_CENTRAL,
        ]


class AcpApps(object):
    APP_NMS = 'nms'
    APP_ANALYTICS = 'analytics'
    APP_DEVICE_PROFILING = 'device_profiling'
    ACP_PLATFORM = 'acp_platform'
    ALL_APPS = {APP_NMS, APP_ANALYTICS, APP_DEVICE_PROFILING}
    MSP_ALLOWED_APPS = {APP_NMS}
    WHITELISTED_APPS = {APP_DEVICE_PROFILING}


class AuthServerConstants(object):
    LOCALDB = 'localdb'
    ARUBASSO = 'sso'
    EXTERNAL = 'external'


class DeploymentConstants(object):
    PUBLIC = 'public'
    PRIVATE = 'private'
    ONPREM = 'on-prem'


@app.route('/apps/<appname>/', methods=['GET', 'POST'])
@app.route('/central/', methods=['GET'])
def index(appname=ApiGwAppConstants.APP_CENTRAL):
    # maintaining backward compatibility between NMS and Central
    if appname == AcpApps.APP_NMS:
        appname = ApiGwAppConstants.APP_CENTRAL
    if request.method == 'POST':
        msg = "unsupported method"
        return jsonify(message=msg), 405
    return send_from_directory("{}/{}".format(swagger_folder, appname), 'index.html')


#@app.route('/apps/<appname>/css/<path:filename>')
@app.route('/css/<path:filename>')
def send_css_files(filename, appname=ApiGwAppConstants.APP_CENTRAL):
    # maintaining backward compatibility between NMS and Central
    # if appname == AcpApps.APP_NMS:
    #     appname = ApiGwAppConstants.APP_CENTRAL

    return send_from_directory(os.path.join("{}/{}".format(swagger_folder, appname), 'css'), filename)


#@app.route('/apps/<appname>/lib/<path:filename>')
@app.route('/lib/<path:filename>')
def send_lib_file(filename, appname=ApiGwAppConstants.APP_CENTRAL):
    # maintaining backward compatibility between NMS and Central
    # if appname == AcpApps.APP_NMS:
    #     appname = ApiGwAppConstants.APP_CENTRAL


    return send_from_directory(os.path.join("{}/{}".format(swagger_folder, appname), 'lib'), filename)


@app.route('/apps/<appname>/<path:filename>')
@app.route('/central/<path:filename>')
# @app.route('/apps/<path:filename>')
def send_static_file(filename, appname=ApiGwAppConstants.APP_CENTRAL):
    # maintaining backward compatibility between NMS and Central
    if appname == AcpApps.APP_NMS:
        appname = ApiGwAppConstants.APP_CENTRAL


    return send_from_directory("{}/{}".format(swagger_folder, appname), filename)


@app.route('/central/proto_topics')
def get_proto_display():
    proto_list = ['Apprf', 'Audit', 'Monitoring', 'Presence', 'Streaming', 'Location', 'Rapids']
    return jsonify({"proto_topics": proto_list})


#@app.route('/apps/<appname>/images/<path:filename>')
@app.route('/images/<path:filename>')
def send_image(filename, appname=ApiGwAppConstants.APP_CENTRAL):
    # maintaining backward compatibility between NMS and Central
    # if appname == AcpApps.APP_NMS:
    #     appname = ApiGwAppConstants.APP_CENTRAL


    return send_from_directory(os.path.join("{}/{}".format(swagger_folder, appname), 'images'), filename)


@app.route('/central/hidden_services')
def get_hidden_services():
    return jsonify({"hidden_services": Config.get_hidden_services_for_deployment})


if __name__ == '__main__':
    print(swagger_folder)
    app.run(debug=True)
