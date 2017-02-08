CFG = 'cfg.cfg.default'


class Config(object):
    VV = 'good'


class TestConfig(Config):
    # DEBUG = True
    CFG = 'test.cfg'


class ProductionConfig(Config):
    CFG = "prod.cfg"