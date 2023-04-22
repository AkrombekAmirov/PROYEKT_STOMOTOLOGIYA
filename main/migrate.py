import argparse
from .config import engine
import user_repository.migrate as sqlmodel
import patient_repository.migrate as patient_migrate
import file_repository.migrate as file_migrate


modules = (
    'sqlmodel',
    'patient_migrate',
    'file_migrate'
)


def migrate():
    for module in modules:
        exec(f"{module}.migrate(engine)")


def remigrate():
    for module in modules:
        exec(f"{module}.remigrate(engine)")


parser = argparse.ArgumentParser(description='Migrate')
parser.add_argument('operation', default='migrate')

args = parser.parse_args()
if args.operation == 'migrate': migrate()
elif args.operation == 'remigrate': remigrate()
elif args.operation in modules:
    exec(f"{args.operation}.migrate(engine")
    exec(f"{args.operation}.migrate(engine)")
