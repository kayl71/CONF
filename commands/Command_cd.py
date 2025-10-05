from Command import Command

class Command_cd(Command):

    @property
    def name(self) -> str:
        return "cd"
    
    @property
    def decsription(self) -> str:
        return "Перемещение в другую директорию"
    
    def excecute(self, args, stdin, stdout, stderr, params, tools):
        cd_path = ""
        stdin_text = stdin.read()
        stdin.seek(0)
        if stdin_text != '':
            cd_path = stdin_text
        elif len(args) > 0:
            cd_path = args[0]
        else:
            stderr.write('No arguments')
            return 1
    
        if cd_path == '..':
            pwd = params['PWD']
            if pwd == '~':
                return 0
            params['PWD'] = pwd[:pwd.rfind('/')]
            return 0
        
        if not tools['VFS'].contain_dir(cd_path):
            stderr.write('No dir ' + params['PWD'] + '/' + cd_path)
            return 1
        params['PWD'] = params['PWD'] + '/' + cd_path
        return 0
