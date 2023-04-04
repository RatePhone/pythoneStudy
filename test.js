var x = 1;

function *foo() {
    x++;
    yield; // 暂停！
    console.log("x:", x);
};

function bar() {
    x++;
}

var it = foo();

it.next(); // 第一次执行 next函数 那么 会执行到 yield之前 

console.log("人工打印", x)

bar();
console.log("人工打印", x)
it.next(); // 后续执行 会执行 yield后面的代码 如果执行完了 那么 后续再次调用 就不会执行了


function *foo2(x) {
    var y = x * (yield);     // <-- yield一个值！
    return y;
}

var it2 = foo2(6);

var res = it2.next();    // 第一个next()，并不传入任何东西
res.value;   
console.log("结果值", res)           // "Hello"

res = it2.next(7);     // 向等待的yield传入7
res.value;              // 42
console.log("结果值2", res)  