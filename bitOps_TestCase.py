#!/usr/bin/python

import unittest
import bitOps

class bitOps_TestCase(unittest.TestCase):
    
    def test_CheckBit(self):
        self.assertEqual(bitOps.CheckBit(0x01, 0), True, 'Check lsb')
        self.assertEqual(bitOps.CheckBit(0x80, 7), True, 'Check msb')
        self.assertEqual(bitOps.CheckBit(0x00, 1), False, 'Check from empty')

    def test_SetBit(self):
        self.assertEqual(bitOps.SetBit(0x00, 0), 0x01, 'Set lsb')
        self.assertEqual(bitOps.SetBit(0x00, 7), 0x80, 'Set msb')
        self.assertEqual(bitOps.SetBit(0xa0, 0), 0xa1, 'Set lsb')
        self.assertEqual(bitOps.SetBit(0xf2, 0), 0xf3, 'Set lsb')
        
    def test_ClearBit(self):
        self.assertEqual(bitOps.ClearBit(0xff, 0), 0xfe, 'Clear lsb')
        self.assertEqual(bitOps.ClearBit(0xff, 7), 0x7f, 'Clear msb')
        self.assertEqual(bitOps.ClearBit(0xa3, 0), 0xa2, 'Clear lsb')
        self.assertEqual(bitOps.ClearBit(0xa3, 7), 0x23, 'Clear msb')  
    
    def test_FlipBit(self):
        self.assertEqual(bitOps.FlipBit(0xff, 0), 0xfe, 'Flip lsb')
        self.assertEqual(bitOps.FlipBit(0xff, 7), 0x7f, 'Flip msb')
        self.assertEqual(bitOps.FlipBit(0x00, 0), 0x01, 'Flip lsb')
        self.assertEqual(bitOps.FlipBit(0x00, 7), 0x80, 'Flip msb') 
    
    def test_CheckBits(self):
        self.assertEqual(bitOps.CheckBits(0xff, 0x0f), True, 'Check first octet')
        self.assertEqual(bitOps.CheckBits(0xff, 0xf0), True, 'Check second octet')
        self.assertEqual(bitOps.CheckBits(0x00, 0x0f), False, 'Check first octet')
        self.assertEqual(bitOps.CheckBits(0x00, 0xf0), False, 'Check second octet') 
    
    def test_SetBits(self):
        self.assertEqual(bitOps.SetBits(0x00, 0x0f), 0x0f, 'Set first octet')
        self.assertEqual(bitOps.SetBits(0xa0, 0x0f), 0xaf, 'Set first octet')
        self.assertEqual(bitOps.SetBits(0xa5, 0xc0), 0xe5, 'Set last two bits')
        self.assertEqual(bitOps.SetBits(0x5a, 0xc0), 0xda, 'Set last two bits')

    def test_ClearBits(self):
        self.assertEqual(bitOps.ClearBits(0xff, 0x0f), 0xf0, 'Clear first octet')
        self.assertEqual(bitOps.ClearBits(0xaf, 0x0f), 0xa0, 'Clear first octet')
        self.assertEqual(bitOps.ClearBits(0xa5, 0xc0), 0x25, 'Clear last two bits')
        self.assertEqual(bitOps.ClearBits(0x5a, 0xc0), 0x1a, 'Clear last two bits')    

    def test_FlipBits(self):
        self.assertEqual(bitOps.FlipBits(0x0f, 0x0f), 0x00, 'Flip first octet')
        self.assertEqual(bitOps.FlipBits(0x0a, 0x05), 0x0f, 'Flip first octet')
        self.assertEqual(bitOps.FlipBits(0xa5, 0xc0), 0x65, 'Flip last two bits')
        self.assertEqual(bitOps.FlipBits(0x5a, 0xc0), 0x9a, 'Flip last two bits')    

    def test_SetValueUnderMask(self):
        self.assertEqual(bitOps.SetValueUnderMask(0x01, 0x00, 0xf0), 0x10)
        self.assertEqual(bitOps.SetValueUnderMask(0x0e, 0xff, 0xf0), 0xef)
        self.assertEqual(bitOps.SetValueUnderMask(0x00, 0xff, 0xf0), 0x0f)
        self.assertEqual(bitOps.SetValueUnderMask(0x00, 0xff, 0x01), 0xfe)
    
    def test_GetValueUnderMask(self):
        self.assertEqual(bitOps.GetValueUnderMask(0xa5, 0xf0), 0x0a)
        self.assertEqual(bitOps.GetValueUnderMask(0x95, 0x30), 0x01)

        
        
if __name__ == '__main__':
    unittest.main()



