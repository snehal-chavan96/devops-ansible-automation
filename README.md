# Automated Flask Application Deployment Using Ansible on AWS EC2

## Project Overview
This project automates the deployment of a Python Flask application on an Amazon Linux 2023 EC2 instance using Ansible.

Ansible handles package installation, application deployment, Gunicorn service configuration, and Nginx reverse proxy setup.

## Tech Stack
- **Cloud:** AWS EC2
- **OS:** Amazon Linux 2023
- **Control Node:** Ubuntu (WSL2)
- **Automation:** Ansible
- **Application:** Python Flask
- **Application Server:** Gunicorn
- **Web Server:** Nginx
- **Version Control:** Git and GitHub

## Architecture
Windows Laptop → Ubuntu WSL2 (Ansible Control Node) → SSH → AWS EC2 (Managed Node)

## Project Structure
```text
application/
  app.py
  requirements.txt

ansible/
  ansible.cfg
  inventory.ini
  playbook.yml
  group_vars/
  templates/

architecture/
screenshots/
README.md
.gitignore
```

## Deployment Steps
1. Configure Ubuntu WSL2 and install Ansible.
2. Launch an Amazon Linux 2023 EC2 instance.
3. Configure SSH connectivity.
4. Set up the Ansible inventory.
5. Create the Flask application.
6. Configure deployment using Ansible playbooks.
7. Deploy Flask with Gunicorn and configure Nginx.
8. Verify application availability.

## Execution

```bash
# Check Ansible version
ansible --version

# Test connectivity
ansible webservers -m ping

# Validate playbook
ansible-playbook --syntax-check playbook.yml

# Deploy application
ansible-playbook playbook.yml
```

## Application Endpoints

| Endpoint | Description |
|---|---|
| `/` | Application homepage |
| `/health` | Application health check |

## Verification
- Verify Ansible connectivity.
- Check Gunicorn and Nginx services.
- Access the application through the EC2 public IP.
- Test the `/health` endpoint.
- Run the playbook again to verify idempotency.

## Security
- SSH access restricted to the administrator's IP.
- Private SSH keys excluded from Git.
- Gunicorn configured to listen on localhost.
- Only HTTP traffic exposed publicly for demonstration.

## Learning Outcomes
- Ansible automation and configuration management.
- AWS EC2 deployment.
- Flask application deployment using Gunicorn.
- Nginx reverse proxy configuration.
- Linux service management using systemd.
- Infrastructure automation and idempotency.
