from django.core.management import call_command


def backup_db():
    try:
        call_command('dbbackup', '--encrypt')
    except ConnectionError:
        print('db_backup is not works')
        pass


