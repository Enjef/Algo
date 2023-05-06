/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function(n) {
    return function() {
        res = n
        n += 1
        return res
    };
};

/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */


// best speed
var createCounter = function(n) {
    return function() {
        return n++;
        
    };
};
