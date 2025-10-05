from Command import Command

class Command_set(Command):

    @property
    def name(self) -> str:
        return "set"
    
    @property
    def decsription(self) -> str:
        return "Устанавливает значение переменной"
    
    def excecute(self, args, stdin, stdout, stderr, params, tools):
        stdin_text = stdin.read()
        if len(args) == 0 and len(stdin_text) == 0:
            stderr.write("No arguments")
            return 1
        
        param_name = ""
        param_value = ""

        if len(stdin_text) != 0:
            stdin_text_split = stdin_text.split()
            if len(stdin_text_split) < 2:
                stderr.write("Need 2 arguments")
                return 1
            
            param_name = stdin_text_split[0]
            param_value = stdin_text[1]

        if len(args) > 1:
            param_name = args[0]
            param_value = args[1]
        
        if param_name == "" or '$' in param_name:
            stderr.write("Wrong param name")
            return 1

        params[param_name] = param_value
        return 0