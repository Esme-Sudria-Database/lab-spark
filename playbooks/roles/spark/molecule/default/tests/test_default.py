import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_spark_shell_command_should_exists(host):
    assert host.exists('spark-shell')


def test_pyspark_command_should_exists(host):
    assert host.exists('pyspark')


def test_spark_shell_is_running_correctly(host):
    cmd = host.run('. /etc/environment; spark-shell --version')
    assert cmd.rc == 0, '{0}\n{1}'.format(cmd.stdout, cmd.stderr)


def test_SPARK_HOME_exists(host):
    cmd = host.run('. /etc/environment; test -z "$SPARK_HOME"')
    assert cmd.rc == 1, 'SPARK_HOME is required'
