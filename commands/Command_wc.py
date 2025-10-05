from Command import Command

class Command_wc(Command):

    @property
    def name(self) -> str:
        return "wc"
    
    @property
    def decsription(self) -> str:
        return "Вывод количества строк, слов, байт файла и его имя"
    
    def excecute(self, args, stdin, stdout, stderr, params, tools):
        vfs = tools['VFS']
        for arg in args:
            full_file_name = params['PWD'] + '/' + arg
            if vfs.contain_file(full_file_name):
                text = vfs.read_file(full_file_name)

                lines_count = len(text.splitlines())
                word_count = len(text.split())
                text_size = vfs.get_info_file(full_file_name).file_size
                stdout.write(str(lines_count) + ' ' + str(word_count) + ' ' + str(text_size) + ' ' + arg + '\n')
            else:
                stderr.write(full_file_name + ": No such file\n")
        return 0
