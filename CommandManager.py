from typing import Dict, List, TextIO
from Command import Command
import importlib
from pathlib import Path

class CommandManager:
    def __init__(self, commands_dir = "commands"):
        self.commands: Dict[str, Command] = {}

        commands_path = Path(commands_dir)
            
        if not commands_path.exists():
            print(f"Warning: Commands directory '{commands_dir}' not found")
            return
        
        # Ищем все Python файлы в директории
        for file_path in commands_path.glob("*.py"):
            if file_path.name.startswith("__"):
                continue
            
            module_name = file_path.stem
            self._load_command_from_module(commands_dir, module_name)


    def _load_command_from_module(self, package_path: str, module_name: str):
        """Загружает команды из конкретного модуля"""
        # Создаем полное имя модуля
        full_module_name = f"{package_path}.{module_name}"
        
        # Импортируем модуль
        module = importlib.import_module(full_module_name)
        
        # Ищем все классы команд в модуле
        for attr_name in dir(module):
            attr = getattr(module, attr_name)
            
            # Проверяем, что это класс команды (но не абстрактный)
            if (isinstance(attr, type) and 
                issubclass(attr, Command) and 
                attr != Command and
                hasattr(attr, 'name')):
                
                # Создаем экземпляр и регистрируем
                command_instance = attr()
                self.add_command(command_instance)

    def add_command(self, command: Command):
        """Добавить команду"""
        self.commands[command.name] = command

    def get_command(self, command_name: str):
        """Получить команду по имени"""
        return self.commands.get(command_name)
    
    def contain_command(self, command_name: str):
        """Проверить существование команды по имени"""
        return self.commands.__contains__(command_name)
    
    def execute_command(self, command_name: str, args: List[str], stdin: TextIO, stdout: TextIO, stderr: TextIO, params: Dict[str, str]):
        """Выполить команду по имени"""
        self.commands.get(command_name).excecute(args, stdin, stdout, stderr, params)