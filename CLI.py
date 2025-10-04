from CommandManager import CommandManager
import re
from io import StringIO

class CLI:
    def __init__(self):
        self.params = {"USER" : "username", "HOSTNAME" : "hostname", "PWD" : "~", "RUNNING" : "True"}
        self.command_manager = CommandManager()
        self.stdin = StringIO()
        self.stdout = StringIO()
        self.stderr = StringIO()  
        

    def get_start(self):
        return self.params["USER"] + "@" + self.params["HOSTNAME"] + ":" + self.params["PWD"] + "$ "
    
    def read(self):
        # Ввод
        command_line = input(self.get_start())

        if not command_line:
            return

        # Подстановка переменных
        command_line = self._replace_variables_on_line(command_line)

        # Токенизация
        splitted_line_conv = command_line.split('|')
        splitted_line = command_line.split()

        #Выполнение команд
        for segment_conv in splitted_line_conv:
            segment_conv_splitted = segment_conv.split()
            if self.command_manager.contain_command(segment_conv_splitted[0]):
                self.command_manager.execute_command(segment_conv_splitted[0], segment_conv_splitted[1:], self.stdin, self.stdout, self.stderr, self.params)

                # Запись выхода команды на вход следующией команды 
                self.stdin.seek(0)
                self.stdin.truncate(0)
                self.stdout.seek(0)
                self.stdin.write(self.stdout.read())
                self.stdin.seek(0)
                self.stdout.seek(0)
                self.stdout.truncate(0)
            else:
                self.stderr.write("Error! Have not command " + splitted_line[0] + '\n')

        if self.stdin.read():
            self.stdin.seek(0)
            self.stdout.write(self.stdin.read())
            self.stdin.seek(0)
            self.stdin.truncate(0)
        
        # Печатаем выход последней команды
        self.print()
            
    def run(self):
        while self._running():
            self.read()

    def _running(self):
        return self.params['RUNNING'] and self.params['RUNNING'] == "True"
            

    def _replace_variables_on_line(self, text_line):
        keys = '|'.join(self.params.keys())
        pattern1 = r'\${(' + keys + r')}'
        pattern2 = r'\$(' + keys + r')'
        text_after_pattern1 = re.sub(pattern1, lambda match: self.params[match.group(1)], text_line)
        return re.sub(pattern2, lambda match: self.params[match.group(1)], text_after_pattern1)
        
    def print(self):
        self.stderr.seek(0)
        self.stdout.seek(0)
        print(self.stderr.read(), end='')
        print(self.stdout.read())
        self.stderr.seek(0)
        self.stdout.seek(0)
        self.stderr.truncate(0)
        self.stdout.truncate(0)
