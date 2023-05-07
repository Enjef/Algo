/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let n = init;
    return {
        increment: () => ++n,
        decrement: () => --n,
        reset: () => n = init
    }
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */

// best speed

const createCounter = (init) => {
    let val = init;
    return {
      increment: () => ++val,
      decrement: () => --val,
      reset: () => (val = init),
    };
  };


// 2nd best speed

  var createCounter = function(init) {
    const initialValue = init
    let currentValue = init
    
    function increment(){return ++currentValue}
    function decrement(){return --currentValue}
    function reset(){return currentValue = initialValue}
    
    return {increment, decrement, reset}
};


// 2nd best memory

var createCounter = function(init) {
    let track=init;
    function increment(){
        track++;
        return track;
    }
        function decrement(){
        track--;
        return track;
    }
        function reset(){
        track=init;
        return track;
    }
    return{
        increment,
        decrement,
        reset
    }
};
