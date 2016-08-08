import pkgutil
import argparse


def iter_commands():
    from . import commands

    for (module_loader, name, ispkg) in pkgutil.iter_modules(commands.__path__):
        module_name = '.'.join([commands.__name__, name])

        module = module_loader.find_module(name).load_module(module_name)

        command = getattr(module, 'Command')

        if command:
            yield (name, command)


def main():
    arg_parser = argparse.ArgumentParser(prog='zyn')

    subparsers = arg_parser.add_subparsers(
        title='action',
        description='Choose action'
    )

    for (name, command_class) in iter_commands():
        command_obj = command_class()
        parser = subparsers.add_parser(name, help=command_obj.help)
        parser.set_defaults(command=command_obj)

        command_obj.add_arguments(parser)

    namespace = arg_parser.parse_args()

    namespace.command.execute(namespace)