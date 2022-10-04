def test_quantumprocessor(self):
    """amount resulted of quantuam processor should be 9999
    """
    self.assertEqual(self.quantumprocessor.amountonhand, 9999)


def test_protocitebarb(self):
    """amount resulted of protocite bar should be 9999
    """
    self.assertEqual(self.protocitebarb.amountonhand, 9999)


def test_protociteoreb(self):
    """amount resulted of protocite should be 19998
    """
    self.assertEqual(self.protociteoreb.amountonhand, 19998)


def test_siliconboard(self):
    """amount resulted of silicon board should be 19998
    """
    self.assertEqual(self.siliconboard.amountonhand, 19998)


def test_silicon(self):
    """amount resulted of silicon should be 19998"""
    self.assertEqual(self.silicon.amountonhand, 19998)


def test_sand(self):
    """amount resulted of sand 999900"""
    self.assertEqual(self.sand.amountonhand, 19998*50)


def test_copperwire(self):
    """amount resulted of copper wire 19998"""
    self.assertEqual(self.copperwire.amountonhand, 19998)


def test_copperbar(self):
    """amount resulted of copper bar 179982"""
    self.assertEqual(self.copperbar.amountonhand, 19998*9)


def test_copperore(self):
    """amount resulted of copper ore 359964"""
    self.assertEqual(self.copperor.amountonhand, 359964)
