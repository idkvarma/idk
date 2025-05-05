ansible-playbook -i hosts.ini file_edit.yml --ask-pass

ansible-playbook -i hosts.ini file_edit.yml --ask-pass  -e 'ansible_ssh_common_args="-o StrictHostKeyChecking=no"'
