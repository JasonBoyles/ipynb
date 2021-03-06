import re
from fabric.api import env, hide, run, task
from envassert import detect, file, package, port, process, service


def ipynb_is_responding():
    with hide('running', 'stdout'):
        homepage = run("wget --no-check-certificate --quiet --output-document - https://localhost/")
        if re.search('IPython Notebook', homepage):
            return True
        else:
            return False


@task
def check():
    env.platform_family = detect.detect()

    assert port.is_listening(80)
    assert port.is_listening(443)
    assert port.is_listening(8888)
    assert process.is_up("nginx")
    assert service.is_enabled("nginx")
    assert ipynb_is_responding()
