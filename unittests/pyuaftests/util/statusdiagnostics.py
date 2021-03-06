import pyuaf
import unittest
from pyuaf.util.unittesting import parseArgs


ARGS = parseArgs()


def suite(args=None):
    if args is not None:
        global ARGS
        ARGS = args
    
    return unittest.TestLoader().loadTestsFromTestCase(StatusDiagnosticsTest)



class StatusDiagnosticsTest(unittest.TestCase):
    
    def setUp(self):
        self.s0  = pyuaf.util.StatusDiagnostics()
        self.s0_ = pyuaf.util.StatusDiagnostics()
        self.s1  = pyuaf.util.StatusDiagnostics()
        self.s2  = pyuaf.util.StatusDiagnostics()
    
    def test_util_StatusDiagnostics_setDescription(self):
        self.s0.setDescription("test")
        self.s0_.setDescription("test")
        self.s1.setDescription("somethingElse")    
        
    def test_util_StatusDiagnostics_setClientHandles(self):
        self.s0.setClientHandles([1,2,3])
        self.s0_.setClientHandles([1,2,3])
        self.s2.setClientHandles([4,5,6,7])
    
    def test_util_StatusDiagnostics_getDescription(self):
        self.test_util_StatusDiagnostics_setDescription()
        self.assertEqual( self.s0.getDescription() , "test" )
    
    def test_util_StatusDiagnostics_hasDescription(self):
        self.test_util_StatusDiagnostics_setDescription()
        self.assertTrue( self.s0.hasDescription() )
    
    def test_util_StatusDiagnostics_getClientHandles(self):
        self.test_util_StatusDiagnostics_setClientHandles()
        self.assertEqual( self.s0.getClientHandles() , (1,2,3) )
    
    def test_util_StatusDiagnostics_hasClientHandles(self):
        self.test_util_StatusDiagnostics_setClientHandles()
        self.assertTrue( self.s0.hasClientHandles() )
    
    def test_util_StatusDiagnostics___eq__(self):
        self.test_util_StatusDiagnostics_setClientHandles()
        self.test_util_StatusDiagnostics_setDescription()
        self.assertTrue( self.s0 == self.s0_ )
    
    def test_util_StatusDiagnostics___ne__(self):
        self.test_util_StatusDiagnostics_setClientHandles()
        self.test_util_StatusDiagnostics_setDescription()
        self.assertTrue( self.s0 != self.s1 )
        self.assertTrue( self.s0 != self.s2 )
        self.assertTrue( self.s1 != self.s2 )
    
    def test_util_StatusDiagnostics___lt__(self):
        self.test_util_StatusDiagnostics_setClientHandles()
        self.test_util_StatusDiagnostics_setDescription()
        self.assertTrue( self.s1 < self.s0 )
        self.assertTrue( self.s2 < self.s0 )
        self.assertTrue( self.s2 < self.s1 )
    
    def test_util_StatusDiagnostics___gt__(self):
        self.test_util_StatusDiagnostics_setClientHandles()
        self.test_util_StatusDiagnostics_setDescription()
        self.assertTrue( self.s0 > self.s1 )
        self.assertTrue( self.s0 > self.s2 )
        self.assertTrue( self.s1 > self.s2 )



if __name__ == '__main__':
    unittest.TextTestRunner(verbosity = ARGS.verbosity).run(suite())
        
