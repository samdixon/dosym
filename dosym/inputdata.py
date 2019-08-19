class InputDataTransformer:
    def __init__(self, symlinks, optional):
        self.symlinks = symlinks
        self.optional = optional
        self.git_remote = None 
        self.local_path = None
        self.localpath_symlinks = None

        self._parse_optional_inputs()
        
        if self.local_path != None:
            self._join_local_path_and_key()

    def _parse_optional_inputs(self):
        if 'git_remote' in self.optional:
            self.git_remote = self.optional['git_remote']
        if 'local_path' in self.optional:
            self.local_path = self.optional['local_path']

    def determine_path_type(self):
        pass

    def _join_local_path_and_key(self):
        self.localpath_symlinks = {}
        for key,val in self.symlinks.items():
            join_char = "/"
            join_seq = (self.optional['local_path'], key)
            joined_key = join_char.join(join_seq)
            self.localpath_symlinks[joined_key] = val


