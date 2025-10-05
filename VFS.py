import zipfile
import os
import base64

class VFS:

    def __init__(self):
        self.zf = zipfile.ZipFile('vfs.zip', 'w')

    def read_file(self, filename):
        filename = self._add_start_path(filename)
        if self.contain_file(filename):
            base64_text = self.zf.read(filename).decode('ascii')
            return base64.b64decode(base64_text).decode('utf-8')
        raise FileNotFoundError(f"File {filename} not found in archive")

    def add_dir(self, dirname):
        if not self._check_filename(dirname):
            return
        dirname = self._add_start_path(dirname)

        self.zf.writestr(dirname + '/', b'')

    def add_file(self, filename, data):
        if not self._check_filename(filename):
            return
        filename = self._add_start_path(filename)
        data = data.encode('utf-8')
        data = base64.b64encode(data).decode('ascii')
        self.zf.writestr(filename, data)

    def get_files_in_dir(self, dir = '~/'):
        dir = self._add_start_path(dir)
        if dir[-1] != '/':
            dir += '/'

        zip_info = self.get_info()
        files = []
        for zip_file in zip_info:
            zip_file_name = zip_file.filename
            if zip_file_name.startswith(dir):
                relative_path = zip_file_name[len(dir):]
                if relative_path and relative_path.find('/') < 0:
                    files.append(relative_path)
        return files
    
    def get_dirs_in_dir(self, dir = '~/'):
        dir = self._add_start_path(dir)
        if dir[-1] != '/':
            dir += '/'

        zip_info = self.get_info()
        dirs = []
        for zip_file in zip_info:
            zip_file_name = zip_file.filename
            if zip_file_name.startswith(dir):
                relative_path = zip_file_name[len(dir):]
                if relative_path and relative_path.find('/') == len(relative_path)-1:
                    dirs.append(relative_path)
        return dirs
    
    def contain_file(self, filename):
        filename = self._add_start_path(filename)
        return filename in self.zf.namelist()
    
    def contain_dir(self, dirname):
        dirname = self._add_start_path(dirname)
        if dirname[-1] != '/':
            dirname += '/'
        return dirname in self.zf.namelist()

    def get_info(self):
        return self.zf.infolist()
    
    def get_info_file(self, filename):
        filename = self._add_start_path(filename)
        if self.contain_file(filename):
            return self.zf.getinfo(filename)
        raise FileNotFoundError(f"File {filename} not found in archive")

    
    def _add_start_path(self, filename):
        if filename[:1] != '~':
            return '~/' + filename
        if filename[:2] != '~/':
            return '~/' + filename[1:]
        return filename
    
    def _check_filename(self, filename):
        if filename.find('$') >= 0 or filename.find('\\') >= 0:
            return False
        return True

    def __del__(self):
        os.remove('vfs.zip')
        pass
