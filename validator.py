# Simple validator script
import os

backend_path = '/home/yutw/project/md_templates/results/smart_farm_management/backend'
frontend_path = '/home/yutw/project/md_templates/results/smart_farm_management/frontend'

print('Checking backend files...')
for root, dirs, files in os.walk(backend_path):
    for f in files:
        if f.endswith('.py'):
            print(f'  {os.path.relpath(os.path.join(root, f), backend_path)}')

print('\nChecking frontend files...')
for root, dirs, files in os.walk(frontend_path):
    for f in files:
        if f.endswith('.vue') or f.endswith('.js') or f.endswith('.json'):
            print(f'  {os.path.relpath(os.path.join(root, f), frontend_path)}')
