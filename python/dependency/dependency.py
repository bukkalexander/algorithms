class Dependency:
    def setup(self):
        self.fetch()
        self.build()
        self.install()

    def fetch(self):
        pass

    def build(self):
        pass
    
    def install(self):
        pass
