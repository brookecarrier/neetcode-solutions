class Solution {
public:
    uint32_t reverseBits(uint32_t n) {

        uint32_t result = 0;

        for (int i = 0; i < 32; i++) {
            result <<= 1; // shift left to make space
            result |= (n&1); // append last value of n to result
            n >>= 1; // shift n to get next value
        }

        return result;
        
    }
};
