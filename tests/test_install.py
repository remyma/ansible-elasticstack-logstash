import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_kibana_running(Service):
    kibana = Service("logstash")
    assert kibana.is_enabled
    assert kibana.is_running
